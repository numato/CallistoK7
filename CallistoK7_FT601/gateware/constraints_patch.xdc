set_output_delay -clock [get_clocks clk100] -min -add_delay -4.800 [get_ports {usb_fifo_be[*]}]
set_output_delay -clock [get_clocks clk100] -max -add_delay 1.000 [get_ports {usb_fifo_be[*]}]
set_output_delay -clock [get_clocks clk100] -min -add_delay -4.800 [get_ports {usb_fifo_data[*]}]
set_output_delay -clock [get_clocks clk100] -max -add_delay 1.000 [get_ports {usb_fifo_data[*]}]
set_output_delay -clock [get_clocks clk100] -min -add_delay -4.800 [get_ports usb_fifo_wr_n]
set_output_delay -clock [get_clocks clk100] -max -add_delay 1.000 [get_ports usb_fifo_wr_n]
