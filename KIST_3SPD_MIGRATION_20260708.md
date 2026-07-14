# KIST 3-SPD Overlay Migration

Date: 2026-07-08

Target:

`D:\Vivado\260513_DYK_workspace\KQOS_NV-main_260707\KQOS_NV-main`

Source overlay/runtime reference:

`D:\Vivado\260513_DYK_workspace\NV_server_deploy_3SPD_20260517`

## Applied Runtime Changes

- `main.py` now loads `top_kist_zcu111.bit` and checks for matching
  `top_kist_zcu111.hwh`.
- `main.py` prefers bundled QICK `0.2.281` from `qick_lib_bundled`, with
  `USE_SYSTEM_QICK=1` as a system-QICK fallback.
- `proc.py` was intentionally preserved to keep the KQOS command set:
  `Lifetime`, `pulse_PSB_GR`, `pulse_ZPL_GR`, `Nuclear_ODMR`, and `pulse_gen`
  remain available.
- `run_averager.py` preserves the KQOS `CNT1_memory` and `CNT2_memory`
  request keys while using the KIST 3-SPD counter registers.
- `run_averager.py` also accepts optional `CNT3_memory` for the remaining SPD
  channel without changing the existing flat response format.
- `address_v6.py` now matches the `top_kist_zcu111` AXI map.

## Overlay Artifacts

- `top_kist_zcu111.bit`
- `top_kist_zcu111.hwh`
- `qick_lib_bundled/qick/VERSION` = `0.2.281`

KIST build evidence from the source project:

- Build date: 2026-05-17 resume build
- Timing: WNS `+0.030 ns`, WHS `+0.002 ns`
- Result: timing met

## Counter Mapping

```text
PMOD1_2_LS_SPD2 -> ADD_CNT  (0x0C)
PMOD0_2_LS_SPD1 -> ADD_CNT1 (0x38)
PMOD1_7_LS_SPD3 -> ADD_CNT2 (0x3C)
```

The KQOS TCP protocol currently returns:

- `CNT1_memory` -> `ADD_CNT`
- `CNT2_memory` -> `ADD_CNT2`
- `CNT3_memory` -> `ADD_CNT1`

Use `address_v6.read_all_spds(memory_num)` when all three SPD channels are
needed from one PWM/counter slot.

The current response shape is still `{memory_num: count}`. If the same
`memory_num` is requested in multiple `CNT*_memory` lists, later writes in
`run_averager.py` overwrite earlier values. Use distinct memory slots when
requesting `CNT1_memory`, `CNT2_memory`, and `CNT3_memory` in one command.

## Rollback

Timestamped backups were created before editing:

- `main.py.20260708_095447.bak`
- `run_averager.py.20260708_095447.bak`
- `address_v6.py.20260708_095447.bak`
- `run_averager.py.20260708_100948.bak`
- `KIST_3SPD_MIGRATION_20260708.md.20260708_100948.bak`

The old `qick_111_240426_cnt_x13.*` and `qick_111_241112_v6.*` bit/hwh pairs
were left in place.
