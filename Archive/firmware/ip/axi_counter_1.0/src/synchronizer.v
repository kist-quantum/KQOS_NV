`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 11/30/2023 09:58:25 AM
// Design Name: 
// Module Name: synchronizer
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module synchronizer#(
    parameter integer DATA_WIDTH = 12,
    parameter integer RAM_DEPTH = 12,
    parameter IDLE=3'd0, DELAY=3'd1, GEN=3'd2, SAVE=3'd3
    /*
    IDLE: i_pl_trig 신호가 입력될 때까지 대기하는 상태
    DELAY: i_pl_trig 입력 후 i_ps_delay 동안 대기하는 상태
    GEN: i_ps_width 크기의 카운터 enable 신호(o_cnt_en)를 생성하는 상태
    SAVE: o_cnt_en 동안 측정된 카운트를 RAM에 저장하는 상태
    */
    )
    (
    /*
    Port 읽는 방법
    -블록1: i -> input 의미, o -> output 의미
    -블록2: 연결될 hierarchy 의미
    -블록3: 신호 이름
    */    
    input wire i_pl_clk,    // 레퍼런스 클럭, o_en 신호의 타이밍 resolution 결정
    input wire i_pl_trig,   // 트리거 신호, QICK lib.의 AveragerProgram.trigger() 함수로 발생된 트리거 신호
    input wire i_ps_resetn, // 리셋 신호, Python에서 전달 받은 리셋 신호
    input wire [DATA_WIDTH-1:0] i_ps_delay, // i_pl_trig 신호와 o_en 신호 간 딜레이, i_pl_trig 감지 후 i_ps_delay 후 o_en -> 'High' 
    input wire [DATA_WIDTH-1:0] i_ps_width, // o_en 신호의 펄스 폭
    input wire [RAM_DEPTH-1:0] i_ps_cnt_reps,   // 카운터 동작 횟수, readout 횟수
    output wire o_pl_cnt_en,   // 카운터 enable 신호, 카운터 모듈로 전달
    output wire o_pl_cnt_resetn,   // 카운터 resetn 신호, 카운터 모듈로 전달
    output wire o_pl_ram_clk,  // RAM WR 클럭신호
    output wire [RAM_DEPTH-1:0] o_pl_ram_add,   // RAM ADD 값
    output wire o_ps_comp   // 전체 카운트 동작 완료 신호, Python으로 전달
    );
    
    reg cnt_en; // 카운터 enable 신호, 카운터 모듈로 전달
    reg cnt_resetn; // 카운터 resetn 신호, 카운터 모듈로 전달    
    reg [DATA_WIDTH-1:0] cnt_delay; // delay 카운팅 변수
    reg [DATA_WIDTH-1:0] cnt_width; // width 카운팅 변수
    reg [RAM_DEPTH-1:0] cnt_reps; // reps 카운팅 변수
    
    reg trig, rstn_trig;
    reg [2:0] state;
    
    reg ram_clk;
    reg [RAM_DEPTH-1:0] ram_add;
    
    assign o_pl_cnt_en = cnt_en;
    assign o_pl_cnt_resetn = cnt_resetn;
    assign o_ps_comp = (cnt_reps >= i_ps_cnt_reps) ? 1'b1 : 1'b0;   // Python에서 설정된 cnt_reps 만큼 카운터 동작 후 comp 신호로 Python에게 동작 완료를 알림
    
    assign o_pl_ram_clk = ram_clk;
    assign o_pl_ram_add = ram_add;
    
    // i_pl_trig 신호 latch
    always @(posedge i_pl_trig or negedge rstn_trig) begin
        if(rstn_trig != 1'b1)   trig <= 1'b0;
        else                    trig <= 1'b1;
    end
    
    always @(posedge i_pl_clk or negedge i_ps_resetn) begin
        if(i_ps_resetn != 1'b1) begin
            state <= IDLE;
            
            rstn_trig <= 1'b0;
            
            cnt_en <= 1'b0;
            cnt_resetn <= 1'b0;
            
            ram_clk <= 1'b0;
            ram_add <= 0;
            
            cnt_delay <= 0;
            cnt_width <= 0;
            cnt_reps <= 0;
        end
        else begin
            case(state)
                IDLE: begin
                    if(trig != 1'b0) begin
                        state <= DELAY;
                        
                        rstn_trig <= 1'b0;
                        
                        cnt_en <= 1'b0;
                        cnt_resetn <= 1'b0;
                        
                        ram_clk <= 1'b0;
                        ram_add <= ram_add;
                        
                        cnt_delay <= 0;
                        cnt_width <= 0;
                        cnt_reps <= cnt_reps;                        
                    end
                    else begin
                        state <= IDLE;
                        
                        rstn_trig <= 1'b1;
                        
                        cnt_en <= 1'b0;
                        cnt_resetn <= 1'b0;
                        
                        ram_clk <= 1'b0;
                        ram_add <= ram_add;
                        
                        cnt_delay <= 0;
                        cnt_width <= 0;
                        cnt_reps <= cnt_reps;      
                    end
                end
                DELAY: begin
                    if(cnt_delay >= i_ps_delay-1) begin
                        state <= GEN;
                        
                        rstn_trig <= 1'b0;
                        
                        cnt_en <= 1'b1;
                        cnt_resetn <= 1'b1;
                        
                        ram_clk <= 1'b0;
                        ram_add <= ram_add;
                        
                        cnt_delay <= 0;
                        cnt_width <= 0;
                        cnt_reps <= cnt_reps;
                    end
                    else begin
                        state <= DELAY;
                        
                        rstn_trig <= 1'b0;
                        
                        cnt_en <= 1'b0;
                        cnt_resetn <= 1'b0;
                        
                        ram_clk <= 1'b0;
                        ram_add <= ram_add;
                        
                        cnt_delay <= cnt_delay + 1;
                        cnt_width <= 0;
                        cnt_reps <= cnt_reps;
                    end
                end
                GEN: begin
                    if(cnt_width >= i_ps_width-1) begin
                        state <= SAVE;
                        
                        rstn_trig <= 1'b0;
                        
                        cnt_en <= 1'b0;
                        cnt_resetn <= 1'b1;
                        
                        ram_clk <= 1'b1;
                        ram_add <= ram_add;
                        
                        cnt_delay <= 0;
                        cnt_width <= 0;
                        cnt_reps <= cnt_reps;
                    end
                    else begin
                        state <= GEN;
                        
                        rstn_trig <= 1'b0;
                        
                        cnt_en <= 1'b1;
                        cnt_resetn <= 1'b1;
                        
                        ram_clk <= 1'b0;
                        ram_add <= ram_add;
                        
                        cnt_delay <= 0;
                        cnt_width <= cnt_width + 1;
                        cnt_reps <= cnt_reps;
                    end
                end
                SAVE: begin
                    state <= IDLE;
                    
                    rstn_trig <= 1'b0;
                    
                    cnt_en <= 1'b0;
                    cnt_resetn <= 1'b1;
                    
                    ram_clk <= 1'b0;
                    ram_add <= ram_add + 1;
                    
                    cnt_delay <= 0;
                    cnt_width <= 0;
                    cnt_reps <= cnt_reps + 1;                    
                end                
                default: begin    
                    state <= IDLE;
                    
                    rstn_trig <= 1'b0;
                    
                    cnt_en <= 1'b0;
                    cnt_resetn <= 1'b1;
                    
                    ram_clk <= 1'b0;
                    ram_add <= ram_add;
                    
                    cnt_delay <= 0;
                    cnt_width <= 0;
                    cnt_reps <= cnt_reps;              
                end
            endcase
        end
    end    
    
endmodule
