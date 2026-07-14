import argparse
import json
import socket
import time
from pathlib import Path


def recv_json(sock, timeout_s):
    sock.settimeout(timeout_s)
    chunks = []
    decoder = json.JSONDecoder()
    text = ""

    while True:
        try:
            chunk = sock.recv(65536)
        except socket.timeout:
            break
        if not chunk:
            break

        chunks.append(chunk)
        text = b"".join(chunks).decode()
        try:
            obj, end = decoder.raw_decode(text)
        except json.JSONDecodeError:
            continue
        if text[end:].strip():
            raise ValueError("Received extra data after the JSON response")
        return obj

    if not text:
        raise TimeoutError("No response received from the KQOS server")
    return json.loads(text)


def make_request(args):
    return {
        "command": "g2",
        "mode": "free_run",
        "capture_ms": args.capture_ms,
        "capture_limit": args.capture_limit,
        "window_ticks": args.window_ticks,
        "bin_width_ticks": args.bin_width_ticks,
        "ref_ch": args.ref_ch,
        "sig_ch": args.sig_ch,
        "return_raw": args.return_raw,
        "max_raw_events": args.max_raw_events,
    }


def run_capture(args):
    request = make_request(args)
    read_timeout_s = max(args.timeout_s, args.capture_ms / 1000.0 + 2.0)
    with socket.create_connection((args.host, args.port), timeout=args.timeout_s) as sock:
        sock.sendall(json.dumps(request, separators=(",", ":")).encode())
        return recv_json(sock, read_timeout_s)


def summarize_response(response):
    result = response.get("results", {})
    meta = result.get("meta", {})
    hist = result.get("hist", [])
    return {
        "event_count": int(meta.get("event_count", 0)),
        "ref_events": int(meta.get("ref_events", 0)),
        "signal_events": int(meta.get("signal_events", 0)),
        "full": bool(meta.get("full", False)),
        "done": bool(meta.get("done", False)),
        "overflow": bool(meta.get("overflow", False)),
        "wrapped": bool(meta.get("wrapped", False)),
        "total_coincidences": sum(int(v) for v in hist),
        "max_bin": max(hist) if hist else 0,
        "hist_bins": len(hist),
    }


def add_to_aggregate(aggregate, response, elapsed_s):
    result = response.get("results", {})
    meta = result.get("meta", {})
    hist = [int(v) for v in result.get("hist", [])]

    if aggregate["hist"] is None:
        aggregate["tau_ticks"] = result.get("tau_ticks", [])
        aggregate["tau_ns"] = result.get("tau_ns", [])
        aggregate["hist"] = hist[:]
    else:
        if len(hist) != len(aggregate["hist"]):
            raise ValueError("Histogram length changed during repeated acquisition")
        aggregate["hist"] = [a + b for a, b in zip(aggregate["hist"], hist)]

    summary = summarize_response(response)
    summary["elapsed_s"] = elapsed_s
    aggregate["captures"].append(summary)
    aggregate["meta"]["shots"] += 1
    aggregate["meta"]["total_events"] += summary["event_count"]
    aggregate["meta"]["total_ref_events"] += summary["ref_events"]
    aggregate["meta"]["total_signal_events"] += summary["signal_events"]
    aggregate["meta"]["total_coincidences"] += summary["total_coincidences"]
    aggregate["meta"]["full_shots"] += int(summary["full"])
    aggregate["meta"]["overflow_shots"] += int(summary["overflow"])
    aggregate["meta"]["wrapped_shots"] += int(summary["wrapped"])
    aggregate["meta"]["tick_ns"] = meta.get("tick_ns")
    aggregate["meta"]["channel_map"] = meta.get("channel_map")
    aggregate["meta"]["capture_ms"] = meta.get("capture_ms_requested")
    aggregate["meta"]["capture_limit"] = meta.get("capture_limit")
    aggregate["meta"]["window_ticks"] = meta.get("window_ticks")
    aggregate["meta"]["bin_width_ticks"] = meta.get("bin_width_ticks")


def save_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def print_capture_summary(index, response):
    summary = summarize_response(response)
    print(
        f"[{index:04d}] events={summary['event_count']} "
        f"ref={summary['ref_events']} sig={summary['signal_events']} "
        f"full={summary['full']} overflow={summary['overflow']} "
        f"coinc={summary['total_coincidences']} max_bin={summary['max_bin']}"
    )


def main():
    parser = argparse.ArgumentParser(
        description="Run a KQOS 2-channel g2 time-tagger capture over TCP."
    )
    parser.add_argument("--host", required=True, help="ZCU111/PYNQ board IP")
    parser.add_argument("--port", type=int, default=6030)
    parser.add_argument("--capture-ms", type=float, default=100.0)
    parser.add_argument("--capture-limit", type=int, default=32768)
    parser.add_argument("--window-ticks", type=int, default=512)
    parser.add_argument("--bin-width-ticks", type=int, default=1)
    parser.add_argument("--ref-ch", type=int, default=2)
    parser.add_argument("--sig-ch", type=int, default=0)
    parser.add_argument("--return-raw", action="store_true")
    parser.add_argument("--max-raw-events", type=int, default=2048)
    parser.add_argument("--timeout-s", type=float, default=3.0)
    parser.add_argument("--out", help="Optional JSON output path")
    parser.add_argument("--out-dir", help="Directory for per-capture JSON files")
    parser.add_argument("--aggregate-out", help="Optional aggregate JSON output path")
    parser.add_argument("--repeat", type=int, help="Number of captures to run")
    parser.add_argument("--total-s", type=float, help="Repeat captures until this wall time elapses")
    parser.add_argument("--interval-s", type=float, default=0.0, help="Delay between repeated captures")
    args = parser.parse_args()

    max_captures = args.repeat
    if max_captures is None and args.total_s is None:
        max_captures = 1
    if max_captures is not None and max_captures <= 0:
        raise ValueError("--repeat must be positive")
    if args.total_s is not None and args.total_s <= 0:
        raise ValueError("--total-s must be positive")

    stamp = time.strftime("%Y%m%d_%H%M%S")
    out_dir = Path(args.out_dir) if args.out_dir else None
    aggregate = {
        "tau_ticks": [],
        "tau_ns": [],
        "hist": None,
        "captures": [],
        "meta": {
            "shots": 0,
            "total_events": 0,
            "total_ref_events": 0,
            "total_signal_events": 0,
            "total_coincidences": 0,
            "full_shots": 0,
            "overflow_shots": 0,
            "wrapped_shots": 0,
        },
    }

    start_s = time.time()
    index = 0
    while True:
        if max_captures is not None and index >= max_captures:
            break
        if args.total_s is not None and index > 0 and time.time() - start_s >= args.total_s:
            break

        index += 1
        response = run_capture(args)
        elapsed_s = time.time() - start_s
        add_to_aggregate(aggregate, response, elapsed_s)
        print_capture_summary(index, response)

        if out_dir:
            save_json(out_dir / f"g2_{stamp}_{index:04d}.json", response)

        if args.interval_s > 0:
            time.sleep(args.interval_s)

    if aggregate["hist"] is None:
        raise RuntimeError("No captures were completed")

    if index == 1 and args.out:
        save_json(args.out, response)
        print(f"saved={args.out}")

    aggregate_out = args.aggregate_out
    if aggregate_out is None and index > 1 and args.out:
        aggregate_out = args.out
    if aggregate_out:
        save_json(aggregate_out, aggregate)
        print(f"aggregate_saved={aggregate_out}")

    print("g2 repeated capture complete")
    print(json.dumps(aggregate["meta"], indent=2))
    print(
        f"hist_bins={len(aggregate['hist'])} "
        f"total_coincidences={aggregate['meta']['total_coincidences']} "
        f"max_bin={max(aggregate['hist']) if aggregate['hist'] else 0}"
    )


if __name__ == "__main__":
    main()
