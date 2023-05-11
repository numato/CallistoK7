from migen import *
from migen.genlib.fifo import *
from migen.genlib.io import CRG

from migen.build.generic_platform import *
from migen.build.xilinx import XilinxPlatform
from migen.build.xilinx.programmer import XC3SProg

from migen.fhdl.specials import Special, Memory
from litex.build.xilinx.common import xilinx_special_overrides

txe_delay = 4

class FT601_245(Module):

    def __init__(self, io, width=32):
        # Shared control
        # Data bus is driven by both the FPGA and the FTDI. We use tristate.
        io.oe_n.reset = 1
        io.rd_n.reset = 1
        io.wr_n.reset = 1

        self.data_tri = data_tri = TSTriple(width)
        data_tri.oe.reset = 1
        assert io.data.nbits == width
        self.specials += data_tri.get_tristate(io.data)

        self.be_tri = be_tri = TSTriple(width // 8)
        be_tri.oe.reset = 1
        assert io.be.nbits == width // 8
        self.specials += be_tri.get_tristate(io.be)

        self.comb += [
            be_tri.o.eq(0xf),
            be_tri.oe.eq(1),
            data_tri.oe.eq(1),
            io.oe_n.eq(1)
        ]

        txe_n_d4 = self.txe_n_d4 = Signal()
        txe_n_d5 = self.txe_n_d5 = Signal()
        wr_n_d1 = self.wr_n_d1 = Signal(reset=1)
        wr_n_d0 = self.wr_n_d0 = Signal(reset=1)
        data_d0 = self.data_d0 = Signal(width, reset=0)
        data_d1 = self.data_d1 = Signal(width, reset=0)
        self.specials += MultiReg(io.txe_n, txe_n_d4, n=txe_delay, reset=1)

        self.comb += [
            io.wr_n.eq(wr_n_d1),
            data_tri.o.eq(data_d1),
        ]

        prefetch_counter = Signal(4, reset=0)
        counter = self.counter = Signal(width, reset=0)
        self.sync += [
            txe_n_d5.eq(txe_n_d4),
            data_d1.eq(data_d0),
            wr_n_d1.eq(wr_n_d0),

            data_d0.eq(counter),
            If((txe_n_d4 == 0) & (txe_n_d5 == 0),
                wr_n_d0.eq(0),
                If(prefetch_counter < txe_delay + 2,
                    prefetch_counter.eq(prefetch_counter + 1)
                ).Else(
                    prefetch_counter.eq(prefetch_counter)
                ),
                counter.eq(counter + 1)
            ).Elif(txe_n_d4 == 1,
                wr_n_d0.eq(1),
                prefetch_counter.eq(0),
                counter.eq(counter - prefetch_counter)
            )
        ]

class MultiRegImpl(Module):
    def __init__(self, i, o, odomain, n, reset=0):
        self.i = i
        self.o = o
        self.odomain = odomain

        w, signed = value_bits_sign(self.i)
        self.regs = [Signal((w, signed), reset=reset, reset_less=True)
                for i in range(n)]

        ###

        sd = getattr(self.sync, self.odomain)
        src = self.i
        for reg in self.regs:
            sd += reg.eq(src)
            src = reg
        self.comb += self.o.eq(src)
        for reg in self.regs:
            reg.attr.add("no_retiming")


class MultiReg(Special):
    def __init__(self, i, o, odomain="sys", n=2, reset=0):
        Special.__init__(self)
        self.i = wrap(i)
        self.o = wrap(o)
        self.odomain = odomain
        self.n = n
        self.reset = reset

    def iter_expressions(self):
        yield self, "i", SPECIAL_INPUT
        yield self, "o", SPECIAL_OUTPUT

    def rename_clock_domain(self, old, new):
        Special.rename_clock_domain(self, old, new)
        if self.odomain == old:
            self.odomain = new

    def list_clock_domains(self):
        r = Special.list_clock_domains(self)
        r.add(self.odomain)
        return r

    @staticmethod
    def lower(dr):
        return MultiRegImpl(dr.i, dr.o, dr.odomain, dr.n, dr.reset)

class FT601SourceTop(Module):
    def __init__(self, platform):
        usb_fifo = platform.request("usb_fifo")

        crg = CRG(platform.request(platform.default_clk_name))
        self.submodules.crg = crg

        usb_phy = FT601_245(usb_fifo)
        self.submodules.usb_phy = usb_phy


_io = [
    ("clk100",  0, Pins("N21"), IOStandard("LVCMOS25")),

    ("usb_fifo", 0,
        Subsignal("data", Pins("N17 N18 M19 M20 N19 K25 K26 L24 L25 M24 M25 M26 N22 N24 N26 P16 R16 U16 R17 T17 U17 R18 P26 P25 P24 R26 R25 R23 T25 T24 R22 T22")),
        Subsignal("be", Pins("P18 P19 T18 T19")),
        #Subsignal("clk", Pins("Y23")),  # Used as main system clock clk100
        Subsignal("txe_n", Pins("U19")),
        Subsignal("rxf_n", Pins("R20")),
        Subsignal("wr_n", Pins("R21")),
        Subsignal("rd_n", Pins("P21")),
        Subsignal("oe_n", Pins("T20")),
        Subsignal("wakeup_n", Pins("T23")),
        IOStandard("LVCMOS25"),
    ),
]


class CallistoK7Platform(XilinxPlatform):
    default_clk_name = "clk100"
    default_clk_period = 10.000

    def __init__(self, programmer="xc3sprog"):
        self.programmer = programmer
        XilinxPlatform.__init__(self, "xc7k160tfbg676-2", _io, [], toolchain="vivado")

    def create_programmer(self):
        if self.programmer == "xc3sprog":
            return XC3SProg("jtaghs1")
        else:
            raise ValueError("{} programmer is not supported".format(self.programmer))


default_subtarget = FT601SourceTop
default_platform = CallistoK7Platform

if __name__ == '__main__':
    p = CallistoK7Platform()
    m = FT601SourceTop(p)
    # out = verilog.convert(m, ios=set()))# m.get_ios()))
    p.build(m, build_name="ft601_callisto_k7_160t", build_dir="build_callisto_k7_160t")
