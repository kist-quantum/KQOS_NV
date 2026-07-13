import sys
import os

# 현재 파일 기준 상위 폴더를 찾아서 sys.path에 추가
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))  # Folder까지 이동
sys.path.append(parent_dir)

# 이제 절대 경로 import 사용 가능
from Drivers.AMC_API.python import AMC  # 예제: 패키지 경로에 맞게 변경

device = AMC.Device("192.168.0.145")
device.connect()
print(device.control.getControlAmplitude(0))
device.move.writeNSteps(0, 1)
device.move.performNSteps(axis = 0, backward = False)
print(device.move.getPosition(0))
device.close()