Callisto K7 DDR3 Project
Numato Lab
https://www.numato.com

This package contains source and other files necessary to build this project for Callisto Kintex 7 FPGA Development board.
This project is built on Vivado design suite 2022.1 and Vitis IDE 2022.1.

This project is created by selecting the part number of Callisto K7 board instead of selecting the board itself.

Open the project(.xpr) file and Open the Block Design. Then Generate the Bitstream along with binary file (select it in Generate Bitstream settings). After the Bitstream is generated successfully, the .bit and .bin 
files will be created in the "CallistoK7_DDR3.runs-->impl_1" folder. Then export the generated bitstream by selecting "Export Hardware" under "File--> Export". Include the bitstream while exporting the hardware. Then launch Vitis IDE and program the board from Vitis and observe the output in the Vitis terminal.
