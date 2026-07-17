# =============================================================================
# ZCU111 KIST + 2ch time-tagger synth-only check
#
# This script refreshes the local Vivado project, validates/regenerates the BD,
# runs synth_1 only, and writes synthesis reports. It intentionally does not
# launch implementation or write a bitstream.
# =============================================================================

# Q: must be subst'd to D:/Vivado/260513_DYK_workspace/qick_240903 before Vivado
# runs. This mirrors build_ttag2ch.tcl and keeps generated paths short enough for
# Vivado debug/IP flows on Windows.
set run_dir "Q:/firmware/projects/qick_tprocv1_111_standard_tc11_ttag2ch_20260709"
set ::origin_dir_loc $run_dir

set top_dir [file join $run_dir "top_kist"]
set report_dir [file join $run_dir "reports_ttag2ch_synth"]

proc write_status {msg} {
    global report_dir
    set ts [clock format [clock seconds] -format {%Y-%m-%d %H:%M:%S}]
    set line "$ts $msg"
    file mkdir $report_dir
    set fp [open [file join $report_dir "synth_status.txt"] a]
    puts $fp $line
    close $fp
    puts "TTAG2CH_SYNTH: $line"
    flush stdout
}

proc fail {msg code} {
    write_status "ERROR: $msg"
    exit $code
}

file mkdir $report_dir
set sf [file join $report_dir "synth_status.txt"]
if {[file exists $sf]} {
    file delete -force $sf
}

set_param general.maxThreads 8
write_status "=== KIST ZCU111 2ch Time Tagger synth-only start ==="
write_status "run_dir=$run_dir"

if {![file exists $run_dir]} {
    fail "run_dir does not exist; check Q: subst mapping" 10
}

if {[file isdirectory $top_dir]} {
    write_status "Removing existing generated project: $top_dir"
    file delete -force $top_dir
}

set project_tcl [file join $run_dir "proj_kist.tcl"]
if {![file exists $project_tcl]} {
    fail "missing project Tcl: $project_tcl" 11
}

write_status "Sourcing $project_tcl"
if {[catch {source $project_tcl} err]} {
    fail "project creation failed: $err" 12
}

set bd_file [get_files -quiet d_1.bd]
if {[llength $bd_file] > 0} {
    set bd_file [lindex $bd_file 0]
    write_status "Top BD found: $bd_file"
    if {[current_bd_design -quiet] eq ""} {
        if {[catch {open_bd_design $bd_file} err]} {
            write_status "WARNING: could not reopen top BD for address probe: $err"
        }
    }
} else {
    write_status "WARNING: top-level d_1.bd was not found for address probe"
}

if {[current_bd_design -quiet] ne ""} {
    set ttag_intf [get_bd_intf_pins -quiet axi_ttag2ch_0/S00_AXI]
    set ttag_addr_segs [get_bd_addr_segs -quiet axi_ttag2ch_0/S00_AXI/*]
    write_status "ttag_intf=$ttag_intf"
    write_status "ttag_addr_segs=$ttag_addr_segs"
    foreach seg $ttag_addr_segs {
        write_status "ttag_addr_seg=$seg range=[get_property RANGE $seg]"
    }
} else {
    write_status "WARNING: no current BD is open for time-tagger address probe"
}

update_compile_order -fileset sources_1

if {[llength [get_runs -quiet synth_1]] == 0} {
    fail "synth_1 run was not created" 15
}

set_property strategy Flow_PerfOptimized_high [get_runs synth_1]
write_status "Resetting synth_1"
reset_run synth_1

write_status "Launching synth_1"
launch_runs synth_1 -jobs 8
wait_on_run synth_1

set synth_status [get_property STATUS [get_runs synth_1]]
set synth_progress [get_property PROGRESS [get_runs synth_1]]
write_status "synth_1 status=$synth_status progress=$synth_progress"

if {$synth_progress ne "100%"} {
    fail "synth_1 did not complete: status=$synth_status progress=$synth_progress" 20
}
if {[string first "fail" [string tolower $synth_status]] >= 0} {
    fail "synth_1 failed: status=$synth_status" 21
}

open_run synth_1 -name synth_1

write_status "Writing synthesis reports"
report_utilization -file [file join $report_dir "synth_utilization.rpt"]
report_utilization -hierarchical -hierarchical_depth 4 -file [file join $report_dir "synth_utilization_hier.rpt"]
report_timing_summary -delay_type min_max -report_unconstrained -check_timing_verbose -file [file join $report_dir "synth_timing_summary.rpt"]
report_clock_utilization -file [file join $report_dir "synth_clock_utilization.rpt"]
if {[catch {report_cdc -file [file join $report_dir "synth_cdc.rpt"]} err]} {
    write_status "WARNING: report_cdc failed: $err"
}
write_checkpoint -force [file join $report_dir "synth_ttag2ch.dcp"]

close_design
write_status "reports=$report_dir"
write_status "=== SYNTH SUCCESS ==="
exit 0
