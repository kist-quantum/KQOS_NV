"""
main_update.py — server entry point for NEW bitstream `top_kist_zcu111.bit`

Build info:
  Project : qick_tprocv1_111_standard_tc11_20260514
  Date    : 2026-05-17 (resume build)
  Timing  : WNS = +0.030 ns, WHS = +0.002 ns (TIMING_MET)
  Counter : axi_async_counter_multi × 13 (3 SPDs per instance)

QICK library policy:
  This deploy bundle ships its OWN qick library (0.2.281) at
  ./qick_lib_bundled/, which is the exact version used to build the
  bitstream.  We prepend this path to sys.path so that `import qick`
  resolves to the bundled version, avoiding any API mismatch with the
  PYNQ board's pre-installed qick_version_0.2.

  If you intentionally want to use the system-installed qick instead,
  set the env var `USE_SYSTEM_QICK=1` before running.

Requirements on the PYNQ board:
  - PYNQ 2.7+
  - The bundle's bitstream + hwh pair must be in the same directory as
    this script (basename match `top_kist_zcu111.{bit,hwh}`).
"""
import os
import sys
import json
from pprint import pprint
from socket import AF_INET, SO_REUSEADDR, SOCK_STREAM, SOL_SOCKET, socket

# ── 1) QICK library path setup ──────────────────────────────────────────────
# Detect script's own directory (so this works from any cwd).
_HERE = os.path.dirname(os.path.abspath(__file__))

# Always include PYNQ's system venv (for pynq.MMIO, xrfdc, etc.)
sys.path.append('/usr/local/share/pynq-venv/lib/python3.8/site-packages')

# Choose qick path: bundled (default) vs system.
_BUNDLED_QICK = os.path.join(_HERE, 'qick_lib_bundled')
_SYSTEM_QICK  = '/home/xilinx/jupyter_notebooks/qick_version_0.2/qick_lib'

if os.environ.get('USE_SYSTEM_QICK') == '1':
    _qick_path = _SYSTEM_QICK
    _qick_source = 'system (USE_SYSTEM_QICK=1)'
elif os.path.isdir(_BUNDLED_QICK):
    _qick_path = _BUNDLED_QICK
    _qick_source = 'bundled (qick_lib_bundled/, version match guaranteed)'
else:
    _qick_path = _SYSTEM_QICK
    _qick_source = 'system (bundle not found — fallback)'

# Prepend (not append) so bundled qick wins over any pre-imported one.
sys.path.insert(0, _qick_path)
print(f"[QICK] Using library at: {_qick_path}")
print(f"[QICK] Source: {_qick_source}")

from qick import *

# Print QICK lib info for traceability
try:
    import qick as _qick_pkg
    _qick_ver = getattr(_qick_pkg, "__version__", None)
    if _qick_ver is None:
        # Older qick versions don't set __version__; read VERSION file directly.
        _vfile = os.path.join(os.path.dirname(_qick_pkg.__file__), 'VERSION')
        try:
            with open(_vfile, 'r') as _vf:
                _qick_ver = _vf.read().strip()
        except FileNotFoundError:
            _qick_ver = '<unknown>'
except Exception as e:
    _qick_ver = f'<unimportable: {e!r}>'
print(f"[QICK] Library version: {_qick_ver}")
print(f"[QICK] Module path: {getattr(_qick_pkg, '__file__', '?')}")

# ── 2) Bitstream / HWH sanity check ────────────────────────────────────────
BITFILE = os.path.join(_HERE, "top_kist_zcu111.bit")
HWHFILE = os.path.join(_HERE, "top_kist_zcu111.hwh")

def _check_bitstream_pair():
    if not os.path.exists(BITFILE):
        print(f"[FATAL] Bitstream not found: {BITFILE}")
        sys.exit(1)
    if not os.path.exists(HWHFILE):
        print(f"[FATAL] HWH not found: {HWHFILE}")
        print(f"  hint: artifacts produced as d_1.hwh — rename to top_kist_zcu111.hwh")
        sys.exit(1)
    print(f"[OK] bitstream pair found: {BITFILE} + {HWHFILE}")

_check_bitstream_pair()

# ── 3) Load bitstream ──────────────────────────────────────────────────────
print(f"[INFO] Loading QickSoc from {BITFILE} ...")
soc = QickSoc(bitfile=BITFILE)
print(f"[OK] QickSoc initialized.")

# ── 4) Import command dispatcher ────────────────────────────────────────────
from proc_update import process

# ── 5) TCP server (unchanged interface — port 6030) ─────────────────────────
def create_socket():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind(('', 6030))
    server_socket.listen(1)
    return server_socket


if __name__ == "__main__":
    server_socket = create_socket()
    pprint("Now ready.")
    while True:
        try:
            client_sock, ip = server_socket.accept()
            pprint(f"Client {ip} is connected")
            while True:
                recv_data = client_sock.recv(1024)
                if not recv_data:
                    client_sock.close()
                else:
                    response = process(json.loads(recv_data), soc)
                    if response['results']:
                        client_sock.send(json.dumps(response).encode())
        except Exception as e:
            pprint(f"Disconnected from the client. Reason: {e!r}")
            pprint("Waiting for a new one.")
            try:
                server_socket.close()
            except Exception:
                pass
            server_socket = create_socket()
