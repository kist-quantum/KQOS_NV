# =============================================================================
# ZCU111 KIST + 2ch time-tagger Build Script
# tc11 경험 적용:
#   - post-route physopt 비활성화
#   - ExtraNetDelay_high 배치 + NoTimingRelaxation 라우팅
#   - route 후 즉시 WNS 확인 → 충족 시 비트스트림 생성
# =============================================================================

# Q: must be subst'd to D:/Vivado/260513_DYK_workspace/qick_240903 before Vivado runs
# This keeps .Xil tmp paths under 146 chars (Chipscope dbg_hub path limit)
set run_dir "Q:/firmware/projects/qick_tprocv1_111_standard_tc11_ttag2ch_20260709"
set ::origin_dir_loc $run_dir

# Make Vivado 2022.1 tcllib explicit before IP customization.
# A previous full build saw the diff_clock IP GUI fail to load yaml/huddle
# despite the file existing and a standalone package check passing.
set vivado_tcllib_dir "D:/Desktop/Xilinx/Vivado/2022.1/tps/tcl/tcllib1.11.1"
if {[file isdirectory $vivado_tcllib_dir] && [lsearch -exact $auto_path $vivado_tcllib_dir] < 0} {
    lappend auto_path $vivado_tcllib_dir
}
foreach required_pkg {math::bignum yaml} {
    if {[catch {package require $required_pkg} pkg_err]} {
        puts "ERROR: failed to preload Tcl package $required_pkg: $pkg_err"
        exit 10
    }
}

# ── 잔여 top_kist 디렉토리 제거 ─────────────────────────────────────────
set top_dir [file join $run_dir "top_kist"]
if {[file isdirectory $top_dir]} {
    puts "Removing existing top_kist directory..."
    file delete -force $top_dir
}

# ── 프로젝트 생성 ────────────────────────────────────────────────────────
source [file join $run_dir "proj_kist.tcl"]

set artifact_dir [file join $run_dir "artifacts_ttag2ch"]
set report_dir   [file join $run_dir "reports_ttag2ch"]
file mkdir $artifact_dir
file mkdir $report_dir

proc write_status {msg} {
    global report_dir
    set ts [clock format [clock seconds] -format {%Y-%m-%d %H:%M:%S}]
    set line "$ts $msg"
    set fp [open [file join $report_dir "build_status.txt"] a]
    puts $fp $line
    close $fp
    puts "BUILD: $line"
    flush stdout
}

proc get_wns {} {
    set p [get_timing_paths -max_paths 1 -nworst 1 -setup -quiet]
    if {[llength $p] == 0} { return 999.0 }
    return [get_property SLACK [lindex $p 0]]
}

proc get_whs {} {
    set p [get_timing_paths -max_paths 1 -nworst 1 -hold -quiet]
    if {[llength $p] == 0} { return 999.0 }
    return [get_property SLACK [lindex $p 0]]
}

set_param general.maxThreads 8

# 상태 파일 초기화
set sf [file join $report_dir "build_status.txt"]
if {[file exists $sf]} { file delete -force $sf }

write_status "=== KIST ZCU111 2ch Time Tagger Build Start ==="

# ── OOC IP 합성 캐시 리셋 (KIST IP HDL 변경 반영 보장) ──────────────────
write_status "Resetting KIST OOC IP synthesis runs..."
foreach run [get_runs -filter {IS_SYNTHESIS == 1}] {
    if {[string match "*axi_timed_pwm*" $run] || \
        [string match "*axi_patt_generator*" $run] || \
        [string match "*axi_async_counter*" $run] || \
        [string match "*axi_spd_mux*" $run]} {
        write_status "  reset_run $run"
        reset_run $run
    }
}

# ── 합성 ─────────────────────────────────────────────────────────────────
set_property strategy Flow_PerfOptimized_high [get_runs synth_1]
write_status "Launching synth_1 (Flow_PerfOptimized_high)..."
reset_run synth_1
launch_runs synth_1 -jobs 8
wait_on_run synth_1
set synth_status   [get_property STATUS   [get_runs synth_1]]
set synth_progress [get_property PROGRESS [get_runs synth_1]]
write_status "synth_1 status=$synth_status progress=$synth_progress"

if {$synth_progress ne "100%"} {
    write_status "ERROR: synth_1 did not complete"
    exit 1
}

open_run synth_1 -name synth_1
report_utilization -file [file join $report_dir "synth_utilization.rpt"]
report_timing_summary -file [file join $report_dir "synth_timing_summary.rpt"]
close_design

# ── 구현: attempt7 검증된 전략 (ExploreWithRemap opt + ExtraNetDelay_high place
#         + AggressiveExplore physopt + NoTimingRelaxation route + AggressiveExplore post-physopt
#         + tproc Pblock — attempt7 에서 WNS=-0.001 달성한 조합) ─────────────
write_status "Setting up impl_kist (attempt7 strategy)..."
set impl_run [create_run impl_kist -parent_run synth_1 -flow {Vivado Implementation 2022}]
set_property strategy Performance_ExplorePostRoutePhysOpt $impl_run

# post-route physopt 활성화 (attempt7 적용)
set_property STEPS.POST_ROUTE_PHYS_OPT_DESIGN.IS_ENABLED true $impl_run
set_property STEPS.POST_ROUTE_PHYS_OPT_DESIGN.ARGS.DIRECTIVE AggressiveExplore $impl_run

# 배치/라우팅 디렉티브 (attempt7)
set_property STEPS.OPT_DESIGN.ARGS.DIRECTIVE ExploreWithRemap $impl_run
set_property STEPS.PLACE_DESIGN.ARGS.DIRECTIVE ExtraNetDelay_high $impl_run
set_property STEPS.PHYS_OPT_DESIGN.ARGS.DIRECTIVE AggressiveExplore $impl_run
set_property STEPS.ROUTE_DESIGN.ARGS.DIRECTIVE NoTimingRelaxation $impl_run

# ── tproc Pblock: dmem BRAM 과 regfile 을 같은 영역에 묶어 1.5ns 라우팅 이격 방지 ──
# attempt3 에서 -0.113 → -0.011 90% 개선을 달성한 핵심 제약
write_status "Writing tproc pblock XDC..."
set pblock_xdc [file join $run_dir "pblock_tproc.xdc"]
set fp [open $pblock_xdc w]
puts $fp "# Pblock: axis_tproc64x32_x8_0 — keep dmem BRAM co-located with regfile"
puts $fp "create_pblock pblock_tproc"
puts $fp "add_cells_to_pblock \[get_pblocks pblock_tproc\] \[get_cells -quiet d_1_i/axis_tproc64x32_x8_0\]"
puts $fp "resize_pblock \[get_pblocks pblock_tproc\] -add {SLICE_X0Y0:SLICE_X59Y199}"
puts $fp "resize_pblock \[get_pblocks pblock_tproc\] -add {RAMB36_X0Y0:RAMB36_X5Y39}"
puts $fp "resize_pblock \[get_pblocks pblock_tproc\] -add {RAMB18_X0Y0:RAMB18_X5Y79}"
puts $fp "resize_pblock \[get_pblocks pblock_tproc\] -add {DSP48E2_X0Y0:DSP48E2_X7Y79}"
close $fp
set existing_pb [get_files -quiet $pblock_xdc]
if {$existing_pb eq ""} {
    add_files -fileset [get_filesets constrs_1] $pblock_xdc
    write_status "Added pblock_tproc.xdc to constrs_1"
} else {
    write_status "pblock_tproc.xdc already in constrs_1"
}

write_status "Launching impl_kist through post-route physopt..."
launch_runs impl_kist -jobs 8
wait_on_run impl_kist
set impl_status   [get_property STATUS   $impl_run]
set impl_progress [get_property PROGRESS $impl_run]
write_status "impl_kist status=$impl_status progress=$impl_progress"

# route 완료 여부 확인
set route_ok 0
if {[string first "Complete" $impl_status] >= 0}               { set route_ok 1 }
if {[string first "Failed Timing" $impl_status] >= 0}          { set route_ok 1 }
if {[string first "Not started phys_opt_design" $impl_status] >= 0} { set route_ok 1 }
if {$impl_progress eq "100%"}                                   { set route_ok 1 }

if {!$route_ok} {
    write_status "ERROR: impl_kist route did not complete"
    exit 2
}

# ── 타이밍 확인 (open_checkpoint 방식) ──────────────────────────────────
set impl_dir [get_property DIRECTORY $impl_run]
set dcp_candidates [list \
    [file join $impl_dir "d_1_wrapper_routed.dcp"] \
    [file join $impl_dir "top_kist.runs" "impl_kist" "d_1_wrapper_routed.dcp"] \
]

set dcp ""
foreach candidate $dcp_candidates {
    if {[file exists $candidate]} {
        set dcp $candidate
        break
    }
}

if {$dcp eq ""} {
    # Try open_run (may work in 2022.1)
    write_status "DCP not found directly; trying open_run..."
    if {[catch {open_run impl_kist -name impl_kist} err]} {
        write_status "open_run failed: $err"
        write_status "Searching for routed DCP..."
        set found_dcps [glob -nocomplain [file join $impl_dir "*.dcp"]]
        write_status "Available DCPs: $found_dcps"
        exit 3
    }
} else {
    write_status "open_checkpoint: $dcp"
    open_checkpoint $dcp
}

set wns [get_wns]
set whs [get_whs]
write_status "post_route WNS=$wns WHS=$whs"

# 상세 타이밍 리포트
report_timing_summary \
    -delay_type min_max -report_unconstrained \
    -max_paths 50 -check_timing_verbose \
    -file [file join $report_dir "impl_timing_summary.rpt"]
report_timing -setup -max_paths 20 -nworst 5 \
    -file [file join $report_dir "impl_timing_setup.rpt"]
report_timing -hold -max_paths 10 -nworst 3 \
    -file [file join $report_dir "impl_timing_hold.rpt"]
report_utilization -hierarchical -hierarchical_depth 3 \
    -file [file join $report_dir "impl_utilization.rpt"]
report_route_status -file [file join $report_dir "impl_route_status.rpt"]
report_drc -file [file join $report_dir "impl_drc.rpt"]

if {$wns >= 0.0 && $whs >= 0.0} {
    write_status "TIMING_MET WNS=$wns WHS=$whs — writing bitstream"
    write_bitstream -force [file join $artifact_dir "top_kist_ttag2ch_zcu111.bit"]
    # HWH 파일 복사
    foreach hwh_file [glob -nocomplain \
        [file join $run_dir "top_kist" "top_kist.gen" "sources_1" "bd" "d_1" "hw_handoff" "*.hwh"] \
        [file join $run_dir "top_kist" "top_kist.srcs" "sources_1" "bd" "d_1" "hw_handoff" "*.hwh"]] {
        file copy -force $hwh_file $artifact_dir
        file copy -force $hwh_file [file join $artifact_dir "top_kist_ttag2ch_zcu111.hwh"]
        write_status "Copied HWH: [file tail $hwh_file]"
    }
    close_design
    write_status "=== BUILD SUCCESS ==="
    exit 0
} else {
    write_status "TIMING_NOT_MET WNS=$wns WHS=$whs"
    write_status "Consider a follow-up ttag2ch timing-closure attempt with AltSpreadLogic_high"
    close_design
    exit 4
}
