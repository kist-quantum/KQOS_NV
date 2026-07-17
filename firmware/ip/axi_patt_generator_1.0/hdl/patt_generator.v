`timescale 1ns / 1ps

module patt_generator (
    input i_clk_ref,
    input i_resetn,
    input i_trig,
    input [15:0] i_ram_data,
    output [16:0] o_ram_add,
    output o_pattern
);

    parameter IDLE = 4'b0001;
    parameter WAIT = 4'b0010;
    parameter ON = 4'b0100;
    parameter OFF = 4'b1000;

    reg [15:0] cnt_patt;
    reg [16:0] ram_add;
    reg [7:0] cnt_clk;
    reg [3:0] ps, ns;
    reg trig_meta, trig_sync, trig_sync_d;

    wire trig_rise = trig_sync & ~trig_sync_d;
    wire wait_done = (cnt_clk >= 8'd15 - 1'b1);
    wire on_done = (cnt_clk >= 8'd10 - 1'b1);
    wire off_done = (cnt_clk >= 8'd70 - 1'b1);

    assign o_pattern = (ps == ON);
    assign o_ram_add = ram_add;

    always @* begin
        ns = IDLE;
        case (ps)
            IDLE:    ns = trig_rise ? WAIT : IDLE;
            WAIT:    ns = (!i_ram_data) ? IDLE : (wait_done ? ON : WAIT);
            ON:      ns = on_done ? OFF : ON;
            OFF:     ns = (cnt_patt >= i_ram_data) ? IDLE : (off_done ? ON : OFF);
            default: ns = IDLE;
        endcase
    end

    always @(posedge i_clk_ref or negedge i_resetn) begin
        if (!i_resetn) begin
            trig_meta <= 1'b0;
            trig_sync <= 1'b0;
            trig_sync_d <= 1'b0;
            ps <= IDLE;
            cnt_clk <= 8'd0;
            cnt_patt <= 16'd0;
            ram_add <= 17'd0;
        end else begin
            trig_meta <= i_trig;
            trig_sync <= trig_meta;
            trig_sync_d <= trig_sync;
            ps <= ns;

            if (ps != ns) begin
                cnt_clk <= 8'd0;
                if (ns == IDLE) begin
                    ram_add <= ram_add + 1'b1;
                    cnt_patt <= 16'd0;
                end else if (ns == ON) begin
                    cnt_patt <= cnt_patt + 1'b1;
                end
            end else begin
                cnt_clk <= cnt_clk + 1'b1;
            end
        end
    end

endmodule
