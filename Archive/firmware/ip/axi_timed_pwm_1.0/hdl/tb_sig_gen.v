`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 06/02/2023 06:03:47 PM
// Design Name: 
// Module Name: tb_sig_gen
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


module tb_sig_gen(
    );
    
    reg CLK, TRIG, RSTN;
    reg [31:0] DELAY, WIDTH;
    wire SIG, COMP;
    reg [31:0] forcnt;
    
    initial begin
        CLK = 1'b0;     // 1-bit input clock
        forever #2.5 CLK = ~CLK;
    end
    
    initial begin
        #50
        TRIG = 0;
        RSTN = 1;
        DELAY = 20;
        WIDTH = 10;
        #10
        RSTN = 0;
        #10
        RSTN = 1;
        #10
        TRIG = 1;
        #10
        TRIG = 0;
        for (forcnt=0;forcnt<5;forcnt=forcnt+1)begin
            #200
            TRIG = 1;
            #10
            TRIG = 0;
        end      
        
        #10
        RSTN = 0;
        #10
        RSTN = 1;
        for (forcnt=0;forcnt<5;forcnt=forcnt+1)begin
            #200
            TRIG = 1;
            #10
            TRIG = 0;
        end  
    end
    
    sig_gen#(.DATA_WIDTH(32))
    sig_gen_inst(.i_clk(CLK),
            .i_trig(TRIG),
            .i_resetn(RSTN),
            .i_delay(DELAY),
            .i_width(WIDTH),
            .i_cnt_trig(5),
            .o_sig(SIG),
            .o_comp(COMP));
endmodule
