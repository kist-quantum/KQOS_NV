from address_v6 import TTAG_DEFAULT_CAPTURE_LIMIT
from timetag_2ch import acquire_g2


def g2(soc, cfg):
    """Run a 2-channel HBT/g2 capture with the FPGA time tagger.

    The `soc` argument is accepted to match the KQOS command handler pattern.
    The first implementation is a free-running TCSPC capture; QICK pulse
    program synchronized captures can be added later as a separate mode.
    """
    mode = cfg.get("mode", "free_run")
    if mode != "free_run":
        raise ValueError(f"Unsupported g2 mode: {mode!r}. Use mode='free_run'.")

    return acquire_g2(
        capture_ms=cfg.get("capture_ms", 100),
        capture_limit=cfg.get("capture_limit", TTAG_DEFAULT_CAPTURE_LIMIT),
        # Main g2 pair:
        #   ref    = PMOD1_7_LS_SPD3 / i_sig[2]
        #   signal = PMOD1_2_LS_SPD2 / i_sig[0]
        ref_ch=cfg.get("ref_ch", 2),
        sig_ch=cfg.get("sig_ch", 0),
        window_ticks=cfg.get("window_ticks", 512),
        bin_width_ticks=cfg.get("bin_width_ticks", 1),
        return_raw=cfg.get("return_raw", False),
        max_raw_events=cfg.get("max_raw_events", 2048),
    )
