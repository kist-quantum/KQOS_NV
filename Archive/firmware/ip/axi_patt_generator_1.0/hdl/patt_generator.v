`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 01/10/2024 04:30:58 PM
// Design Name: 
// Module Name: patt_generator
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


module patt_generator(
    input i_clk_ref,
    input i_resetn,
    input i_trig,
    input [15:0] i_ram_data,
    output [16:0] o_ram_add,
    output o_pattern
    );
    parameter IDLE = 4'b0001, WAIT = 4'b0010, ON = 4'b0100, OFF = 4'b1000;
    reg [15:0] cnt_patt;
    reg [16:0] ram_add;
    reg [7:0] cnt_clk;
    reg [3:0] ps, ns;   // ps:present state, ns:next state    
    reg trig;
    
    //State Register
    always @(posedge i_clk_ref or negedge i_resetn)
        if(!i_resetn)   ps <= IDLE;
        else            ps <= ns;    
    
    //Next State Logic
    always @(ps or trig or cnt_clk) begin
        ns = IDLE;
        case(ps)
            IDLE:   if(trig)                        ns = WAIT;
                    else                            ns = IDLE;
            WAIT:   if(!i_ram_data)                 ns = IDLE;
                    else if(cnt_clk >= 8'd15 - 1)   ns = ON;
                    else                            ns = WAIT;
            ON:     if(cnt_clk >= 8'd10 - 1)        ns = OFF;
                    else                            ns = ON;
            OFF:    if(cnt_patt >= i_ram_data)      ns = IDLE;
                    else if(cnt_clk >= 8'd70 - 1)   ns = ON;
                    else                            ns = OFF;
        endcase
    end
    
    //trig latch
    //IDLE->WAIT: trig 리셋
    always @(posedge i_trig or posedge ps[1]) begin
        if(ps[1])   trig <= 1'b0;
        else        trig <= 1'b1;
    end
    
    //i_clk_ref counter
    //i_resetn 또는 ps!=ns 인 경우 cnt_clk 리셋
    always @(posedge i_clk_ref) begin
        if(ps != ns)    cnt_clk <= 8'd0;
        else            cnt_clk <= cnt_clk + 8'd1;
    end    
    
    //ram_add counter
    //WAIT->IDLE or OFF->IDLE: ram_add 1증가
    always @(posedge ps[0] or negedge i_resetn) begin
        if(!i_resetn)   ram_add <= 16'd0;
        else            ram_add <= ram_add + 16'd1;
    end
    
    //pattern counter
    //WAIT(OFF)->IDLE: cnt_patt 리셋
    //WAIT(OFF)->ON: cnt_patt 1증가
    always @(posedge ps[0] or posedge ps[2]) begin
        if(ps[0])   cnt_patt <= 16'd0;
        else        cnt_patt <= cnt_patt + 16'd1;            
    end
    
    //Output Logic
    assign o_pattern = (ps == ON);
    assign o_ram_add = ram_add;
    
endmodule