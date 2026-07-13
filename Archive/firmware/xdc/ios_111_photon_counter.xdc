set_property PACKAGE_PIN C17 [get_ports PMOD0_0_LS]
set_property IOSTANDARD LVCMOS12 [get_ports PMOD0_0_LS]
set_property PACKAGE_PIN M18 [get_ports PMOD0_1_LS]
set_property IOSTANDARD LVCMOS12 [get_ports PMOD0_1_LS]
set_property PACKAGE_PIN H16 [get_ports PMOD0_2_LS]
set_property IOSTANDARD LVCMOS12 [get_ports PMOD0_2_LS]
set_property CLOCK_DEDICATED_ROUTE FALSE [get_nets PMOD0_2_LS_IBUF_inst/O]
set_property PACKAGE_PIN H17 [get_ports PMOD0_3_LS]
set_property IOSTANDARD LVCMOS12 [get_ports PMOD0_3_LS]
set_property PACKAGE_PIN J16 [get_ports PMOD0_4_LS]
set_property IOSTANDARD LVCMOS12 [get_ports PMOD0_4_LS]
set_property PACKAGE_PIN K16 [get_ports PMOD0_5_LS]
set_property IOSTANDARD LVCMOS12 [get_ports PMOD0_5_LS]
set_property PACKAGE_PIN H15 [get_ports PMOD0_6_LS]
set_property IOSTANDARD LVCMOS12 [get_ports PMOD0_6_LS]
set_property PACKAGE_PIN J15 [get_ports PMOD0_7_LS]
set_property IOSTANDARD LVCMOS12 [get_ports PMOD0_7_LS]

set_property PACKAGE_PIN L14 [get_ports PMOD1_0_LS]
set_property IOSTANDARD LVCMOS12 [get_ports PMOD1_0_LS]
#set_property PACKAGE_PIN L15      	[get_ports "PMOD1_1_LS"];
#set_property IOSTANDARD  LVCMOS12 	[get_ports "PMOD1_1_LS"];
set_property PACKAGE_PIN M13 [get_ports PMOD1_2_LS]
set_property IOSTANDARD LVCMOS12 [get_ports PMOD1_2_LS]
set_property CLOCK_DEDICATED_ROUTE FALSE [get_nets PMOD1_2_LS_IBUF_inst/O]
#set_property PACKAGE_PIN N13      	[get_ports "PMOD1_3_LS"];
#set_property IOSTANDARD  LVCMOS12 	[get_ports "PMOD1_3_LS"];
set_property PACKAGE_PIN M15      	[get_ports PMOD1_4_LS];
set_property IOSTANDARD  LVCMOS12 	[get_ports PMOD1_4_LS];
set_property PACKAGE_PIN N15 [get_ports PMOD1_5_LS]
set_property IOSTANDARD LVCMOS12 [get_ports PMOD1_5_LS]
set_property PACKAGE_PIN M14 [get_ports PMOD1_6_LS]
set_property IOSTANDARD LVCMOS12 [get_ports PMOD1_6_LS]
set_property PACKAGE_PIN N14 [get_ports PMOD1_7_LS]
set_property IOSTANDARD LVCMOS12 [get_ports PMOD1_7_LS]
set_property CLOCK_DEDICATED_ROUTE FALSE [get_nets PMOD1_7_LS_IBUF_inst/O]

#set_property SEVERITY {Warning} [get_drc_checks UCIO-1]

set_property C_CLK_INPUT_FREQ_HZ 300000000 [get_debug_cores dbg_hub]
set_property C_ENABLE_CLK_DIVIDER false [get_debug_cores dbg_hub]
set_property C_USER_SCAN_CHAIN 1 [get_debug_cores dbg_hub]
connect_debug_port dbg_hub/clk [get_nets clk]
