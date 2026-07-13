import json
import os
import sys
import traceback
from pprint import pprint
from socket import AF_INET, SO_REUSEADDR, SOCK_STREAM, SOL_SOCKET, socket

_HERE = os.path.dirname(os.path.abspath(__file__))

# PYNQ packages still come from the board environment.
sys.path.append('/usr/local/share/pynq-venv/lib/python3.8/site-packages')

# Use the QICK version bundled with the KIST bitstream by default.
_BUNDLED_QICK = os.path.join(_HERE, 'qick_lib_bundled')
_SYSTEM_QICK = '/home/xilinx/jupyter_notebooks/qick_version_0.2/qick_lib'

if os.environ.get('USE_SYSTEM_QICK') == '1':
    _qick_path = _SYSTEM_QICK
    _qick_source = 'system (USE_SYSTEM_QICK=1)'
elif os.path.isdir(_BUNDLED_QICK):
    _qick_path = _BUNDLED_QICK
    _qick_source = 'bundled qick_lib_bundled'
else:
    _qick_path = _SYSTEM_QICK
    _qick_source = 'system fallback'

sys.path.insert(0, _qick_path)
print(f"[QICK] Using library at: {_qick_path}")
print(f"[QICK] Source: {_qick_source}")

from qick import *


def _patch_qick_map_signal_paths_for_kist():
    """Skip unused DDR/MR readout branches that hang on the KIST overlay."""
    if os.environ.get('KIST_SKIP_DDR_MR_MAP', '1') == '0':
        return

    try:
        import qick.qick as _qick_core
    except Exception as exc:
        print(f"[WARN] Could not patch QICK map_signal_paths: {exc!r}")
        return

    if getattr(_qick_core.QickSoc, '_kist_skip_ddr_mr_map', False):
        return

    _orig_map_signal_paths = _qick_core.QickSoc.map_signal_paths
    _skip_ip = {
        'axis_buffer_ddr_v1_0',
        'axis_switch_ddr',
        'axis_switch_mr',
        'mr_buffer_et_0',
    }

    def _patched_map_signal_paths(self):
        original_ip_dict = self.ip_dict
        self.ip_dict = {
            key: val for key, val in original_ip_dict.items()
            if key not in _skip_ip
        }
        try:
            _orig_map_signal_paths(self)
        finally:
            self.ip_dict = original_ip_dict

        self._cfg.pop('ddr4_buf', None)
        self._cfg.pop('mr_buf', None)
        if self._cfg.get('tprocs') and not self._cfg['tprocs'][0].get('output_pins'):
            self._cfg['tprocs'][0]['output_pins'] = [
                ('output', 0, pin, f'kist_marker_{pin}') for pin in range(16)
            ]
        print("[QICK] Added synthetic KIST marker output pin mapping.")
        print("[QICK] Skipped unused DDR/MR readout mapping for KIST overlay.")

    _qick_core.QickSoc.map_signal_paths = _patched_map_signal_paths
    _qick_core.QickSoc._kist_skip_ddr_mr_map = True


_patch_qick_map_signal_paths_for_kist()

try:
    import qick as _qick_pkg
    _qick_ver = getattr(_qick_pkg, "__version__", None)
    if _qick_ver is None:
        _version_file = os.path.join(os.path.dirname(_qick_pkg.__file__), 'VERSION')
        try:
            with open(_version_file, 'r') as _vf:
                _qick_ver = _vf.read().strip()
        except FileNotFoundError:
            _qick_ver = '<unknown>'
except Exception as exc:
    _qick_ver = f'<unavailable: {exc!r}>'
    _qick_pkg = None

print(f"[QICK] Library version: {_qick_ver}")
print(f"[QICK] Module path: {getattr(_qick_pkg, '__file__', '?')}")

OVERLAY_PROFILE = os.environ.get("KQOS_OVERLAY", "ttag2ch").lower()
if OVERLAY_PROFILE in ("ttag2ch", "g2", "tcspc"):
    BITFILE = os.path.join(_HERE, "top_kist_ttag2ch_zcu111.bit")
    HWHFILE = os.path.join(_HERE, "top_kist_ttag2ch_zcu111.hwh")
elif OVERLAY_PROFILE in ("legacy", "kist", "3spd"):
    BITFILE = os.path.join(_HERE, "top_kist_zcu111.bit")
    HWHFILE = os.path.join(_HERE, "top_kist_zcu111.hwh")
else:
    raise ValueError(
        "Unknown KQOS_OVERLAY value "
        f"{OVERLAY_PROFILE!r}; use 'ttag2ch' or 'legacy'."
    )
print(f"[INFO] Overlay profile: {OVERLAY_PROFILE}")


def _check_bitstream_pair():
    if not os.path.exists(BITFILE):
        raise FileNotFoundError(f"Bitstream not found: {BITFILE}")
    if not os.path.exists(HWHFILE):
        raise FileNotFoundError(
            f"HWH not found: {HWHFILE}. Keep the .hwh next to the selected bitstream."
        )
    print(f"[OK] bitstream pair found: {BITFILE} + {HWHFILE}")


_check_bitstream_pair()
print(f"[INFO] Loading QickSoc from {BITFILE} ...")
soc = QickSoc(bitfile=BITFILE)
print("[OK] QickSoc initialized.")
print("[QICK] Generator channel map:")
for _idx, _gen in enumerate(soc._cfg.get('gens', [])):
    print(
        f"  gen_ch={_idx}: dac={_gen.get('dac')}, "
        f"f_fabric={_gen.get('f_fabric')}, fs={_gen.get('fs')}, "
        f"has_mixer={_gen.get('has_mixer')}"
    )

from proc import process


def create_socket():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind(('', 6030))
    server_socket.listen(1)
    return server_socket


server_socket = create_socket()
pprint('Now ready.')
while True:
    try:
        client_sock, ip = server_socket.accept()
        pprint(f"Client {ip} is connected")
        while True:
            recv_data = client_sock.recv(1024)
            print(recv_data)
            if not recv_data:
                client_sock.close()
                break
            response = process(json.loads(recv_data), soc)
            if response['results'] is not None:
                client_sock.sendall(json.dumps(response, separators=(",", ":")).encode())
    except Exception as exc:
        pprint(f"Disconnected from the client. Reason: {exc!r}")
        traceback.print_exc()
        pprint("Waiting for a new one.")
        try:
            server_socket.close()
        except Exception:
            pass
        server_socket = create_socket()
