from address_v6 import *
from qick import AveragerProgram, QickSoc
from utils import ns2cycle

def run_and_count(soc: QickSoc, prog: AveragerProgram, cfg: dict) -> list:
    PL_initialization()
    for mmio_timed_pwm in mmio_timed_pwms:
        mmio_timed_pwm.write(ADD_DELAY, 1)
        mmio_timed_pwm.write(ADD_CNT_TRG, cfg["reps"])

    for mmio_timed_pwm in mmio_timed_pwms:
        mmio_timed_pwm.write(ADD_WIDTH, ns2cycle((cfg['ro_len'])-1))
    
    # mmio_spd_mux.write(ADD_SPD_SELECT, 8191)
    prog.acquire_decimated(soc, load_pulses=True, progress=False, debug=False)
    
    while True:
        complete_flag = True
        # 모든 카운터의 comp 신호가 '1'로 감지될 경우 카운트 읽음
        if 'ro_memory' in cfg.keys():
            for memory_num in cfg['ro_memory']:
                if not mmio_timed_pwms[memory_num].read(ADD_COMP):
                    complete_flag = False
        if '_ro_memory' in cfg.keys():
            for memory_num in cfg['_ro_memory']:
                if not mmio_timed_pwms[memory_num].read(ADD_COMP):
                    complete_flag = False
        if complete_flag:
            break

    counts = {}

    if 'ro_memory' in cfg.keys():
        for memory_num in cfg['ro_memory']:
            counts[memory_num] = mmio_async_cnts[memory_num].read(ADD_CNT)
    if '_ro_memory' in cfg.keys():
        for memory_num in cfg['_ro_memory']:
            counts[memory_num] = mmio_async_cnts[memory_num].read(ADD_CNT2)
    return counts