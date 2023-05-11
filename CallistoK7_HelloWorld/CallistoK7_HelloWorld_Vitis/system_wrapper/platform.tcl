# 
# Usage: To re-create this platform project launch xsct with below options.
# xsct G:\Sample_codes\Callisto_K7\CallistoK7_HelloWorld\CallistoK7_HelloWorld_Vitis\system_wrapper\platform.tcl
# 
# OR launch xsct and run below command.
# source G:\Sample_codes\Callisto_K7\CallistoK7_HelloWorld\CallistoK7_HelloWorld_Vitis\system_wrapper\platform.tcl
# 
# To create the platform in a different location, modify the -out option of "platform create" command.
# -out option specifies the output directory of the platform project.

platform create -name {system_wrapper}\
-hw {G:\Sample_codes\Callisto_K7\CallistoK7_HelloWorld\system_wrapper.xsa}\
-out {G:/Sample_codes/Callisto_K7/CallistoK7_HelloWorld/CallistoK7_HelloWorld_Vitis}

platform write
domain create -name {standalone_microblaze_0} -display-name {standalone_microblaze_0} -os {standalone} -proc {microblaze_0} -runtime {cpp} -arch {32-bit} -support-app {hello_world}
platform generate -domains 
platform active {system_wrapper}
platform generate -quick
platform generate