`timescale 1ns / 1ps
// sig_gen v2: down-counter + MSB underflow detection
// Replaces 32-bit comparator (4-5 LUT levels) with single-bit MSB check.
// Timing-equivalent behavior: same latency for i_delay/i_width >= 1.
// o_comp registered 1 cycle (acceptable for pulse generation).

module sig_gen #(
    parameter integer DATA_WIDTH = 32,
    parameter IDLE = 3'b001,
    parameter WAIT = 3'b010,
    parameter EN = 3'b100
) (
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

    reg trig_meta, trig_sync, trig_sync_d;
    reg [2:0] ps, ns;
    reg [DATA_WIDTH-1:0] cnt_reps;
    // Down-counter: loaded with (target - 2) on state entry.
    // MSB becomes 1 on underflow (2's complement), replacing the comparator.
    reg [DATA_WIDTH-1:0] cnt_down;
    reg comp_r;

    wire trig_rise  = trig_sync & ~trig_sync_d;
    // Single-bit underflow detect — no wide comparator on critical path
    wire delay_done = cnt_down[DATA_WIDTH-1];
    wire width_done = cnt_down[DATA_WIDTH-1];

    assign o_cnt_reps = cnt_reps;
    assign o_ps  = ps;
    assign o_ns  = ns;
    assign o_trig = trig_sync;
    assign o_en  = ps[2];
    // comp_r is registered one cycle: avoids 32-bit comparator on FSM input
    assign o_comp = comp_r;

    always @* begin
        ns = IDLE;
        case (ps)
            IDLE:    ns = (trig_rise && !comp_r) ? WAIT : IDLE;
            WAIT:    ns = delay_done ? EN : WAIT;
            EN:      ns = width_done ? IDLE : EN;
            default: ns = IDLE;
        endcase
    end

    always @(posedge i_clk_ref or negedge i_resetn) begin
        if (!i_resetn) begin
            trig_meta  <= 1'b0;
            trig_sync  <= 1'b0;
            trig_sync_d<= 1'b0;
            ps         <= IDLE;
            cnt_down   <= {DATA_WIDTH{1'b0}};
            cnt_reps   <= {DATA_WIDTH{1'b0}};
            comp_r     <= 1'b0;
        end else begin
            trig_meta   <= i_trig;
            trig_sync   <= trig_meta;
            trig_sync_d <= trig_sync;
            ps          <= ns;

            // Update registered completion flag each cycle
            comp_r <= (cnt_reps >= i_reps);

            if (ps != ns) begin
                // Load down-counter: (target - 2) so MSB underflows after
                // exactly (target) cycles in the new state.
                case (ns)
                    WAIT:    cnt_down <= i_delay - 2;
                    EN:      cnt_down <= i_width - 2;
                    default: cnt_down <= {DATA_WIDTH{1'b0}};
                endcase
                // Increment rep count on EN→IDLE transition
                if (ps == EN && ns == IDLE)
                    cnt_reps <= cnt_reps + 1'b1;
            end else begin
                cnt_down <= cnt_down - 1'b1;
            end
        end
    end

endmodule
