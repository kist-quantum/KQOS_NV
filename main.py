import sys
import matplotlib
matplotlib.use('Qt5Agg')  # Use Qt5Agg backend to avoid OLE issues
import matplotlib.pyplot as plt

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from UI_files.main_window import MainWindow
from UI_files.event_handler import event_handler
from Drivers.ZCU import *
from Drivers.PI import PI
from Drivers.Zaber_z import Zaber_z
from Drivers.KST101 import KST101
from Drivers.BSC203 import BSC203
from Drivers.wlm_client import WLMProducer
from Drivers.Actuator_piezo import actuator
from Drivers.newport import newport
from Drivers.DLC import DLCcontrol
from Drivers.AMC300 import AMC300
# from Drivers.elliptec import ElliptecRotationStage
from Functions.counter import counter
from Functions.confocal import confocal
from Functions.resonant import resonant
from Functions.spin_control import spin_control
from Functions.T1_sensing import T1_sensing
from Functions.B_align import B_align
from Functions.entanglement import entanglement
from Functions.utils import *
from Functions.device_config import *

plt.rcParams["font.size"] = 12
plt.rcParams["xtick.color"] = "White"
plt.rcParams["ytick.color"] = "White"

# Funcitons->utils에서 측정 결과 저장할 경로 지정하고 사용하세요.

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    ui = window.ui
    
    equips = {
        'FPGA': ZCU_111(ip=SERVER_IP, port=SERVER_PORT),
        'E-727': PI(ip=E727_IP, port=E727_PORT),
        'Zaber': Zaber_z(ip = ZABER_IP, port = ZABER_PORT),
        'wlm_client': WLMProducer(ip = LT1_IP, port = LT1_PORT),
        'actuator_red':actuator(id = ACTUATOR_ID_RED),
        'actuator_zpl':actuator(id = ACTUATOR_ID_ZPL),
        'newport':newport(id = NEWPORT_ID, key = NEWPORT_KEY),
        'DLCcontrol1':DLCcontrol(ip = TOPTICA1_IP),
        'DLCcontrol2':None,#DLCcontrol(ip = TOPTICA2_IP),
        'BSC203': BSC203(serial_N=BSC_203_N)
    }

    basic_funcs = {
        'confocal': confocal(ui, equips['FPGA'], equips['E-727'], equips['Zaber'], equips['actuator_red'],equips['actuator_zpl'], ),
        'B_align': B_align(ui, equips['FPGA'], equips['BSC203']),
    }
    
    funcs = {
        'spin_control': spin_control(ui, equips['FPGA'], equips['E-727'], equips['Zaber']),
        'resonant': resonant(ui, equips['FPGA'], equips['wlm_client'], equips['newport'], equips['DLCcontrol1'], equips['DLCcontrol2']),
        'entanglement' : entanglement(ui, equips['FPGA'])
    }
    
    ui_event = event_handler(ui, basic_funcs, funcs)
    sys.exit(app.exec())