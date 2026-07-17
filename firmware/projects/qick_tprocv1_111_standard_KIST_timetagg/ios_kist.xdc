# =============================================================================
# ZCU111 KIST IO Constraint
# 원본 ios.xdc 기반, KIST PMOD 핀 추가/변경
# =============================================================================

# PMOD0 - 기존 그대로 유지 (핀 매핑 동일, 이름만 BD에서 변경)
set_property PACKAGE_PIN C17      	[get_ports "PMOD0_0_LS"];
set_property IOSTANDARD  LVCMOS12   [get_ports "PMOD0_0_LS"];
set_property PACKAGE_PIN M18      	[get_ports "PMOD0_1_LS"];
set_property IOSTANDARD  LVCMOS12 	[get_ports "PMOD0_1_LS"];

# PMOD0_2: Input (SPD1 광센서)
set_property PACKAGE_PIN H16      	[get_ports "PMOD0_2_LS_SPD1"];
set_property IOSTANDARD  LVCMOS12 	[get_ports "PMOD0_2_LS_SPD1"];

set_property PACKAGE_PIN H17      	[get_ports "PMOD0_3_LS"];
set_property IOSTANDARD  LVCMOS12 	[get_ports "PMOD0_3_LS"];

# PMOD0_4: Output (patt_generator LASER)
set_property PACKAGE_PIN J16      	[get_ports "PMOD0_4_LS_LASER"];
set_property IOSTANDARD  LVCMOS12 	[get_ports "PMOD0_4_LS_LASER"];

# PMOD0_5..7: Output (timed PWM enable/count)
set_property PACKAGE_PIN K16      	[get_ports "PMOD0_5_LS_CNT1"];
set_property IOSTANDARD  LVCMOS12 	[get_ports "PMOD0_5_LS_CNT1"];
set_property PACKAGE_PIN H15      	[get_ports "PMOD0_6_LS_CNT2"];
set_property IOSTANDARD  LVCMOS12 	[get_ports "PMOD0_6_LS_CNT2"];
set_property PACKAGE_PIN J15      	[get_ports "PMOD0_7_LS_CNT3"];
set_property IOSTANDARD  LVCMOS12 	[get_ports "PMOD0_7_LS_CNT3"];

# PMOD1_0: Input (기존 - tProc start)
set_property PACKAGE_PIN L14      	[get_ports "PMOD1_0_LS"];
set_property IOSTANDARD  LVCMOS12 	[get_ports "PMOD1_0_LS"];

# PMOD1_2: Input (SPD2 광센서)
set_property PACKAGE_PIN M13      	[get_ports "PMOD1_2_LS_SPD2"];
set_property IOSTANDARD  LVCMOS12 	[get_ports "PMOD1_2_LS_SPD2"];

# PMOD1_3: Output (vect2bits_16_0/dout12 RAW trigger, PWM 우회 — 신규)
set_property PACKAGE_PIN N13      	[get_ports "PMOD1_3_LS"];
set_property IOSTANDARD  LVCMOS12 	[get_ports "PMOD1_3_LS"];

# PMOD1_4: Output (PWM3 enable - LASER)
set_property PACKAGE_PIN M15      	[get_ports "PMOD1_4_LS_LASER"];
set_property IOSTANDARD  LVCMOS12 	[get_ports "PMOD1_4_LS_LASER"];

# PMOD1_5..6: Output (timed PWM enable/count)
set_property PACKAGE_PIN N15      	[get_ports "PMOD1_5_LS_CNT1"];
set_property IOSTANDARD  LVCMOS12 	[get_ports "PMOD1_5_LS_CNT1"];
set_property PACKAGE_PIN M14      	[get_ports "PMOD1_6_LS_CNT2"];
set_property IOSTANDARD  LVCMOS12 	[get_ports "PMOD1_6_LS_CNT2"];

# PMOD1_7: Input (SPD3 광센서 — 구 v6 호환 핀 N14)
set_property PACKAGE_PIN N14      	[get_ports "PMOD1_7_LS_SPD3"];
set_property IOSTANDARD  LVCMOS12 	[get_ports "PMOD1_7_LS_SPD3"];

# =============================================================================
# SPD inputs: prevent automatic BUFG insertion (Sub-optimal CCIO→BUFG error fix)
# SPD detector pulses go to xlconcat_1 → 13개 카운터 i_sig 로 fanout
# Vivado가 자동으로 BUFG 삽입 시 BUFGCE 위치가 IO 뱅크와 멀어 placement 실패
# → CLOCK_DEDICATED_ROUTE FALSE 로 non-dedicated 라우팅 허용
# (구 ios_111_kist_bramcounter.xdc 에서 사용된 패턴)
# =============================================================================
set_property CLOCK_DEDICATED_ROUTE FALSE [get_nets PMOD0_2_LS_SPD1_IBUF_inst/O]
set_property CLOCK_DEDICATED_ROUTE FALSE [get_nets PMOD1_2_LS_SPD2_IBUF_inst/O]
set_property CLOCK_DEDICATED_ROUTE FALSE [get_nets PMOD1_7_LS_SPD3_IBUF_inst/O]
