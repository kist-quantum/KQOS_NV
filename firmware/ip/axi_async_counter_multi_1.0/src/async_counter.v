`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2023/03/30 14:08:34
// Design Name: 
// Module Name: async_counter
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


module async_counter#(
    parameter integer DATA_WIDTH = 12
    )
    (
    input wire i_pl_sig,
    input wire i_pl_en,
    input wire i_pl_resetn,
    output wire [DATA_WIDTH-1:0] o_pl_cnt
    );
      
    reg [DATA_WIDTH-1:0] cnt;  
    assign o_pl_cnt = cnt;
    
    always @(posedge i_pl_sig or negedge i_pl_resetn) begin
        if(i_pl_resetn != 1'b1)    cnt <= 0;
//        else if(i_pl_en != 1'b0)   cnt <= cnt + 1;
        else                       cnt <= cnt + i_pl_en;
    end    
endmodule