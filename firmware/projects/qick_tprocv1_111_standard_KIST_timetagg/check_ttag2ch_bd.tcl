set run_dir "Q:/firmware/projects/qick_tprocv1_111_standard_tc11_ttag2ch_20260709"
set ::origin_dir_loc $run_dir

set top_dir [file join $run_dir "top_kist"]
if {[file isdirectory $top_dir]} {
    file delete -force $top_dir
}

source [file join $run_dir "proj_kist.tcl"]

validate_bd_design
set ttag_intf [get_bd_intf_pins -quiet axi_ttag2ch_0/*]
set ttag_pins [get_bd_pins -quiet axi_ttag2ch_0/*]
set ttag_addr_segs [get_bd_addr_segs -quiet axi_ttag2ch_0/S00_AXI/*]
puts "TTAG_INTF_PINS=$ttag_intf"
puts "TTAG_PINS=$ttag_pins"
puts "TTAG_ADDR_SEGS=$ttag_addr_segs"
foreach seg $ttag_addr_segs {
    puts "TTAG_ADDR_SEG=$seg OFFSET=[get_property OFFSET $seg] RANGE=[get_property RANGE $seg]"
}
save_bd_design
close_project
