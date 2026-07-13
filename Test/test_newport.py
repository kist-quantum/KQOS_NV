import sys
import os
import time
import numpy as np
import matplotlib.pyplot as plt
# 현재 파일 기준 상위 폴더를 찾아서 sys.path에 추가
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))  # Folder까지 이동
sys.path.append(parent_dir)

save_dir = r"C:\Users\oprs1\Desktop\이한빛\newport_data"


from Drivers.wlm_client import WLMProducer
from Drivers.newport import newport
wlm = WLMProducer("192.168.0.7",65432)
device = newport(4106,"6700 SN22500008")
device.connected = 1
w = 637
pzt_array=np.arange(0,95.05,0.1)
plt.figure()
while w < 637.13:
    device.lbd = w
    device.pzt = 0
    time.sleep(10)
    i=0
    wl_array=[]
    while float(device.get_piezo_voltage()) < 95.02 :
        time.sleep(0.05)
        print(device.pzt)
        wlm.WL_from_server(1)
        wl=wlm.get_WL(1)
        #if wl<630 :
        #    wl = wl1 
        #wl1=wl
        wl_array.append(wl)
        i+=0.1
        device.pzt = i
    plt.plot(pzt_array,wl_array)
    file_base = f"72mA_scan_{w:.2f}nm_2"
    data = np.column_stack((pzt_array, wl_array))
    np.savetxt(os.path.join(save_dir, file_base + ".dat"),data, header="piezo(%)   wavelength(nm)",fmt="%.5f")
    w+=0.05
device.connected = 0

plt.title("Wavelength scan vs piezo")
plt.xlabel("piezo(%)")
plt.ylabel("wave length(nm)")
plt.tight_layout()
file_base1 = f"72mA_scan_2"
plt.savefig(os.path.join(save_dir, file_base1 + ".png"))
plt.show()


# pzt_array_1=pzt_array[640:901]
# pzt_array_2=pzt_array[1440:1761]
# wl_array_1=wl_array[640:901]
# wl_array_2=wl_array[1440:1761]
# plt.subplot(1,2,1)
# plt.plot(pzt_array_1,wl_array_1)
# plt.title("pzt-wl ratio")
# plt.xlabel("piezo(%)")
# plt.ylabel("wave length(nm)")
# plt.subplot(1,2,2)
# plt.plot(pzt_array_2,wl_array_2)
# plt.title("pzt-wl ratio")
# plt.xlabel("piezo(%)")
# plt.ylabel("wave length(nm)")
# plt.show()
