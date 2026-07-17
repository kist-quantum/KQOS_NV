`timescale 1 ns / 1 ps

module axi_timetag_2ch_snapshot_v1_0 #(
    parameter integer C_S00_AXI_DATA_WIDTH = 32,
    parameter integer C_S00_AXI_ADDR_WIDTH = 8,
    parameter integer INPUT_WIDTH = 3,
    parameter integer BUFFER_ADDR_BITS = 15,
    parameter integer TICK_HZ = 384000000
) (
    input wire [INPUT_WIDTH-1:0] i_sig,

    (* X_INTERFACE_INFO = "xilinx.com:signal:clock:1.0 i_clk_ref CLK" *)
    (* X_INTERFACE_PARAMETER = "ASSOCIATED_RESET i_resetn_ref" *)
    input wire i_clk_ref,
    (* X_INTERFACE_INFO = "xilinx.com:signal:reset:1.0 i_resetn_ref RST" *)
    (* X_INTERFACE_PARAMETER = "POLARITY ACTIVE_LOW" *)
    input wire i_resetn_ref,

    (* X_INTERFACE_INFO = "xilinx.com:signal:clock:1.0 s00_axi_aclk CLK" *)
    (* X_INTERFACE_PARAMETER = "ASSOCIATED_BUSIF S00_AXI, ASSOCIATED_RESET s00_axi_aresetn" *)
    input wire s00_axi_aclk,
    (* X_INTERFACE_INFO = "xilinx.com:signal:reset:1.0 s00_axi_aresetn RST" *)
    (* X_INTERFACE_PARAMETER = "POLARITY ACTIVE_LOW" *)
    input wire s00_axi_aresetn,

    (* X_INTERFACE_INFO = "xilinx.com:interface:aximm:1.0 S00_AXI AWADDR" *)
    input wire [C_S00_AXI_ADDR_WIDTH-1:0] s00_axi_awaddr,
    (* X_INTERFACE_INFO = "xilinx.com:interface:aximm:1.0 S00_AXI AWPROT" *)
    input wire [2:0] s00_axi_awprot,
    (* X_INTERFACE_INFO = "xilinx.com:interface:aximm:1.0 S00_AXI AWVALID" *)
    input wire s00_axi_awvalid,
    (* X_INTERFACE_INFO = "xilinx.com:interface:aximm:1.0 S00_AXI AWREADY" *)
    output wire s00_axi_awready,
    (* X_INTERFACE_INFO = "xilinx.com:interface:aximm:1.0 S00_AXI WDATA" *)
    input wire [C_S00_AXI_DATA_WIDTH-1:0] s00_axi_wdata,
    (* X_INTERFACE_INFO = "xilinx.com:interface:aximm:1.0 S00_AXI WSTRB" *)
    input wire [(C_S00_AXI_DATA_WIDTH/8)-1:0] s00_axi_wstrb,
    (* X_INTERFACE_INFO = "xilinx.com:interface:aximm:1.0 S00_AXI WVALID" *)
    input wire s00_axi_wvalid,
    (* X_INTERFACE_INFO = "xilinx.com:interface:aximm:1.0 S00_AXI WREADY" *)
    output wire s00_axi_wready,
    (* X_INTERFACE_INFO = "xilinx.com:interface:aximm:1.0 S00_AXI BRESP" *)
    output wire [1:0] s00_axi_bresp,
    (* X_INTERFACE_INFO = "xilinx.com:interface:aximm:1.0 S00_AXI BVALID" *)
    output wire s00_axi_bvalid,
    (* X_INTERFACE_INFO = "xilinx.com:interface:aximm:1.0 S00_AXI BREADY" *)
    input wire s00_axi_bready,
    (* X_INTERFACE_INFO = "xilinx.com:interface:aximm:1.0 S00_AXI ARADDR" *)
    input wire [C_S00_AXI_ADDR_WIDTH-1:0] s00_axi_araddr,
    (* X_INTERFACE_INFO = "xilinx.com:interface:aximm:1.0 S00_AXI ARPROT" *)
    input wire [2:0] s00_axi_arprot,
    (* X_INTERFACE_INFO = "xilinx.com:interface:aximm:1.0 S00_AXI ARVALID" *)
    input wire s00_axi_arvalid,
    (* X_INTERFACE_INFO = "xilinx.com:interface:aximm:1.0 S00_AXI ARREADY" *)
    output wire s00_axi_arready,
    (* X_INTERFACE_INFO = "xilinx.com:interface:aximm:1.0 S00_AXI RDATA" *)
    output wire [C_S00_AXI_DATA_WIDTH-1:0] s00_axi_rdata,
    (* X_INTERFACE_INFO = "xilinx.com:interface:aximm:1.0 S00_AXI RRESP" *)
    output wire [1:0] s00_axi_rresp,
    (* X_INTERFACE_INFO = "xilinx.com:interface:aximm:1.0 S00_AXI RVALID" *)
    output wire s00_axi_rvalid,
    (* X_INTERFACE_INFO = "xilinx.com:interface:aximm:1.0 S00_AXI RREADY" *)
    input wire s00_axi_rready
);

    localparam integer BUFFER_DEPTH = (1 << BUFFER_ADDR_BITS);
    localparam integer EVENT_WIDTH = 36;
    localparam [BUFFER_ADDR_BITS:0] BUFFER_DEPTH_COUNT = {1'b1, {BUFFER_ADDR_BITS{1'b0}}};
    localparam [31:0] VERSION = 32'h54544731; // "TTG1"

    localparam integer ADDR_LSB = 2;
    localparam integer REG_ADDR_BITS = 6;
    localparam [REG_ADDR_BITS-1:0] REG_CONTROL       = 6'h00; // 0x00
    localparam [REG_ADDR_BITS-1:0] REG_STATUS        = 6'h01; // 0x04
    localparam [REG_ADDR_BITS-1:0] REG_EVENT_COUNT   = 6'h02; // 0x08
    localparam [REG_ADDR_BITS-1:0] REG_TOTAL_COUNT   = 6'h03; // 0x0c
    localparam [REG_ADDR_BITS-1:0] REG_OVERFLOW_CNT  = 6'h04; // 0x10
    localparam [REG_ADDR_BITS-1:0] REG_WRITE_PTR     = 6'h05; // 0x14
    localparam [REG_ADDR_BITS-1:0] REG_CAPTURE_LIMIT = 6'h06; // 0x18
    localparam [REG_ADDR_BITS-1:0] REG_READ_INDEX    = 6'h07; // 0x1c
    localparam [REG_ADDR_BITS-1:0] REG_EVENT_LO      = 6'h08; // 0x20
    localparam [REG_ADDR_BITS-1:0] REG_EVENT_HI      = 6'h09; // 0x24
    localparam [REG_ADDR_BITS-1:0] REG_TIME_NOW      = 6'h0a; // 0x28
    localparam [REG_ADDR_BITS-1:0] REG_CH_SELECT     = 6'h0b; // 0x2c
    localparam [REG_ADDR_BITS-1:0] REG_VERSION       = 6'h0c; // 0x30
    localparam [REG_ADDR_BITS-1:0] REG_DEPTH         = 6'h0d; // 0x34
    localparam [REG_ADDR_BITS-1:0] REG_TICK_HZ       = 6'h0e; // 0x38
    localparam [REG_ADDR_BITS-1:0] REG_EVENT_WIDTH   = 6'h0f; // 0x3c

    function [31:0] apply_wstrb32;
        input [31:0] old_value;
        input [31:0] new_value;
        input [3:0] wstrb;
        integer i;
        begin
            apply_wstrb32 = old_value;
            for (i = 0; i < 4; i = i + 1) begin
                if (wstrb[i]) begin
                    apply_wstrb32[(i*8) +: 8] = new_value[(i*8) +: 8];
                end
            end
        end
    endfunction

    function select_input;
        input [INPUT_WIDTH-1:0] value;
        input [1:0] sel;
        begin
            case (sel)
                2'd0: select_input = value[0];
                2'd1: select_input = value[1];
                2'd2: select_input = value[2];
                default: select_input = 1'b0;
            endcase
        end
    endfunction

    (* ram_style = "block" *) reg [EVENT_WIDTH-1:0] event_mem [0:BUFFER_DEPTH-1];

    reg axi_awready;
    reg axi_wready;
    reg [1:0] axi_bresp;
    reg axi_bvalid;
    reg axi_arready;
    reg [31:0] axi_rdata;
    reg [1:0] axi_rresp;
    reg axi_rvalid;

    assign s00_axi_awready = axi_awready;
    assign s00_axi_wready  = axi_wready;
    assign s00_axi_bresp   = axi_bresp;
    assign s00_axi_bvalid  = axi_bvalid;
    assign s00_axi_arready = axi_arready;
    assign s00_axi_rdata   = axi_rdata;
    assign s00_axi_rresp   = axi_rresp;
    assign s00_axi_rvalid  = axi_rvalid;

    reg [31:0] control_reg;
    reg [31:0] capture_limit_reg;
    reg [31:0] read_index_reg;
    reg [31:0] channel_select_reg;
    reg cmd_clear_toggle;
    reg cmd_reset_ts_toggle;

    wire [REG_ADDR_BITS-1:0] awaddr_word = s00_axi_awaddr[ADDR_LSB+REG_ADDR_BITS-1:ADDR_LSB];
    wire [REG_ADDR_BITS-1:0] araddr_word = s00_axi_araddr[ADDR_LSB+REG_ADDR_BITS-1:ADDR_LSB];
    wire [31:0] control_wdata = apply_wstrb32(control_reg, s00_axi_wdata, s00_axi_wstrb);
    wire [31:0] capture_limit_wdata = apply_wstrb32(capture_limit_reg, s00_axi_wdata, s00_axi_wstrb);
    wire [31:0] read_index_wdata = apply_wstrb32(read_index_reg, s00_axi_wdata, s00_axi_wstrb);
    wire [31:0] channel_select_wdata = apply_wstrb32(channel_select_reg, s00_axi_wdata, s00_axi_wstrb);

    reg [BUFFER_ADDR_BITS-1:0] rd_addr;
    reg [EVENT_WIDTH-1:0] rd_data;

    reg [31:0] status_axi_s0, status_axi_s1;
    reg [31:0] event_count_axi_s0, event_count_axi_s1;
    reg [31:0] total_count_axi_s0, total_count_axi_s1;
    reg [31:0] overflow_count_axi_s0, overflow_count_axi_s1;
    reg [31:0] write_ptr_axi_s0, write_ptr_axi_s1;
    reg [31:0] timestamp_axi_s0, timestamp_axi_s1;

    reg [31:0] reg_read_data;
    always @(*) begin
        case (araddr_word)
            REG_CONTROL:       reg_read_data = control_reg & 32'h00000039;
            REG_STATUS:        reg_read_data = status_axi_s1;
            REG_EVENT_COUNT:   reg_read_data = event_count_axi_s1;
            REG_TOTAL_COUNT:   reg_read_data = total_count_axi_s1;
            REG_OVERFLOW_CNT:  reg_read_data = overflow_count_axi_s1;
            REG_WRITE_PTR:     reg_read_data = write_ptr_axi_s1;
            REG_CAPTURE_LIMIT: reg_read_data = capture_limit_reg;
            REG_READ_INDEX:    reg_read_data = read_index_reg;
            REG_EVENT_LO:      reg_read_data = rd_data[31:0];
            REG_EVENT_HI:      reg_read_data = {28'd0, rd_data[35:32]};
            REG_TIME_NOW:      reg_read_data = timestamp_axi_s1;
            REG_CH_SELECT:     reg_read_data = channel_select_reg;
            REG_VERSION:       reg_read_data = VERSION;
            REG_DEPTH:         reg_read_data = BUFFER_DEPTH;
            REG_TICK_HZ:       reg_read_data = TICK_HZ;
            REG_EVENT_WIDTH:   reg_read_data = EVENT_WIDTH;
            default:           reg_read_data = 32'd0;
        endcase
    end

    always @(posedge s00_axi_aclk) begin
        if (!s00_axi_aresetn) begin
            axi_awready <= 1'b0;
            axi_wready <= 1'b0;
            axi_bresp <= 2'b00;
            axi_bvalid <= 1'b0;
            axi_arready <= 1'b0;
            axi_rdata <= 32'd0;
            axi_rresp <= 2'b00;
            axi_rvalid <= 1'b0;
            control_reg <= 32'h00000030; // stop_on_full + read auto-increment
            capture_limit_reg <= BUFFER_DEPTH;
            read_index_reg <= 32'd0;
            channel_select_reg <= 32'h00000001; // ref=i_sig[1], sig=i_sig[0]
            cmd_clear_toggle <= 1'b0;
            cmd_reset_ts_toggle <= 1'b0;
        end else begin
            axi_awready <= 1'b0;
            axi_wready <= 1'b0;
            axi_arready <= 1'b0;

            if (axi_bvalid && s00_axi_bready) begin
                axi_bvalid <= 1'b0;
            end

            if (axi_rvalid && s00_axi_rready) begin
                axi_rvalid <= 1'b0;
            end

            if (!axi_bvalid && s00_axi_awvalid && s00_axi_wvalid) begin
                axi_awready <= 1'b1;
                axi_wready <= 1'b1;
                axi_bvalid <= 1'b1;
                axi_bresp <= 2'b00;

                case (awaddr_word)
                    REG_CONTROL: begin
                        control_reg[0] <= control_wdata[0];
                        control_reg[3] <= control_wdata[3];
                        control_reg[4] <= control_wdata[4];
                        control_reg[5] <= control_wdata[5];
                        if (control_wdata[1]) begin
                            cmd_clear_toggle <= ~cmd_clear_toggle;
                        end
                        if (control_wdata[2]) begin
                            cmd_reset_ts_toggle <= ~cmd_reset_ts_toggle;
                        end
                    end
                    REG_CAPTURE_LIMIT: begin
                        capture_limit_reg <= capture_limit_wdata;
                    end
                    REG_READ_INDEX: begin
                        read_index_reg <= read_index_wdata;
                    end
                    REG_CH_SELECT: begin
                        channel_select_reg <= channel_select_wdata;
                    end
                    default: begin
                    end
                endcase
            end

            if (!axi_rvalid && s00_axi_arvalid) begin
                axi_arready <= 1'b1;
                axi_rvalid <= 1'b1;
                axi_rresp <= 2'b00;
                axi_rdata <= reg_read_data;

                if ((araddr_word == REG_EVENT_HI) && control_reg[5]) begin
                    read_index_reg <= read_index_reg + 1'b1;
                end
            end
        end
    end

    always @(posedge s00_axi_aclk) begin
        if (!s00_axi_aresetn) begin
            rd_addr <= {BUFFER_ADDR_BITS{1'b0}};
            rd_data <= {EVENT_WIDTH{1'b0}};
        end else begin
            if (read_index_reg >= BUFFER_DEPTH) begin
                rd_addr <= {BUFFER_ADDR_BITS{1'b0}};
            end else begin
                rd_addr <= read_index_reg[BUFFER_ADDR_BITS-1:0];
            end
            rd_data <= event_mem[rd_addr];
        end
    end

    reg enable_ref_s0, enable_ref;
    reg circular_ref_s0, circular_ref;
    reg stop_on_full_ref_s0, stop_on_full_ref;
    reg [1:0] ref_sel_ref_s0, ref_sel_ref;
    reg [1:0] sig_sel_ref_s0, sig_sel_ref;
    reg [31:0] capture_limit_ref_s0, capture_limit_ref;

    (* ASYNC_REG = "TRUE" *) reg [2:0] clear_toggle_ref_sync;
    (* ASYNC_REG = "TRUE" *) reg [2:0] reset_ts_toggle_ref_sync;
    (* ASYNC_REG = "TRUE" *) reg [INPUT_WIDTH-1:0] sig_meta;
    (* ASYNC_REG = "TRUE" *) reg [INPUT_WIDTH-1:0] sig_sync;
    reg [INPUT_WIDTH-1:0] sig_sync_d;

    reg [31:0] timestamp_ref;
    reg [BUFFER_ADDR_BITS-1:0] write_ptr_ref;
    reg [BUFFER_ADDR_BITS:0] event_count_ref;
    reg [31:0] total_count_ref;
    reg [31:0] overflow_count_ref;
    reg full_ref;
    reg overflow_ref;
    reg wrapped_ref;
    reg done_ref;

    wire clear_req_ref = clear_toggle_ref_sync[2] ^ clear_toggle_ref_sync[1];
    wire reset_ts_req_ref = reset_ts_toggle_ref_sync[2] ^ reset_ts_toggle_ref_sync[1];
    wire [BUFFER_ADDR_BITS:0] capture_limit_eff =
        ((capture_limit_ref == 32'd0) || (capture_limit_ref > BUFFER_DEPTH)) ?
        BUFFER_DEPTH_COUNT : capture_limit_ref[BUFFER_ADDR_BITS:0];
    wire [BUFFER_ADDR_BITS-1:0] limit_last_addr = capture_limit_eff[BUFFER_ADDR_BITS-1:0] - 1'b1;
    wire [INPUT_WIDTH-1:0] sig_edge = sig_sync & ~sig_sync_d;
    wire ref_edge = select_input(sig_edge, ref_sel_ref);
    wire sig_edge_sel = select_input(sig_edge, sig_sel_ref);
    wire [1:0] event_mask = {sig_edge_sel, ref_edge};
    wire event_seen = |event_mask;
    wire [31:0] status_ref_bus = {
        24'd0,
        stop_on_full_ref,
        circular_ref,
        (!full_ref) | circular_ref,
        done_ref,
        wrapped_ref,
        overflow_ref,
        full_ref,
        enable_ref
    };

    always @(posedge i_clk_ref) begin
        if (!i_resetn_ref) begin
            enable_ref_s0 <= 1'b0;
            enable_ref <= 1'b0;
            circular_ref_s0 <= 1'b0;
            circular_ref <= 1'b0;
            stop_on_full_ref_s0 <= 1'b1;
            stop_on_full_ref <= 1'b1;
            ref_sel_ref_s0 <= 2'd1;
            ref_sel_ref <= 2'd1;
            sig_sel_ref_s0 <= 2'd0;
            sig_sel_ref <= 2'd0;
            capture_limit_ref_s0 <= BUFFER_DEPTH;
            capture_limit_ref <= BUFFER_DEPTH;
            clear_toggle_ref_sync <= 3'b000;
            reset_ts_toggle_ref_sync <= 3'b000;
            sig_meta <= {INPUT_WIDTH{1'b0}};
            sig_sync <= {INPUT_WIDTH{1'b0}};
            sig_sync_d <= {INPUT_WIDTH{1'b0}};
            timestamp_ref <= 32'd0;
            write_ptr_ref <= {BUFFER_ADDR_BITS{1'b0}};
            event_count_ref <= {BUFFER_ADDR_BITS+1{1'b0}};
            total_count_ref <= 32'd0;
            overflow_count_ref <= 32'd0;
            full_ref <= 1'b0;
            overflow_ref <= 1'b0;
            wrapped_ref <= 1'b0;
            done_ref <= 1'b0;
        end else begin
            enable_ref_s0 <= control_reg[0];
            enable_ref <= enable_ref_s0;
            circular_ref_s0 <= control_reg[3];
            circular_ref <= circular_ref_s0;
            stop_on_full_ref_s0 <= control_reg[4];
            stop_on_full_ref <= stop_on_full_ref_s0;
            ref_sel_ref_s0 <= channel_select_reg[1:0];
            ref_sel_ref <= ref_sel_ref_s0;
            sig_sel_ref_s0 <= channel_select_reg[5:4];
            sig_sel_ref <= sig_sel_ref_s0;
            capture_limit_ref_s0 <= capture_limit_reg;
            capture_limit_ref <= capture_limit_ref_s0;
            clear_toggle_ref_sync <= {clear_toggle_ref_sync[1:0], cmd_clear_toggle};
            reset_ts_toggle_ref_sync <= {reset_ts_toggle_ref_sync[1:0], cmd_reset_ts_toggle};
            sig_meta <= i_sig;
            sig_sync <= sig_meta;
            sig_sync_d <= sig_sync;

            if (reset_ts_req_ref) begin
                timestamp_ref <= 32'd0;
            end else begin
                timestamp_ref <= timestamp_ref + 1'b1;
            end

            if (clear_req_ref) begin
                write_ptr_ref <= {BUFFER_ADDR_BITS{1'b0}};
                event_count_ref <= {BUFFER_ADDR_BITS+1{1'b0}};
                total_count_ref <= 32'd0;
                overflow_count_ref <= 32'd0;
                full_ref <= 1'b0;
                overflow_ref <= 1'b0;
                wrapped_ref <= 1'b0;
                done_ref <= 1'b0;
            end else if (event_seen && enable_ref) begin
                if (circular_ref) begin
                    event_mem[write_ptr_ref] <= {2'b00, event_mask, timestamp_ref};
                    total_count_ref <= total_count_ref + 1'b1;
                    if (event_count_ref < capture_limit_eff) begin
                        event_count_ref <= event_count_ref + 1'b1;
                    end else begin
                        full_ref <= 1'b1;
                    end
                    if ((event_count_ref + 1'b1) >= capture_limit_eff) begin
                        full_ref <= 1'b1;
                    end
                    if (write_ptr_ref == limit_last_addr) begin
                        write_ptr_ref <= {BUFFER_ADDR_BITS{1'b0}};
                        wrapped_ref <= 1'b1;
                    end else begin
                        write_ptr_ref <= write_ptr_ref + 1'b1;
                    end
                end else if (!full_ref) begin
                    event_mem[write_ptr_ref] <= {2'b00, event_mask, timestamp_ref};
                    total_count_ref <= total_count_ref + 1'b1;
                    event_count_ref <= event_count_ref + 1'b1;
                    if (write_ptr_ref == limit_last_addr) begin
                        write_ptr_ref <= {BUFFER_ADDR_BITS{1'b0}};
                    end else begin
                        write_ptr_ref <= write_ptr_ref + 1'b1;
                    end
                    if ((event_count_ref + 1'b1) >= capture_limit_eff) begin
                        full_ref <= 1'b1;
                        if (stop_on_full_ref) begin
                            done_ref <= 1'b1;
                        end
                    end
                end else begin
                    full_ref <= 1'b1;
                    overflow_ref <= 1'b1;
                    overflow_count_ref <= overflow_count_ref + 1'b1;
                    if (stop_on_full_ref) begin
                        done_ref <= 1'b1;
                    end
                end
            end
        end
    end

    always @(posedge s00_axi_aclk) begin
        if (!s00_axi_aresetn) begin
            status_axi_s0 <= 32'd0;
            status_axi_s1 <= 32'd0;
            event_count_axi_s0 <= 32'd0;
            event_count_axi_s1 <= 32'd0;
            total_count_axi_s0 <= 32'd0;
            total_count_axi_s1 <= 32'd0;
            overflow_count_axi_s0 <= 32'd0;
            overflow_count_axi_s1 <= 32'd0;
            write_ptr_axi_s0 <= 32'd0;
            write_ptr_axi_s1 <= 32'd0;
            timestamp_axi_s0 <= 32'd0;
            timestamp_axi_s1 <= 32'd0;
        end else begin
            status_axi_s0 <= status_ref_bus;
            status_axi_s1 <= status_axi_s0;
            event_count_axi_s0 <= {{(31-BUFFER_ADDR_BITS){1'b0}}, event_count_ref};
            event_count_axi_s1 <= event_count_axi_s0;
            total_count_axi_s0 <= total_count_ref;
            total_count_axi_s1 <= total_count_axi_s0;
            overflow_count_axi_s0 <= overflow_count_ref;
            overflow_count_axi_s1 <= overflow_count_axi_s0;
            write_ptr_axi_s0 <= {{(32-BUFFER_ADDR_BITS){1'b0}}, write_ptr_ref};
            write_ptr_axi_s1 <= write_ptr_axi_s0;
            timestamp_axi_s0 <= timestamp_ref;
            timestamp_axi_s1 <= timestamp_axi_s0;
        end
    end

endmodule
