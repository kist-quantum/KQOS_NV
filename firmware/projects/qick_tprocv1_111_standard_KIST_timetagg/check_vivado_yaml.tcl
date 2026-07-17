puts "vivado=[version -short]"
puts "tcl_patchLevel=$tcl_patchLevel"
puts "auto_path=$auto_path"
set h "D:/Desktop/Xilinx/Vivado/2022.1/tps/tcl/tcllib1.11.1/yaml/huddle.tcl"
puts "huddle_exists=[file exists $h] readable=[file readable $h]"
if {[catch {package require yaml} err]} {
    puts "YAML_REQUIRE_FAIL: $err"
    exit 1
} else {
    puts "YAML_REQUIRE_OK"
    exit 0
}
