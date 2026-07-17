# Pblock: axis_tproc64x32_x8_0 ?€? keep dmem BRAM co-located with regfile
create_pblock pblock_tproc
add_cells_to_pblock [get_pblocks pblock_tproc] [get_cells -quiet d_1_i/axis_tproc64x32_x8_0]
resize_pblock [get_pblocks pblock_tproc] -add {SLICE_X0Y0:SLICE_X59Y199}
resize_pblock [get_pblocks pblock_tproc] -add {RAMB36_X0Y0:RAMB36_X5Y39}
resize_pblock [get_pblocks pblock_tproc] -add {RAMB18_X0Y0:RAMB18_X5Y79}
resize_pblock [get_pblocks pblock_tproc] -add {DSP48E2_X0Y0:DSP48E2_X7Y79}
