from pynq import MMIO

# PL module의 axi-lite address 정보
BASE_ADD_TPWM0 = 0x00_A010_0000  # timed_pwm_0의 base address
BASE_ADD_ACNT0 = 0x00_A010_1000  # async counter0의 base address
BASE_ADD_TPWM1 = 0x00_A011_0000  # timed_pwm_1의 base address
BASE_ADD_ACNT1 = 0x00_A011_1000  # async counter1의 base address
BASE_ADD_TPWM2 = 0x00_A012_0000  # timed_pwm_2의 base address
BASE_ADD_ACNT2 = 0x00_A012_1000  # async counter2의 base address
BASE_ADD_TPWM3 = 0x00_A013_0000  # timed_pwm_3의 base address
BASE_ADD_ACNT3 = 0x00_A013_1000  # async counter3의 base address
BASE_ADD_TPWM4 = 0x00_A014_0000  # timed_pwm_4의 base address
BASE_ADD_ACNT4 = 0x00_A014_1000  # async counter4의 base address
BASE_ADD_TPWM5 = 0x00_A015_0000  # timed_pwm_5의 base address
BASE_ADD_ACNT5 = 0x00_A015_1000  # async counter5의 base address
BASE_ADD_TPWM6 = 0x00_A016_0000  # timed_pwm_6의 base address
BASE_ADD_ACNT6 = 0x00_A016_1000  # async counter6의 base address
BASE_ADD_TPWM7 = 0x00_A017_0000  # timed_pwm_7의 base address
BASE_ADD_ACNT7 = 0x00_A017_1000  # async counter7의 base address
BASE_ADD_TPWM8 = 0x00_A018_0000  # timed_pwm_8의 base address
BASE_ADD_ACNT8 = 0x00_A018_1000  # async counter8의 base address
BASE_ADD_TPWM9 = 0x00_A019_0000  # timed_pwm_9의 base address
BASE_ADD_ACNT9 = 0x00_A019_1000  # async counter9의 base address
BASE_ADD_TPWM10 = 0x00_A01A_0000  # timed_pwm_10의 base address
BASE_ADD_ACNT10 = 0x00_A01A_1000  # async counter10의 base address
BASE_ADD_TPWM11 = 0x00_A01B_0000  # timed_pwm_11의 base address
BASE_ADD_ACNT11 = 0x00_A01B_1000  # async counter11의 base address
BASE_ADD_TPWM12 = 0x00_A01C_0000  # timed_pwm_12의 base address
BASE_ADD_ACNT12 = 0x00_A01C_1000  # async counter12의 base address

# BASE_ADD_PATT = 0x00_A001_0000 # patt_generator의 base address
# BASE_SPD_MUX = 0x00_A002_0000 # spd_mux의 base address
# axi module의 포트별 offset address
ADD_RANGE = 0xFFF  # address range
ADD_RSTN = 0x0  # reset, '0' 입력시 PL 모듈 리셋
ADD_DELAY = 0x4  # delay, readout 딜레이 설정
ADD_WIDTH = 0x8  # width, readout 폭 설정
ADD_CNT = 0xC  # count, 측정된 SPD 카운트
ADD_CNT1 = 0x38
ADD_CNT2 = 0x3c

ADD_CNT_TRG = 0x10  # trigger count
ADD_COMP = 0x14  # readout 완료시 '1', 이 신호 모니터링해서 측정 완료됨을 확인

ADD_RAM_WR_ADD = 0x1C # pattern generator의 ram write address
ADD_RAM_WR_DATA = 0x20 # pattern generator의 ram write data
ADD_RAM_WR_WEN = 0x24 # pattern generator의 ram write enable
ADD_RAM_RD_ADD_SEL = 0x28   # pattern generator의 ram read add select
                            # '0': readout 트리거 함수인 trigger()를 카운트해서 ram read address로 사용함
                            # '1': ADD_RAM_RD_ADD 값을 ram read address로 사용함, 오버레이 ram에 저장된 기본 데이터가 아닌, 파이썬에서 임의의 데이터로 pattern을 생성하고 싶을 때 사용
ADD_RAM_RD_ADD = 0x2C # pattern generator의 ram read address
ADD_RAM_RD_DATA = 0x30 # pattern generator의 ram read data
ADD_SPD_SELECT = 0x34
RAM_BUF_SIZE = 131072
SPD_SEL = 1

# PL module (counter, timed_pwm) 초기화
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


# mmio_patt_gen = MMIO(BASE_ADD_PATT, ADD_RANGE)  
# mmio_spd_mux = MMIO(BASE_SPD_MUX, ADD_RANGE) 

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
        mmio_timed_pwm12
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
    mmio_async_cnt12
]

def PL_initialization():
    # PL module (counter, timed_pwm) 초기화
    for mmio_timed_pwm in mmio_timed_pwms:
        mmio_timed_pwm.write(ADD_RSTN, 0x1)
        mmio_timed_pwm.write(ADD_RSTN, 0x0)
        mmio_timed_pwm.write(ADD_RSTN, 0x1)
    for mmio_async_cnt in mmio_async_cnts:
        mmio_async_cnt.write(ADD_RSTN, 0x1)
        mmio_async_cnt.write(ADD_RSTN, 0x0)
        mmio_async_cnt.write(ADD_RSTN, 0x1)
        
    # mmio_patt_gen.write(ADD_RSTN, 0x1)
    # mmio_patt_gen.write(ADD_RSTN, 0x0)
    # mmio_patt_gen.write(ADD_RSTN, 0x1)
    # mmio_patt_gen.write(ADD_RAM_WR_ADD, 0)
    # mmio_patt_gen.write(ADD_RAM_WR_DATA, 0)
    # mmio_patt_gen.write(ADD_RAM_WR_WEN, 0)
    # mmio_patt_gen.write(ADD_RAM_RD_ADD_SEL, 0)
    # mmio_patt_gen.write(ADD_RAM_RD_ADD, 0)
