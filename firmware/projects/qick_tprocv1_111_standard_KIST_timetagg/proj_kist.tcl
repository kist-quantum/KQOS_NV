# =============================================================================
# ZCU111 KIST Project Creator
# KIST subsystem (axi_timed_pwm x13, axi_async_counter x13,
#                  axi_patt_generator, axi_spd_mux) 포함 버전
# =============================================================================

set origin_dir "."

if { [info exists ::origin_dir_loc] } {
  set origin_dir $::origin_dir_loc
}

set _xil_proj_name_ "top_kist"

set orig_proj_dir "[file normalize "$origin_dir/"]"

# Create project
create_project ${_xil_proj_name_} [file join $origin_dir ${_xil_proj_name_}] -part xczu28dr-ffvg1517-2-e

set proj_dir [get_property directory [current_project]]

# Set project properties
set obj [current_project]
set_property -name "board_part" -value "xilinx.com:zcu111:part0:1.4" -objects $obj
set_property -name "corecontainer.enable" -value "1" -objects $obj
set_property -name "default_lib" -value "xil_defaultlib" -objects $obj
set_property -name "enable_core_container" -value "1" -objects $obj
set_property -name "enable_resource_estimation" -value "0" -objects $obj
set_property -name "dsa.board_id" -value "zcu111" -objects $obj
set_property -name "dsa.description" -value "Vivado generated DSA" -objects $obj
set_property -name "dsa.dr_bd_base_address" -value "0" -objects $obj
set_property -name "dsa.emu_dir" -value "emu" -objects $obj
set_property -name "dsa.flash_interface_type" -value "bpix16" -objects $obj
set_property -name "dsa.flash_offset_address" -value "0" -objects $obj
set_property -name "dsa.flash_size" -value "1024" -objects $obj
set_property -name "dsa.host_architecture" -value "x86_64" -objects $obj
set_property -name "dsa.host_interface" -value "pcie" -objects $obj
set_property -name "dsa.num_compute_units" -value "60" -objects $obj
set_property -name "dsa.platform_state" -value "pre_synth" -objects $obj
set_property -name "dsa.vendor" -value "xilinx" -objects $obj
set_property -name "dsa.version" -value "0.0" -objects $obj
set_property -name "enable_vhdl_2008" -value "1" -objects $obj
set_property -name "ip_cache_permissions" -value "read write" -objects $obj
set_property -name "ip_output_repo" -value "$proj_dir/${_xil_proj_name_}.cache/ip" -objects $obj
set_property -name "mem.enable_memory_map_generation" -value "1" -objects $obj
set_property -name "platform.board_id" -value "zcu111" -objects $obj
set_property -name "revised_directory_structure" -value "1" -objects $obj
set_property -name "sim.central_dir" -value "$proj_dir/${_xil_proj_name_}.ip_user_files" -objects $obj
set_property -name "sim.ip.auto_export_scripts" -value "1" -objects $obj
set_property -name "simulator_language" -value "Mixed" -objects $obj
set_property -name "xpm_libraries" -value "XPM_CDC XPM_FIFO XPM_MEMORY" -objects $obj

# Set IP repository paths (includes KIST IPs)
set obj [get_filesets sources_1]
set_property "ip_repo_paths" "[file normalize "$origin_dir/../../ip"]" $obj

# Rebuild user ip_repo's index
update_ip_catalog -rebuild

# Set 'sources_1' fileset object
set obj [get_filesets sources_1]
set files [list \
	[ file normalize "$origin_dir/../../hdl/vect2bits_16.v"]	\
	[ file normalize "$origin_dir/hdl/axi_timetag_2ch_snapshot_v1_0.v"]	\
]
add_files -norecurse -fileset $obj $files

# Set 'constrs_1' fileset object
set obj [get_filesets constrs_1]

# Add KIST XDC (uses ios_kist.xdc instead of ios.xdc)
set files [list \
	[ file normalize "$origin_dir/timing.xdc"] 	\
	[ file normalize "$origin_dir/ios_kist.xdc"] 	\
]
add_files -fileset $obj $files

# Source KIST Block Design
set file "[file normalize "$origin_dir/bd_2022-1_kist.tcl"]"
source $file

# Set sources_1 fileset object
set obj [get_filesets sources_1]

# Create HDL Wrapper
make_wrapper -files [get_files d_1.bd] -top

# Add wrapper files
set files [list \
  [file normalize "${origin_dir}/top_kist/top_kist.gen/sources_1/bd/d_1/hdl/d_1_wrapper.v" ]\
]
add_files -fileset $obj $files

set_property strategy "Performance_Explore" [get_runs impl_1]
