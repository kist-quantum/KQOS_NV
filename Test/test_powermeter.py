import ctypes
from ctypes import byref, c_void_p, c_char_p, c_uint32, c_double, c_int32, create_string_buffer
import pyvisa
import sys
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# DLL 경로 설정
tlpm = ctypes.WinDLL(r"C:\Program Files\IVI Foundation\VISA\Win64\Bin\TLPM_64.dll")

tlpm.TLPM_init.argtypes = [ctypes.c_char_p, ctypes.c_bool, ctypes.c_bool, ctypes.POINTER(ctypes.c_int)]
tlpm.TLPM_init.restype  = ctypes.c_int   # ViStatus (에러 코드)

device_count = ctypes.c_int()
err = tlpm.TLPM_findRsrc(0, ctypes.byref(device_count))
if err != 0 or device_count.value == 0:
    print("장치를 찾을 수 없습니다.")
    # 필요한 오류 처리 수행 후 종료
    sys.exit(1)

name_buf = ctypes.create_string_buffer(1024)
tlpm.TLPM_getRsrcName(0, 0, name_buf)
resource_name = name_buf.value
print("발견된 장치:", resource_name.decode())
instr = ctypes.c_int()
err = tlpm.TLPM_init(resource_name, True, False, ctypes.byref(instr))
if err:
    print("TLPM_init 실패, 에러 코드:", err)
    sys.exit(1)

print("장치 초기화 성공, 핸들 ID:", instr.value)

# 그래프 세팅
xdata, ydata = [], []
start_time = time.time()

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_ylim(0, 1)  # 예상 파워 범위에 따라 조정 (예: 0 ~ 5W)
ax.set_xlim(0, 10)
ax.set_xlabel("Time (s)")
ax.set_ylabel("Power (W)")
ax.set_title("Live Power Reading from PM101")



def update(frame):
    current_time = time.time() - start_time
    power = c_double()
    ret = tlpm.TLPM_measPower(instr.value, byref(power))
    if ret == 0:
        xdata.append(current_time)
        ydata.append(power.value)
        if current_time > ax.get_xlim()[1] - 1:
            ax.set_xlim(0, current_time + 5)
        ax.set_ylim(min(ydata) * 0.9, max(ydata) * 1.1)
        line.set_data(xdata, ydata)
        time.sleep(0.1)
    return line,

ani = animation.FuncAnimation(fig, update, interval=200)
plt.show()

tlpm.TLPM_close(instr.value)