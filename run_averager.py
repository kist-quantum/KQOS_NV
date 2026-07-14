from address_v6 import (
    ADD_COMP,
    ADD_CNT,
    ADD_CNT1,
    ADD_CNT2,
    ADD_CNT_TRG,
    ADD_DELAY,
    ADD_WIDTH,
    PL_initialization,
    mmio_async_cnts,
    mmio_timed_pwms,
)
from qick import AveragerProgram, QickSoc
from utils import ns2cycle


def _memory_slots(cfg: dict, *keys: str):
    slots = []
    for key in keys:
        if key in cfg:
            slots.extend(cfg[key])
    return slots


def run_and_count(soc: QickSoc, prog: AveragerProgram, cfg: dict) -> dict:
    PL_initialization()

    for mmio_timed_pwm in mmio_timed_pwms:
        mmio_timed_pwm.write(ADD_DELAY, 1)
        mmio_timed_pwm.write(ADD_CNT_TRG, cfg["reps"])

    for mmio_timed_pwm in mmio_timed_pwms:
        mmio_timed_pwm.write(ADD_WIDTH, ns2cycle(cfg["ro_len"] - 1))

    # QICK 0.2.281 does not accept the older debug=False kwarg here.
    # prog.acquire_decimated(soc, load_pulses=True, progress=False)
    prog.run(soc, load_pulses=True)

    cnt1_slots = _memory_slots(cfg, "CNT1_memory", "ro_memory")
    cnt2_slots = _memory_slots(cfg, "CNT2_memory", "_ro_memory")
    cnt3_slots = _memory_slots(cfg, "CNT3_memory")

    while True:
        complete_flag = True
        for memory_num in cnt1_slots:
            if not mmio_timed_pwms[memory_num].read(ADD_COMP):
                complete_flag = False
        for memory_num in cnt2_slots:
            if not mmio_timed_pwms[memory_num].read(ADD_COMP):
                complete_flag = False
        for memory_num in cnt3_slots:
            if not mmio_timed_pwms[memory_num].read(ADD_COMP):
                complete_flag = False
        if complete_flag:
            break

    counts = {}

    # Existing KQOS protocol: CNT1_memory reads the primary SPD channel.
    # In the 3-SPD KIST overlay this is PMOD1_2_LS_SPD2 / i_sig[0].
    for memory_num in cnt1_slots:
        counts[memory_num] = mmio_async_cnts[memory_num].read(ADD_CNT)

    # Existing KQOS protocol: CNT2_memory reads the second requested channel.
    # In the 3-SPD KIST overlay this is PMOD1_7_LS_SPD3 / i_sig[2].
    for memory_num in cnt2_slots:
        counts[memory_num] = mmio_async_cnts[memory_num].read(ADD_CNT2)

    # New optional KQOS protocol: CNT3_memory reads the remaining SPD channel.
    # In the 3-SPD KIST overlay this is PMOD0_2_LS_SPD1 / i_sig[1].
    # Keep memory_num values distinct across CNT*_memory lists with the current
    # flat {memory_num: count} response format.
    for memory_num in cnt3_slots:
        counts[memory_num] = mmio_async_cnts[memory_num].read(ADD_CNT1)

    return counts
