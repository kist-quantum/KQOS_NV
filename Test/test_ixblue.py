import serial
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque

# 시리얼 설정
ser = serial.Serial(
    port='COM6',
    baudrate=115200,
    stopbits=serial.STOPBITS_ONE,
    parity=serial.PARITY_NONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

def send_command(cmd):
    ser.write((cmd + '\r').encode())
    time.sleep(0.02)
    response = ser.readline().decode().strip()
    return response

def read_bias_voltage():
    try:
        return float(send_command("BV?"))
    except:
        return None

def read_pg_gain():
    try:
        return float(send_command("PG?"))
    except:
        return None

# 데이터 버퍼 설정
MAX_POINTS = 100
x_data = deque(maxlen=MAX_POINTS)
bv_data = deque(maxlen=MAX_POINTS)
pg_data = deque(maxlen=MAX_POINTS)

start_time = time.time()

def update_plot(frame):
    current_time = time.time() - start_time
    bv = read_bias_voltage()
    pg = read_pg_gain()

    if bv is not None and pg is not None:
        x_data.append(current_time)
        bv_data.append(bv)
        pg_data.append(pg)

        line_bv.set_data(x_data, bv_data)
        line_pg.set_data(x_data, pg_data)

        ax1.relim()
        ax1.autoscale_view()

        ax2.relim()
        ax2.autoscale_view()

    return line_bv, line_pg

# 그래프 초기화
fig, ax1 = plt.subplots()

# 왼쪽 Y축 (Bias Voltage)
line_bv, = ax1.plot([], [], label="Bias Voltage (mV)", color='tab:blue', lw=2)
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Bias Voltage (mV)", color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')
ax1.grid(True)

# 오른쪽 Y축 (Photodiode Gain)
ax2 = ax1.twinx()
line_pg, = ax2.plot([], [], label="Photodiode Gain (PG)", color='tab:orange', lw=2)
ax2.set_ylabel("Photodiode Gain", color='tab:orange')
ax2.tick_params(axis='y', labelcolor='tab:orange')

# 제목
plt.title("Real-Time Bias Voltage & Photodiode Gain")

# 애니메이션 시작
ani = animation.FuncAnimation(fig, update_plot, interval=100)
plt.show()

# 종료 시 포트 닫기
try:
    plt.show()
except KeyboardInterrupt:
    print("Stopped by user.")
    ser.close()
