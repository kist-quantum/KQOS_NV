
`timescale 1 ns / 1 ps

	module axi_patt_generator_v1_0 #
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
        input wire i_pl_clk_ref,
        input wire i_pl_trig,
        output wire o_pl_pattern,
        
        output wire [16:0] o_pl_ram_add,
        output wire [15:0] o_pl_ram_data,
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
	wire w_resetn;
	wire [16:0] w_ram_wr_add;
	wire [15:0] w_ram_wr_data;
	wire w_ram_wr_wen;
	wire w_ram_rd_add_sel;
	wire [16:0] w_ps_ram_rd_add;
	wire [16:0] w_pl_ram_rd_add;
	wire [16:0] w_ram_rd_add;
	wire [15:0] w_ram_rd_data;
	
	assign w_ram_rd_add = w_ram_rd_add_sel ? w_ps_ram_rd_add : w_pl_ram_rd_add;
	
// Instantiation of Axi Bus Interface S00_AXI
	axi_patt_generator_v1_0_S00_AXI # ( 
		.C_S_AXI_DATA_WIDTH(C_S00_AXI_DATA_WIDTH),
		.C_S_AXI_ADDR_WIDTH(C_S00_AXI_ADDR_WIDTH)
	) axi_patt_generator_v1_0_S00_AXI_inst (
        .o_slv_reg0(w_resetn), //resetn
        .o_slv_reg7(w_ram_wr_add), //ram_wr_add
        .o_slv_reg8(w_ram_wr_data), //ram_wr_data
        .o_slv_reg9(w_ram_wr_wen), //ram_wr_wen: '0': read, '1': write
        .o_slv_reg10(w_ram_rd_add_sel), //ram_rd_add_sel: '0': patt_generator, '1': python
        .o_slv_reg11(w_ps_ram_rd_add), //ram_rd_add        
        .i_slv_reg12(w_ram_rd_data), //ram_rd_data
		
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
    patt_generator patt_generator_inst(
    .i_clk_ref(i_pl_clk_ref),
    .i_resetn(w_resetn),
    .i_trig(i_pl_trig),
    .i_ram_data(w_ram_rd_data),
    .o_ram_add(w_pl_ram_rd_add),
    .o_pattern(o_pl_pattern)
    );    
    
    blk_mem_gen_0 blk_mem_gen_0_inst(
    // write port
    .addra(w_ram_wr_add),
    .clka(s00_axi_aclk),
    .dina(w_ram_wr_data),
    .wea(w_ram_wr_wen),
    // read port
    .addrb(w_ram_rd_add),
    .clkb(s00_axi_aclk),
    .doutb(w_ram_rd_data));
	// User logic ends

	endmodule
