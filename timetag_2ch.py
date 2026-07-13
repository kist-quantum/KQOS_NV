import time

import numpy as np

from address_v6 import (
    TTAG_CAPTURE_LIMIT,
    TTAG_CHANNEL_NAMES,
    TTAG_CH_SELECT,
    TTAG_CONTROL,
    TTAG_CONTROL_CIRCULAR,
    TTAG_CONTROL_CLEAR,
    TTAG_CONTROL_ENABLE,
    TTAG_CONTROL_READ_AUTO_INC,
    TTAG_CONTROL_RESET_TIME,
    TTAG_CONTROL_STOP_ON_FULL,
    TTAG_DEFAULT_CAPTURE_LIMIT,
    TTAG_DEFAULT_REF_CH,
    TTAG_DEFAULT_SIG_CH,
    TTAG_DEPTH,
    TTAG_EVENT_COUNT,
    TTAG_EVENT_HI,
    TTAG_EVENT_LO,
    TTAG_EVENT_WIDTH,
    TTAG_NOMINAL_TICK_HZ,
    TTAG_OVERFLOW_COUNT,
    TTAG_READ_INDEX,
    TTAG_STATUS,
    TTAG_STATUS_CAPTURE_READY,
    TTAG_STATUS_CIRCULAR,
    TTAG_STATUS_DONE,
    TTAG_STATUS_ENABLED,
    TTAG_STATUS_FULL,
    TTAG_STATUS_OVERFLOW,
    TTAG_STATUS_STOP_ON_FULL,
    TTAG_STATUS_WRAPPED,
    TTAG_TICK_HZ,
    TTAG_TIME_NOW,
    TTAG_TOTAL_COUNT,
    TTAG_VERSION,
    TTAG_VERSION_MAGIC,
    TTAG_WRITE_PTR,
    mmio_ttag2ch,
)


U32_MOD = 1 << 32
U32_HALF = 1 << 31


class TimeTagger2CH:
    """MMIO driver for the KIST ZCU111 2-channel snapshot time tagger."""

    def __init__(self, mmio=None):
        self.mmio = mmio if mmio is not None else mmio_ttag2ch

    def _read(self, offset):
        return int(self.mmio.read(offset)) & 0xFFFFFFFF

    def _write(self, offset, value):
        self.mmio.write(offset, int(value) & 0xFFFFFFFF)

    @staticmethod
    def channel_name(index):
        return TTAG_CHANNEL_NAMES.get(int(index), f"i_sig[{int(index)}]")

    @staticmethod
    def ch_select_value(ref_ch, sig_ch):
        ref_ch = int(ref_ch)
        sig_ch = int(sig_ch)
        if not 0 <= ref_ch <= 2:
            raise ValueError(f"ref_ch must be 0, 1, or 2, got {ref_ch}")
        if not 0 <= sig_ch <= 2:
            raise ValueError(f"sig_ch must be 0, 1, or 2, got {sig_ch}")
        return ref_ch | (sig_ch << 4)

    @staticmethod
    def _control_value(enable=False, circular=False, stop_on_full=True,
                       read_auto_inc=True):
        value = 0
        if enable:
            value |= TTAG_CONTROL_ENABLE
        if circular:
            value |= TTAG_CONTROL_CIRCULAR
        if stop_on_full:
            value |= TTAG_CONTROL_STOP_ON_FULL
        if read_auto_inc:
            value |= TTAG_CONTROL_READ_AUTO_INC
        return value

    def identify(self, strict=True):
        info = {
            "version": self._read(TTAG_VERSION),
            "depth": self._read(TTAG_DEPTH),
            "tick_hz": self._read(TTAG_TICK_HZ),
            "event_width": self._read(TTAG_EVENT_WIDTH),
        }
        if strict and info["version"] != TTAG_VERSION_MAGIC:
            raise RuntimeError(
                "2ch time tagger was not detected at 0xA01D0000 "
                f"(VERSION=0x{info['version']:08X})"
            )
        return info

    def status(self):
        raw = self._read(TTAG_STATUS)
        return {
            "raw": raw,
            "enabled": bool(raw & TTAG_STATUS_ENABLED),
            "full": bool(raw & TTAG_STATUS_FULL),
            "overflow": bool(raw & TTAG_STATUS_OVERFLOW),
            "wrapped": bool(raw & TTAG_STATUS_WRAPPED),
            "done": bool(raw & TTAG_STATUS_DONE),
            "capture_ready": bool(raw & TTAG_STATUS_CAPTURE_READY),
            "circular": bool(raw & TTAG_STATUS_CIRCULAR),
            "stop_on_full": bool(raw & TTAG_STATUS_STOP_ON_FULL),
            "event_count": self._read(TTAG_EVENT_COUNT),
            "total_count": self._read(TTAG_TOTAL_COUNT),
            "overflow_count": self._read(TTAG_OVERFLOW_COUNT),
            "write_ptr": self._read(TTAG_WRITE_PTR),
            "time_now": self._read(TTAG_TIME_NOW),
        }

    def configure(self, capture_limit=TTAG_DEFAULT_CAPTURE_LIMIT,
                  ref_ch=TTAG_DEFAULT_REF_CH, sig_ch=TTAG_DEFAULT_SIG_CH):
        capture_limit = int(capture_limit)
        if capture_limit <= 0:
            capture_limit = TTAG_DEFAULT_CAPTURE_LIMIT
        depth = self._read(TTAG_DEPTH) or TTAG_DEFAULT_CAPTURE_LIMIT
        capture_limit = min(capture_limit, depth)
        self._write(TTAG_CAPTURE_LIMIT, capture_limit)
        self._write(TTAG_CH_SELECT, self.ch_select_value(ref_ch, sig_ch))
        return capture_limit

    def clear(self, reset_time=True, circular=False, stop_on_full=True):
        base = self._control_value(
            enable=False,
            circular=circular,
            stop_on_full=stop_on_full,
            read_auto_inc=True,
        )
        pulse = TTAG_CONTROL_CLEAR
        if reset_time:
            pulse |= TTAG_CONTROL_RESET_TIME
        self._write(TTAG_CONTROL, base | pulse)
        self._write(TTAG_CONTROL, base)
        self._write(TTAG_READ_INDEX, 0)

    def start(self, circular=False, stop_on_full=True):
        self._write(
            TTAG_CONTROL,
            self._control_value(
                enable=True,
                circular=circular,
                stop_on_full=stop_on_full,
                read_auto_inc=True,
            ),
        )

    def stop(self, circular=False, stop_on_full=True):
        self._write(
            TTAG_CONTROL,
            self._control_value(
                enable=False,
                circular=circular,
                stop_on_full=stop_on_full,
                read_auto_inc=True,
            ),
        )

    def capture(self, capture_ms, capture_limit=TTAG_DEFAULT_CAPTURE_LIMIT,
                ref_ch=TTAG_DEFAULT_REF_CH, sig_ch=TTAG_DEFAULT_SIG_CH,
                circular=False, stop_on_full=True, poll_done=True):
        self.identify(strict=True)
        actual_limit = self.configure(capture_limit, ref_ch, sig_ch)
        self.clear(reset_time=True, circular=circular, stop_on_full=stop_on_full)
        self.start(circular=circular, stop_on_full=stop_on_full)

        deadline = time.time() + max(0.0, float(capture_ms)) / 1000.0
        while time.time() < deadline:
            if poll_done:
                st = self.status()
                if st["done"] or (st["full"] and stop_on_full):
                    break
            remaining = deadline - time.time()
            time.sleep(max(0.001, min(0.01, remaining)))

        self.stop(circular=circular, stop_on_full=stop_on_full)
        st = self.status()
        st["capture_limit"] = actual_limit
        return st

    def read_events(self, max_events=None):
        depth = self._read(TTAG_DEPTH) or TTAG_DEFAULT_CAPTURE_LIMIT
        count = min(self._read(TTAG_EVENT_COUNT), depth)
        if max_events is not None:
            count = min(count, int(max_events))

        self._write(TTAG_READ_INDEX, 0)
        events = []
        for _ in range(count):
            timestamp = self._read(TTAG_EVENT_LO)
            event_hi = self._read(TTAG_EVENT_HI)
            events.append({
                "timestamp": timestamp,
                "channel_mask": event_hi & 0x3,
                "flags": (event_hi >> 2) & 0x3,
            })
        return events

    @staticmethod
    def split_channels(events, unwrap=True):
        ref = []
        sig = []
        last_ts = None
        epoch = 0

        for event in events:
            ts = int(event["timestamp"])
            if unwrap and last_ts is not None and ts + U32_HALF < last_ts:
                epoch += U32_MOD
            last_ts = ts
            ts_unwrapped = ts + epoch

            mask = int(event["channel_mask"])
            if mask & 0x1:
                ref.append(ts_unwrapped)
            if mask & 0x2:
                sig.append(ts_unwrapped)

        return np.asarray(ref, dtype=np.int64), np.asarray(sig, dtype=np.int64)

    @staticmethod
    def histogram_g2(ref_ticks, sig_ticks, window_ticks=512,
                     bin_width_ticks=1, tick_hz=TTAG_NOMINAL_TICK_HZ):
        window_ticks = int(window_ticks)
        bin_width_ticks = int(bin_width_ticks)
        if window_ticks <= 0:
            raise ValueError("window_ticks must be positive")
        if bin_width_ticks <= 0:
            raise ValueError("bin_width_ticks must be positive")

        ref_ticks = np.asarray(ref_ticks, dtype=np.int64)
        sig_ticks = np.asarray(sig_ticks, dtype=np.int64)
        edges = np.arange(
            -window_ticks - 0.5 * bin_width_ticks,
            window_ticks + 0.5 * bin_width_ticks + bin_width_ticks,
            bin_width_ticks,
            dtype=float,
        )
        hist = np.zeros(len(edges) - 1, dtype=np.int64)

        if len(ref_ticks) and len(sig_ticks):
            sig_sorted = np.sort(sig_ticks)
            for ref in ref_ticks:
                lo = np.searchsorted(sig_sorted, ref - window_ticks, side="left")
                hi = np.searchsorted(sig_sorted, ref + window_ticks, side="right")
                if hi > lo:
                    diffs = sig_sorted[lo:hi] - ref
                    hist += np.histogram(diffs, bins=edges)[0]

        tau_ticks = 0.5 * (edges[:-1] + edges[1:])
        tick_ns = 1e9 / float(tick_hz or TTAG_NOMINAL_TICK_HZ)
        return tau_ticks, tau_ticks * tick_ns, hist


def acquire_g2(capture_ms=100, capture_limit=TTAG_DEFAULT_CAPTURE_LIMIT,
               ref_ch=TTAG_DEFAULT_REF_CH, sig_ch=TTAG_DEFAULT_SIG_CH,
               window_ticks=512, bin_width_ticks=1, return_raw=False,
               max_raw_events=2048):
    tagger = TimeTagger2CH()
    info = tagger.identify(strict=True)
    tick_hz = info.get("tick_hz") or TTAG_NOMINAL_TICK_HZ

    status_after_capture = tagger.capture(
        capture_ms=capture_ms,
        capture_limit=capture_limit,
        ref_ch=ref_ch,
        sig_ch=sig_ch,
        circular=False,
        stop_on_full=True,
        poll_done=True,
    )
    events = tagger.read_events()
    ref_ticks, sig_ticks = tagger.split_channels(events)
    tau_ticks, tau_ns, hist = tagger.histogram_g2(
        ref_ticks,
        sig_ticks,
        window_ticks=window_ticks,
        bin_width_ticks=bin_width_ticks,
        tick_hz=tick_hz,
    )

    result = {
        "tau_ticks": tau_ticks.astype(float).tolist(),
        "tau_ns": tau_ns.astype(float).tolist(),
        "hist": hist.astype(int).tolist(),
        "meta": {
            "capture_ms_requested": float(capture_ms),
            "capture_limit": int(status_after_capture["capture_limit"]),
            "event_count": int(status_after_capture["event_count"]),
            "total_count": int(status_after_capture["total_count"]),
            "overflow_count": int(status_after_capture["overflow_count"]),
            "full": bool(status_after_capture["full"]),
            "overflow": bool(status_after_capture["overflow"]),
            "wrapped": bool(status_after_capture["wrapped"]),
            "done": bool(status_after_capture["done"]),
            "ref_events": int(len(ref_ticks)),
            "signal_events": int(len(sig_ticks)),
            "tick_hz": int(tick_hz),
            "tick_ns": 1e9 / float(tick_hz),
            "bin_width_ticks": int(bin_width_ticks),
            "window_ticks": int(window_ticks),
            "ref_ch": int(ref_ch),
            "sig_ch": int(sig_ch),
            "channel_map": {
                "ref": tagger.channel_name(ref_ch),
                "signal": tagger.channel_name(sig_ch),
            },
            "version": f"0x{info['version']:08X}",
            "depth": int(info["depth"]),
            "event_width": int(info["event_width"]),
        },
    }

    if return_raw:
        limit = min(len(events), int(max_raw_events))
        result["raw_events"] = events[:limit]
        result["meta"]["raw_events_returned"] = limit
        result["meta"]["raw_events_truncated"] = len(events) > limit

    return result
