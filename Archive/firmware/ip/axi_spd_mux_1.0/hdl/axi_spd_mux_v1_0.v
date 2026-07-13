
`timescale 1 ns / 1 ps

	module axi_spd_mux_v1_0 #
	(
		// Users to add parameters here

		// User parameters ends
		// Do not modify the parameters beyond this line


		// Parameters of Axi Slave Bus Interface S00_AXI
		parameter integer C_S00_AXI_DATA_WIDTH	= 32,
		parameter integer C_S00_AXI_ADDR_WIDTH	= 6
	)
	(
		// Users to add ports here
		input wire [1:0] i_pl_spd,
		output wire o_pl_counter0,
		output wire o_pl_counter1,
		output wire o_pl_counter2,
		output wire o_pl_counter3,
		output wire o_pl_counter4,
		output wire o_pl_counter5,
		output wire o_pl_counter6,
		output wire o_pl_counter7,
		output wire o_pl_counter8,
		output wire o_pl_counter9,
		output wire o_pl_counter10,
		output wire o_pl_counter11,
		output wire o_pl_counter12,
		output wire o_pl_counter13,
		output wire o_pl_counter14,
		output wire o_pl_counter15,
		// User ports ends
		// Do not modify the ports beyond this line


		// Ports of Axi Slave Bus Interface S00_AXI
		input wire  s00_axi_aclk,
		input wire  s00_axi_aresetn,
		input wire [C_S00_AXI_ADDR_WIDTH-1 : 0] s00_axi_awaddr,
		input wire [2 : 0] s00_axi_awprot,
		input wire  s00_axi_awvalid,
		output wire  s00_axi_awready,
		input wire [C_S00_AXI_DATA_WIDTH-1 : 0] s00_axi_wdata,
		input wire [(C_S00_AXI_DATA_WIDTH/8)-1 : 0] s00_axi_wstrb,
		input wire  s00_axi_wvalid,
		output wire  s00_axi_wready,
		output wire [1 : 0] s00_axi_bresp,
		output wire  s00_axi_bvalid,
		input wire  s00_axi_bready,
		input wire [C_S00_AXI_ADDR_WIDTH-1 : 0] s00_axi_araddr,
		input wire [2 : 0] s00_axi_arprot,
		input wire  s00_axi_arvalid,
		output wire  s00_axi_arready,
		output wire [C_S00_AXI_DATA_WIDTH-1 : 0] s00_axi_rdata,
		output wire [1 : 0] s00_axi_rresp,
		output wire  s00_axi_rvalid,
		input wire  s00_axi_rready
	);
	//assigns
	wire [15:0] w_ps_spd_sel;  //Python에서 설정한 SPD selection, '0': spd1, '1':spd2
	                           //[0]: counter0
	                           //[1]: counter1
	                           //..
	                           //[14]: counter14
	                           //[15]: counter15
	assign o_pl_counter0 = i_pl_spd[w_ps_spd_sel[0]];
	assign o_pl_counter1 = i_pl_spd[w_ps_spd_sel[1]];
	assign o_pl_counter2 = i_pl_spd[w_ps_spd_sel[2]];
	assign o_pl_counter3 = i_pl_spd[w_ps_spd_sel[3]];
	assign o_pl_counter4 = i_pl_spd[w_ps_spd_sel[4]];
	assign o_pl_counter5 = i_pl_spd[w_ps_spd_sel[5]];
	assign o_pl_counter6 = i_pl_spd[w_ps_spd_sel[6]];
	assign o_pl_counter7 = i_pl_spd[w_ps_spd_sel[7]];
	assign o_pl_counter8 = i_pl_spd[w_ps_spd_sel[8]];
	assign o_pl_counter9 = i_pl_spd[w_ps_spd_sel[9]];
	assign o_pl_counter10 = i_pl_spd[w_ps_spd_sel[10]];
	assign o_pl_counter11 = i_pl_spd[w_ps_spd_sel[11]];
	assign o_pl_counter12 = i_pl_spd[w_ps_spd_sel[12]];
	assign o_pl_counter13 = i_pl_spd[w_ps_spd_sel[13]];
	assign o_pl_counter14 = i_pl_spd[w_ps_spd_sel[14]];
	assign o_pl_counter15 = i_pl_spd[w_ps_spd_sel[15]];	
	
// Instantiation of Axi Bus Interface S00_AXI
	axi_spd_mux_v1_0_S00_AXI # ( 
		.C_S_AXI_DATA_WIDTH(C_S00_AXI_DATA_WIDTH),
		.C_S_AXI_ADDR_WIDTH(C_S00_AXI_ADDR_WIDTH)
	) axi_spd_mux_v1_0_S00_AXI_inst (
		.o_slv_reg13(w_ps_spd_sel),
		.S_AXI_ACLK(s00_axi_aclk),
		.S_AXI_ARESETN(s00_axi_aresetn),
		.S_AXI_AWADDR(s00_axi_awaddr),
		.S_AXI_AWPROT(s00_axi_awprot),
		.S_AXI_AWVALID(s00_axi_awvalid),
		.S_AXI_AWREADY(s00_axi_awready),
		.S_AXI_WDATA(s00_axi_wdata),
		.S_AXI_WSTRB(s00_axi_wstrb),
		.S_AXI_WVALID(s00_axi_wvalid),
		.S_AXI_WREADY(s00_axi_wready),
		.S_AXI_BRESP(s00_axi_bresp),
		.S_AXI_BVALID(s00_axi_bvalid),
		.S_AXI_BREADY(s00_axi_bready),
		.S_AXI_ARADDR(s00_axi_araddr),
		.S_AXI_ARPROT(s00_axi_arprot),
		.S_AXI_ARVALID(s00_axi_arvalid),
		.S_AXI_ARREADY(s00_axi_arready),
		.S_AXI_RDATA(s00_axi_rdata),
		.S_AXI_RRESP(s00_axi_rresp),
		.S_AXI_RVALID(s00_axi_rvalid),
		.S_AXI_RREADY(s00_axi_rready)
	);

	// Add user logic here

	// User logic ends

	endmodule
