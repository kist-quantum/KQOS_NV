from pynq import MMIO

# Address map for top_kist_zcu111.bit and top_kist_ttag2ch_zcu111.bit.
# Legacy build: 2026-05-17 KIST ZCU111 resume build, WNS=+0.030 ns, WHS=+0.002 ns.
# Time tagger build: 2026-07-10 KIST ZCU111 2ch time tagger, WNS=+0.017 ns, WHS=+0.010 ns.
#
# Counter path:
#   PMOD1_2_LS_SPD2 -> xlconcat_1/In0 -> i_sig[0] -> ADD_CNT  (0x0C)
#   PMOD0_2_LS_SPD1 -> xlconcat_1/In1 -> i_sig[1] -> ADD_CNT1 (0x38)
#   PMOD1_7_LS_SPD3 -> xlconcat_1/In2 -> i_sig[2] -> ADD_CNT2 (0x3C)
#
# The SPD1/SPD2 label order follows the existing v6 measurement convention.

BASE_ADD_PATT = 0x00_A001_0000
BASE_SPD_MUX = 0x00_A002_0000

BASE_ADD_TPWM0 = 0x00_A003_0000
BASE_ADD_TPWM1 = 0x00_A004_0000
BASE_ADD_TPWM2 = 0x00_A005_0000
BASE_ADD_TPWM3 = 0x00_A006_0000
BASE_ADD_TPWM4 = 0x00_A007_0000
BASE_ADD_TPWM5 = 0x00_A008_0000
BASE_ADD_TPWM6 = 0x00_A009_0000
BASE_ADD_TPWM7 = 0x00_A00A_0000
BASE_ADD_TPWM8 = 0x00_A00B_0000
BASE_ADD_TPWM9 = 0x00_A00C_0000
BASE_ADD_TPWM10 = 0x00_A00D_0000
BASE_ADD_TPWM11 = 0x00_A00E_0000
BASE_ADD_TPWM12 = 0x00_A00F_0000

BASE_ADD_ACNT0 = 0x00_A010_0000
BASE_ADD_ACNT1 = 0x00_A011_0000
BASE_ADD_ACNT2 = 0x00_A012_0000
BASE_ADD_ACNT3 = 0x00_A013_0000
BASE_ADD_ACNT4 = 0x00_A014_0000
BASE_ADD_ACNT5 = 0x00_A015_0000
BASE_ADD_ACNT6 = 0x00_A016_0000
BASE_ADD_ACNT7 = 0x00_A017_0000
BASE_ADD_ACNT8 = 0x00_A018_0000
BASE_ADD_ACNT9 = 0x00_A019_0000
BASE_ADD_ACNT10 = 0x00_A01A_0000
BASE_ADD_ACNT11 = 0x00_A01B_0000
BASE_ADD_ACNT12 = 0x00_A01C_0000
BASE_ADD_TTAG2CH = 0x00_A01D_0000

ADD_RANGE = 0xFFF
TTAG_RANGE = 0x10000

ADD_RSTN = 0x0
ADD_DELAY = 0x4
ADD_WIDTH = 0x8

ADD_CNT = 0x0C
ADD_CNT1 = 0x38
ADD_CNT2 = 0x3C
HAS_MULTI_COUNTER = True

ADD_CNT_TRG = 0x10
ADD_COMP = 0x14

ADD_RAM_WR_ADD = 0x1C
ADD_RAM_WR_DATA = 0x20
ADD_RAM_WR_WEN = 0x24
ADD_RAM_RD_ADD_SEL = 0x28
ADD_RAM_RD_ADD = 0x2C
ADD_RAM_RD_DATA = 0x30
ADD_SPD_SELECT = 0x34
RAM_BUF_SIZE = 131072
SPD_SEL = 1

TTAG_CONTROL = 0x00
TTAG_STATUS = 0x04
TTAG_EVENT_COUNT = 0x08
TTAG_TOTAL_COUNT = 0x0C
TTAG_OVERFLOW_COUNT = 0x10
TTAG_WRITE_PTR = 0x14
TTAG_CAPTURE_LIMIT = 0x18
TTAG_READ_INDEX = 0x1C
TTAG_EVENT_LO = 0x20
TTAG_EVENT_HI = 0x24
TTAG_TIME_NOW = 0x28
TTAG_CH_SELECT = 0x2C
TTAG_VERSION = 0x30
TTAG_DEPTH = 0x34
TTAG_TICK_HZ = 0x38
TTAG_EVENT_WIDTH = 0x3C

TTAG_CONTROL_ENABLE = 1 << 0
TTAG_CONTROL_CLEAR = 1 << 1
TTAG_CONTROL_RESET_TIME = 1 << 2
TTAG_CONTROL_CIRCULAR = 1 << 3
TTAG_CONTROL_STOP_ON_FULL = 1 << 4
TTAG_CONTROL_READ_AUTO_INC = 1 << 5

TTAG_STATUS_ENABLED = 1 << 0
TTAG_STATUS_FULL = 1 << 1
TTAG_STATUS_OVERFLOW = 1 << 2
TTAG_STATUS_WRAPPED = 1 << 3
TTAG_STATUS_DONE = 1 << 4
TTAG_STATUS_CAPTURE_READY = 1 << 5
TTAG_STATUS_CIRCULAR = 1 << 6
TTAG_STATUS_STOP_ON_FULL = 1 << 7

TTAG_VERSION_MAGIC = 0x54544731  # TTG1
TTAG_DEFAULT_REF_CH = 2          # PMOD1_7_LS_SPD3 / i_sig[2]
TTAG_DEFAULT_SIG_CH = 0          # PMOD1_2_LS_SPD2 / i_sig[0]
TTAG_DEFAULT_CAPTURE_LIMIT = 32768
TTAG_NOMINAL_TICK_HZ = 384000000

TTAG_CHANNEL_NAMES = {
    0: "PMOD1_2_LS_SPD2",
    1: "PMOD0_2_LS_SPD1",
    2: "PMOD1_7_LS_SPD3",
}

mmio_timed_pwm0 = MMIO(BASE_ADD_TPWM0, ADD_RANGE)
mmio_timed_pwm1 = MMIO(BASE_ADD_TPWM1, ADD_RANGE)
mmio_timed_pwm2 = MMIO(BASE_ADD_TPWM2, ADD_RANGE)
mmio_timed_pwm3 = MMIO(BASE_ADD_TPWM3, ADD_RANGE)
mmio_timed_pwm4 = MMIO(BASE_ADD_TPWM4, ADD_RANGE)
mmio_timed_pwm5 = MMIO(BASE_ADD_TPWM5, ADD_RANGE)
mmio_timed_pwm6 = MMIO(BASE_ADD_TPWM6, ADD_RANGE)
mmio_timed_pwm7 = MMIO(BASE_ADD_TPWM7, ADD_RANGE)
mmio_timed_pwm8 = MMIO(BASE_ADD_TPWM8, ADD_RANGE)
mmio_timed_pwm9 = MMIO(BASE_ADD_TPWM9, ADD_RANGE)
mmio_timed_pwm10 = MMIO(BASE_ADD_TPWM10, ADD_RANGE)
mmio_timed_pwm11 = MMIO(BASE_ADD_TPWM11, ADD_RANGE)
mmio_timed_pwm12 = MMIO(BASE_ADD_TPWM12, ADD_RANGE)

mmio_async_cnt0 = MMIO(BASE_ADD_ACNT0, ADD_RANGE)
mmio_async_cnt1 = MMIO(BASE_ADD_ACNT1, ADD_RANGE)
mmio_async_cnt2 = MMIO(BASE_ADD_ACNT2, ADD_RANGE)
mmio_async_cnt3 = MMIO(BASE_ADD_ACNT3, ADD_RANGE)
mmio_async_cnt4 = MMIO(BASE_ADD_ACNT4, ADD_RANGE)
mmio_async_cnt5 = MMIO(BASE_ADD_ACNT5, ADD_RANGE)
mmio_async_cnt6 = MMIO(BASE_ADD_ACNT6, ADD_RANGE)
mmio_async_cnt7 = MMIO(BASE_ADD_ACNT7, ADD_RANGE)
mmio_async_cnt8 = MMIO(BASE_ADD_ACNT8, ADD_RANGE)
mmio_async_cnt9 = MMIO(BASE_ADD_ACNT9, ADD_RANGE)
mmio_async_cnt10 = MMIO(BASE_ADD_ACNT10, ADD_RANGE)
mmio_async_cnt11 = MMIO(BASE_ADD_ACNT11, ADD_RANGE)
mmio_async_cnt12 = MMIO(BASE_ADD_ACNT12, ADD_RANGE)

mmio_patt_gen = MMIO(BASE_ADD_PATT, ADD_RANGE)
mmio_spd_mux = MMIO(BASE_SPD_MUX, ADD_RANGE)
mmio_ttag2ch = MMIO(BASE_ADD_TTAG2CH, TTAG_RANGE)

mmio_timed_pwms = [
    mmio_timed_pwm0,
    mmio_timed_pwm1,
    mmio_timed_pwm2,
    mmio_timed_pwm3,
    mmio_timed_pwm4,
    mmio_timed_pwm5,
    mmio_timed_pwm6,
    mmio_timed_pwm7,
    mmio_timed_pwm8,
    mmio_timed_pwm9,
    mmio_timed_pwm10,
    mmio_timed_pwm11,
    mmio_timed_pwm12,
]

mmio_async_cnts = [
    mmio_async_cnt0,
    mmio_async_cnt1,
    mmio_async_cnt2,
    mmio_async_cnt3,
    mmio_async_cnt4,
    mmio_async_cnt5,
    mmio_async_cnt6,
    mmio_async_cnt7,
    mmio_async_cnt8,
    mmio_async_cnt9,
    mmio_async_cnt10,
    mmio_async_cnt11,
    mmio_async_cnt12,
]


def PL_initialization():
    for mmio_timed_pwm in mmio_timed_pwms:
        mmio_timed_pwm.write(ADD_RSTN, 0x1)
        mmio_timed_pwm.write(ADD_RSTN, 0x0)
        mmio_timed_pwm.write(ADD_RSTN, 0x1)

    for mmio_async_cnt in mmio_async_cnts:
        mmio_async_cnt.write(ADD_RSTN, 0x1)
        mmio_async_cnt.write(ADD_RSTN, 0x0)
        mmio_async_cnt.write(ADD_RSTN, 0x1)

    mmio_patt_gen.write(ADD_RSTN, 0x1)
    mmio_patt_gen.write(ADD_RSTN, 0x0)
    mmio_patt_gen.write(ADD_RSTN, 0x1)
    mmio_patt_gen.write(ADD_RAM_WR_ADD, 0)
    mmio_patt_gen.write(ADD_RAM_WR_DATA, 0)
    mmio_patt_gen.write(ADD_RAM_WR_WEN, 0)
    mmio_patt_gen.write(ADD_RAM_RD_ADD_SEL, 0)
    mmio_patt_gen.write(ADD_RAM_RD_ADD, 0)


def read_all_spds(memory_num: int) -> dict:
    mmio = mmio_async_cnts[memory_num]
    return {
        "PMOD1_2_LS_SPD2": mmio.read(ADD_CNT),
        "PMOD0_2_LS_SPD1": mmio.read(ADD_CNT1),
        "PMOD1_7_LS_SPD3": mmio.read(ADD_CNT2),
    }
