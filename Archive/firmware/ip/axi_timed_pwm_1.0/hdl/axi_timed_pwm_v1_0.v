
`timescale 1 ns / 1 ps

module axi_timed_pwm_v1_0 #
	(
		// Users to add parameters here

		// User parameters ends
		// Do not modify the parameters beyond this line


		// Parameters of Axi Slave Bus Interface S00_AXI
		parameter integer C_S00_AXI_DATA_WIDTH	= 32,
		parameter integer C_S00_AXI_ADDR_WIDTH	= 5
	)
	(
		// Users to add ports here
        input wire i_clk_ref,
        input wire i_trig,
        output wire o_en,
        
        //Debug
        output wire o_comp,
        output wire [C_S00_AXI_DATA_WIDTH-1:0] o_cnt_reps,
        output wire [2:0] o_ps,
        output wire [2:0] o_ns,
        output wire o_trig,
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
	wire [C_S00_AXI_DATA_WIDTH-1:0] w_delay, w_width, w_reps;
	wire w_resetn;
	
	//debug
    assign o_comp = w_comp;
	
// Instantiation of Axi Bus Interface S00_AXI
	axi_timed_pwm_v1_0_S00_AXI # ( 
		.C_S_AXI_DATA_WIDTH(C_S00_AXI_DATA_WIDTH),
		.C_S_AXI_ADDR_WIDTH(C_S00_AXI_ADDR_WIDTH)
	) axi_timed_pwm_v1_0_S00_AXI_inst (
		.o_slv_reg0(w_resetn),
		.o_slv_reg1(w_delay),
		.o_slv_reg2(w_width),
		.o_slv_reg4(w_reps),
		.i_slv_reg5(w_comp),
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
    sig_gen #(
    .DATA_WIDTH(C_S00_AXI_DATA_WIDTH)
    ) sig_gen_inst(
    .i_clk_ref(i_clk_ref),
    .i_trig(i_trig),
    .i_resetn(w_resetn),
    .i_delay(w_delay),
    .i_width(w_width),
    .i_reps(w_reps),
    .o_en(o_en),
    .o_comp(w_comp),    
    .o_cnt_reps(o_cnt_reps),
    .o_ps(o_ps),
    .o_ns(o_ns),
    .o_trig(o_trig));

endmodule
