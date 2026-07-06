
`timescale 1 ns / 1 ps

	module axi_counter_v1_0 #
	(
		// Users to add parameters here

		// User parameters ends
		// Do not modify the parameters beyond this line


		// Parameters of Axi Slave Bus Interface S00_AXI
		parameter integer C_S00_AXI_DATA_WIDTH	= 32,
		parameter integer C_S00_AXI_ADDR_WIDTH	= 6,
        parameter integer DATA_WIDTH_CNT = 32,      // 카운터 비트 사이즈
        parameter integer DATA_WIDTH_TIME = 32,     // 타이밍(delay, width) 비트 사이즈
        parameter integer RAM_DEPTH = 16            // RAM ADD 비트 사이즈
		
	)
	(
		// Users to add ports here
        input wire i_pl_clk_ref,
        input wire i_pl_sig,
        input wire i_pl_trig,
        output wire o_pl_cnt_en,
        
//        output wire o_pl_ram_add,        
//        output wire o_ps_resetn,
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
	// assigns
    wire [DATA_WIDTH_TIME-1:0] w_ps_delay;  // Python에서 설정된 enable 신호의 딜레이
    wire [DATA_WIDTH_TIME-1:0] w_ps_width;  // Python에서 설정된 enable 신호의 펄스폭
    wire [DATA_WIDTH_CNT-1:0] w_pl_cnt; // 카운터에서 RAM으로 전달되는 카운터 출력 값
    wire [DATA_WIDTH_CNT-1:0] w_ps_cnt; // 카운터에서 Python으로 전달되는 RAM에 저장된 카운터 출력 값
    wire [RAM_DEPTH-1:0] w_ps_cnt_reps; // Python에서 설정된 카운터 동작 횟수, 동작 횟수 달성할 경우 w_ps_comp 신호가 HIGH 상태가 됨
    wire [RAM_DEPTH-1:0] w_pl_ram_add;  // 카운터에서 RAM으로 전달되는 주소 값
    wire [RAM_DEPTH-1:0] w_ps_ram_add;  // Python에서 RAM으로 전달되는 주소 값
    wire w_ps_resetn;   // Python에서 설정된 리셋 신호
    wire w_pl_cnt_en;   // 카운트 enable 신호
    wire w_pl_cnt_resetn;   // 카운터 리셋
    wire w_pl_ram_clk;  // RAM WR 클럮
    wire w_ps_comp;     // w_ps_cnt_reps 만큼 카운트 후 HIGH 상태로 천이	
    assign o_pl_cnt_en = w_pl_cnt_en;
	assign o_ps_resetn = w_ps_resetn;
	assign o_pl_ram_add = w_pl_ram_add;
// Instantiation of Axi Bus Interface S00_AXI
	axi_counter_v1_0_S00_AXI # ( 
		.C_S_AXI_DATA_WIDTH(C_S00_AXI_DATA_WIDTH),
		.C_S_AXI_ADDR_WIDTH(C_S00_AXI_ADDR_WIDTH)
	) axi_counter_v1_0_S00_AXI_inst (
		.o_slv_reg0(w_ps_resetn),
		.o_slv_reg1(w_ps_delay),
		.o_slv_reg2(w_ps_width),
		.i_slv_reg3(w_ps_cnt),
		.o_slv_reg4(w_ps_cnt_reps),
		.i_slv_reg5(w_ps_comp),
		.o_slv_reg6(w_ps_ram_add),
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
    synchronizer#(.DATA_WIDTH(DATA_WIDTH_TIME),
                  .RAM_DEPTH(RAM_DEPTH))
    synchronizer_inst(.i_pl_clk(i_pl_clk_ref),    // 레퍼런스 클럭, o_en 신호의 타이밍 resolution 결정
                      .i_pl_trig(i_pl_trig),   // 트리거 신호, QICK lib.의 AveragerProgram.trigger() 함수로 발생된 트리거 신호
                      .i_ps_resetn(w_ps_resetn), // 리셋 신호, Python에서 전달 받은 리셋 신호
                      .i_ps_delay(w_ps_delay), // i_pl_trig 신호와 o_en 신호 간 딜레이, i_pl_trig 감지 후 i_ps_delay 후 o_en -> 'High'
                      .i_ps_width(w_ps_width), // o_en 신호의 펄스 폭
                      .i_ps_cnt_reps(w_ps_cnt_reps),   // 카운터 동작 횟수, readout 횟수
                      .o_pl_cnt_en(w_pl_cnt_en),   // 카운터 enable 신호, 카운터 모듈로 전달
                      .o_pl_cnt_resetn(w_pl_cnt_resetn),   // 카운터 resetn 신호, 카운터 모듈로 전달
                      .o_pl_ram_clk(w_pl_ram_clk),  // RAM WR 클럭신호
                      .o_pl_ram_add(w_pl_ram_add),   // RAM ADD 값
                      .o_ps_comp(w_ps_comp)   // 전체 카운트 동작 완료 신호, Python으로 전달
    );  
    
    async_counter#(.DATA_WIDTH(DATA_WIDTH_CNT))
    async_counter_inst(.i_pl_sig(i_pl_sig),
                       .i_pl_en(w_pl_cnt_en),
                       .i_pl_resetn(w_pl_cnt_resetn),
                       .o_pl_cnt(w_pl_cnt));
                       
    blk_mem_gen_0 blk_mem_gen_0_inst(
            // write port
            .addra(w_pl_ram_add),
            .clka(w_pl_ram_clk),
            .dina(w_pl_cnt),
            .wea(1'b1),
            // read port
            .addrb(w_ps_ram_add),
            .clkb(s00_axi_aclk),
            .doutb(w_ps_cnt));  
                                        
	// User logic ends

	endmodule
