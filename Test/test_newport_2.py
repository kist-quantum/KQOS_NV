import sys
import os
import time
import numpy as np
import matplotlib.pyplot as plt
# 현재 파일 기준 상위 폴더를 찾아서 sys.path에 추가
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))  # Folder까지 이동
sys.path.append(parent_dir)


from Drivers.wlm_client import WLMProducer
from Drivers.newport import newport
wlm = WLMProducer("192.168.0.7",65432)
device = newport(4106,"6700 SN22500008")
device.connected = 1
device.lbd = 637.05
device.pzt = 0
time.sleep(10)
i=0
t=0
time_array=np.arange(0,200.05,0.1)
wl_array=[]

while float(device.get_piezo_voltage()) < 39.6 :
    time.sleep(0.2)
    i+=0.5
    device.pzt = i
    print(device.pzt)
time.sleep(0.2)

while (t < 200.005) :
    wlm.WL_from_server(1)
    wl=wlm.get_WL(1)
    wl_array.append(wl)
    t+=0.1
    print(t)
    time.sleep(0.1)

device.connected = 0

plt.plot(time_array,wl_array)
plt.title("time-wl ratio when piezo = 30%")
plt.xlabel("time(s)")
plt.ylabel("wave length(nm)")

plt.show()