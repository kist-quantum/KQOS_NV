`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 06/02/2023 05:42:35 PM
// Design Name: 
// Module Name: sig_gen
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


module sig_gen#(
    parameter integer DATA_WIDTH = 32,
    parameter IDLE=3'b001, WAIT=3'b010, EN=3'b100
    )
    (
    input i_clk_ref,
    input i_trig,
    input i_resetn,
    input [DATA_WIDTH-1:0] i_delay,
    input [DATA_WIDTH-1:0] i_width,
    input [DATA_WIDTH-1:0] i_reps,
    output o_en,
    output o_comp,
    
    output [DATA_WIDTH-1:0] o_cnt_reps,
    output [2:0] o_ps,
    output [2:0] o_ns,
    output o_trig
    );
    
    reg trig;
    reg [2:0] ps, ns; //ps: present state, ns: next state
    reg [DATA_WIDTH-1:0] cnt_reps, cnt_clk;
    
    //Debug
    assign o_cnt_reps = cnt_reps;
    assign o_ps = ps;
    assign o_ns = ns;
    assign o_trig = trig;

    //State Register
    always @(posedge i_clk_ref or negedge i_resetn)
        if(!i_resetn)   ps <= IDLE;
        else            ps <= ns;
    
    //trig latch
    //IDLE->WAIT: trig 리셋
    //o_comp '0'일 경우만 trig '1' 셋
    always @(posedge i_trig or posedge ps[1]) begin
        if(ps[1])   trig <= 1'b0;
        else        trig <= !o_comp;
    end    
    
    //Next State Logic
    always @(ps or trig or cnt_clk) begin
        ns = IDLE;
        case(ps)
            IDLE:   if(trig)                        ns = WAIT;
                    else                            ns = IDLE;
            WAIT:   if(cnt_clk >= i_delay-1)        ns = EN;
                    else                            ns = WAIT;
            EN:     if(cnt_clk >= i_width-1)        ns = IDLE;
                    else                            ns = EN;
        endcase
    end          
    
    //i_clk_ref counter
    //ps!=ns 인 경우 cnt_clk 리셋
    always @(posedge i_clk_ref) begin
        if(ps != ns)    cnt_clk <= 32'd0;
        else            cnt_clk <= cnt_clk + 32'd1;
    end       
    
    //cnt_reps counter
    always @(posedge ps[0] or negedge i_resetn) begin
        if(!i_resetn)   cnt_reps <= 32'd0;
        else            cnt_reps <= cnt_reps + 32'd1;            
    end     
    
    //Output Logic
    assign o_en = ps[2];   
    assign o_comp = (cnt_reps >= i_reps); 
endmodule
