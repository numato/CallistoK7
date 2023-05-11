Callisto K7 Microblaze HelloWorld Project
Numato Lab
https://www.numato.com

This package contains source and other files necessary to build this project for Callisto Kintex 7 FPGA Development board.
This project is built on Vivado Design Suite 2022.1 and Vitis 2022.1.

This project is created by selecting the part number of Callisto K7 board instead of selecting the board itself.

Open the project(.xpr) file and Open the Block Design. Then Generate the Bitstream along with binary file (select it in Generate Bitstream settings). After the Bitstream is generated successfully, the .bit and .bin files will be created in the "CallistoK7_HelloWorld.runs-->impl_1" folder. Then export the generated bitstream by selecting "Export Hardware" under "File--> Export". Include the bitstream while exporting the hardware. Then launch Vitis IDE. After launching Vitis if the HelloWorld project is not opened, go to File--> Import and open the "CallistoK7_Microblaze_HelloWorld_Vitis" folder. This will open the HelloWorld project. Now program the board from Vitis and observe the output in the Vitis terminal.
