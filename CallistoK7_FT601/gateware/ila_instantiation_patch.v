ila_0 ila_phy (
  .clk(sys_clk), // input wire clk

  .probe0(incoming_fifo_syncfifo_din), // input wire [31:0]  probe0  
  .probe1(incoming_fifo_syncfifo_writable), // input wire [0:0]  probe1 
  .probe2(incoming_fifo_syncfifo_we), // input wire [0:0]  probe2 
  
  .probe3(outgoing_fifo_syncfifo_dout), // input wire [31:0]  probe3 
  .probe4(outgoing_fifo_syncfifo_readable), // input wire [0:0]  probe4 
  .probe5(outgoing_fifo_syncfifo_re), // input wire [0:0]  probe5 
  
  .probe6(data_tri_o), // input wire [31:0]  probe6 
  .probe7(data_tri_i), // input wire [31:0]  probe7 
  .probe8(data_tri_oe), // input wire [0:0]  probe8 
  
  .probe9(be_tri_o), // input wire [3:0]  probe9 
  .probe10(be_tri_i), // input wire [3:0]  probe10 
  .probe11(be_tri_oe), // input wire [0:0]  probe11 
  
  .probe12(rxf_n), // input wire [0:0]  probe12 
  .probe13(txe_n), // input wire [0:0]  probe13 
  .probe14(wr_n), // input wire [0:0]  probe14 
  .probe15(rd_n), // input wire [0:0]  probe15 
  .probe16(oe_n), // input wire [0:0]  probe16 
  
  .probe17(curr_op), // input wire [0:0]  probe17 
  .probe18(can_read), // input wire [0:0]  probe18 
  .probe19(can_write), // input wire [0:0]  probe19 
  .probe20(state) // input wire [3:0]  probe20
);

ila_1 ila_cntr (
  .clk(sys_clk), // input wire clk


  .probe0(incoming_fifo_syncfifo_dout), // input wire [31:0]  probe0  
  .probe1(incoming_fifo_syncfifo_readable), // input wire [0:0]  probe1 
  .probe2(incoming_fifo_syncfifo_re), // input wire [0:0]  probe2 
  .probe3(outgoing_fifo_syncfifo_din), // input wire [31:0]  probe3 
  .probe4(outgoing_fifo_syncfifo_writable), // input wire [0:0]  probe4 
  .probe5(outgoing_fifo_syncfifo_we) // input wire [0:0]  probe5
);
