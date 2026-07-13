from Drivers.RFSoC import RFSoC
from Drivers.DLC import DLCcontrol
from Drivers.wlm_client import WLMProducer
from Drivers.newport import newport
from Drivers.elliptec import ElliptecRotationStage
import numpy as np
import pandas as pd
from PySide6.QtGui import QPixmap, QIcon
import time
from Functions.utils import *
import os, logging, toml
from Functions.canvas.canvas_1D import *
from Functions.canvas.canvas_2D import *
# from Functions.utils import LASER_ON_CONFIG
import pyqtgraph as pg
from pyqtgraph.Qt import QtWidgets

class resonant:
    def __init__(self, ui, soc: RFSoC, wlm_client:WLMProducer, newport:newport, DLC1:DLCcontrol, DLC2:DLCcontrol):
        self.ui = ui
        self.soc = soc
        self.wlm_client = wlm_client
        self.newport = newport
        self.DLC1 = DLC1
        self.DLC2 = DLC2
        self.flag1 = Flag()
        self.flag2 = Flag()

        self.flag_PLE = Flag()
        self.flag_wl_scan = Flag()

        self.flag_laser_lock_1 = Flag()
        self.flag_laser_lock_2 = Flag()

        self.flag_PLE_repeat = Flag()

        self.flag_PLE_repeat_Pol = Flag()
        

        self.canvas_PLE = canvas_1D(self)
        self.ui.horizontalLayout_PLE_count.addWidget(self.canvas_PLE)
        self.canvas_WLscan = canvas_1D(self)
        self.ui.horizontalLayout_wavelength.addWidget(self.canvas_WLscan)

        self.wl_update_loop_thread = threading.Thread(target = self.wl_update_loop, daemon = True,)

    def init_PLE_params(self):
        self.stopping = False
        self.flag_PLE.clear()
        filepath = f'Configs/PLE.toml'
        with open(filepath, 'r') as f:
            self.config = toml.load(f)
        f.close()
        self.soc_config = {
            'command': 'PLE'
        }
        for key in self.config['soc'].keys():
            self.soc_config[key] = self.config['soc'][key]

        if self.ui.radioButton_PLE_CH1.isChecked():
            self.config['soc']['red_ch'] = self.CH1_mw_ch
            self.device = self.CH1_device
        elif self.ui.radioButton_PLE_CH2.isChecked():
            self.config['soc']['red_ch'] = self.CH2_mw_ch
            self.device = self.CH2_device
        self.PLE_step = float(self.ui.lineEdit_PLE_step.text())
        self.cnt1_temp = 0
        self.cnt2_temp = 0
        self.PLE_count_array = np.array([])
        self.PLE_axis_array = np.array([])
        
    def pressed_connect_CH1(self):
        if self.ui.pushButton_CH1_connect.text() == "Connect":
            CH1_txt = self.ui.comboBox_laser_CH1.currentText()
            self.CH1_WLM_ch = int(self.ui.comboBox_WLM_ch1.currentText())
            self.flag1.clear()
            try:
                if CH1_txt == "Newport":
                    self.CH1_device = self.newport
                    self.CH1_mw_ch = '5'
                elif CH1_txt == "DLC1":
                    self.CH1_device = self.DLC1
                    self.CH1_mw_ch = '1'
                elif CH1_txt == "DLC2":
                    self.CH1_device = self.DLC2
                    self.CH1_mw_ch = '2'
                self.ui.pushButton_laserlock_button_1.setEnabled(True)
                self.ui.pushButton_change_wavelength_1.setEnabled(True)
                self.ui.pushButton_CH1_connect.setText("Disconnect")
                self.thread1 = threading.Thread(
                    target=self.show_WL, 
                    args=(1,self.CH1_WLM_ch,),
                    daemon = True,)
                self.thread1.start()
            except:
                logging.error("connecting device failed" + CH1_txt)
            

        elif self.ui.pushButton_CH1_connect.text() == "Disconnect":
            self.CH1_device = None
            self.flag1.set()
            self.ui.pushButton_laserlock_button_1.setEnabled(False)
            self.ui.pushButton_change_wavelength_1.setEnabled(False)
            self.ui.pushButton_CH1_connect.setText("Connect")
    
    def pressed_connect_CH2(self):
        if self.ui.pushButton_CH2_connect.text() == "Connect":
            CH2_txt = self.ui.comboBox_laser_CH2.currentText()
            self.CH2_WLM_ch = int(self.ui.comboBox_WLM_ch2.currentText())
            self.flag2.clear()
            try:
                if CH2_txt == "Newport":
                    self.CH2_device = self.newport
                    self.CH2_mw_ch = '5'
                elif CH2_txt == "DLC1":
                    self.CH2_device = self.DLC1
                    self.CH2_mw_ch = '1'
                elif CH2_txt == "DLC2":
                    self.CH2_device = self.DLC2
                    self.CH2_mw_ch = '2'
                self.ui.pushButton_laserlock_button_2.setEnabled(True)
                self.ui.pushButton_change_wavelength_2.setEnabled(True)
                self.ui.pushButton_CH2_connect.setText("Disconnect")
                self.thread2 = threading.Thread(
                    target=self.show_WL, 
                    args=(2,self.CH2_WLM_ch,),
                    daemon = True,)
                self.thread2.start()
            except:
                logging.error("connecting device failed" + CH2_txt)

        elif self.ui.pushButton_CH2_connect.text() == "Disconnect":
            self.CH2_device = None
            self.flag2.set()
            self.ui.pushButton_laserlock_button_2.setEnabled(False)
            self.ui.pushButton_change_wavelength_2.setEnabled(False)
            self.ui.pushButton_CH2_connect.setText("Connect")
    
    def pressed_change_wl_CH1(self): # 수정 예정
        target_WL = self.ui.lineEdit_changeWL_CH1.text()
        try:
            target_WL = float(target_WL)
        except:
            logging.error("lineEdit_lambda_1 has insufficient variable")
        self.CH1_device.pzt = 0
        self.CH1_device.lbd = float(target_WL)

    def show_WL(self, device_ch, wl_ch):
        if not self.wl_update_loop_thread.is_alive():
            self.wl_update_loop_thread.start()
        if device_ch == 1:
            while not self.flag1.is_set():
                time.sleep(0.3)
                self.curr_wl_ch1 = self.wlm_client.wl_from_wlmList(int(wl_ch))
                self.ui.label_CH1_curr_WL.setText(str(self.curr_wl_ch1))

        elif device_ch == 2:
            while not self.flag2.is_set():
                time.sleep(0.3)
                self.curr_wl_ch2 = self.wlm_client.wl_from_wlmList(int(wl_ch))
                self.ui.label_CH2_curr_WL.setText(str(self.curr_wl_ch2))

    def wl_update_loop(self):
        while True:
            self.wlm_client.WL_from_server()
            time.sleep(0.2)

    def pressed_laserLock_CH1(self):
        if self.ui.pushButton_laserlock_button_1.text() == "laser lock":
            target_WL = float(self.ui.lineEdit_laserLock_CH1.text())
            laserlock1_thread = threading.Thread(
                    target=self.laserLock,
                    args=(target_WL, self.CH1_device, self.flag_laser_lock_1, 1),
                    daemon=True,
                )
            self.flag_laser_lock_1.clear()
            laserlock1_thread.start()
            self.ui.pushButton_laserlock_button_1.setText("halt laser lock")
            
        elif self.ui.pushButton_laserlock_button_1.text() == "halt laser lock":
            self.flag_laser_lock_1.set()
            self.ui.pushButton_laserlock_button_1.setText("laser lock")

    def pressed_laserLock_CH2(self):
        if self.ui.pushButton_laserlock_button_2.text() == "laser lock":
            target_WL = float(self.ui.lineEdit_laserLock_CH2.text())
            laserlock2_thread = threading.Thread(
                    target=self.laserLock,
                    args=(target_WL, self.CH2_device, self.flag_laser_lock_2, 2),
                    daemon=True,
                )
            self.flag_laser_lock_2.clear()
            laserlock2_thread.start()
            self.ui.pushButton_laserlock_button_2.setText("halt laser lock")

        elif self.ui.pushButton_laserlock_button_2.text() == "halt laser lock":
            self.flag_laser_lock_2.set()
            self.ui.pushButton_laserlock_button_2.setText("laser lock")

    def laserLock(self, target_WL, device, flag_laser_lock, CH_N):
        weight = 100
        diff_threshold = 2e-5
        while not flag_laser_lock:
            if CH_N == 1:
                wl_temp = float(self.curr_wl_ch1)
            elif CH_N == 2:
                wl_temp = float(self.curr_wl_ch2)
            difference = target_WL - float(wl_temp)


            if device.get_device_info() == "newport":
                if abs(difference) > diff_threshold and difference > 0:
                    target_pzt = float(device.pzt) + max(weight * difference, 0.01)
                    device.pzt = target_pzt
                elif abs(difference) > diff_threshold and difference < 0:
                    target_pzt = float(device.pzt) + min(weight * difference, -0.01)
                    device.pzt = target_pzt
                else:
                    time.sleep(5)
                    continue
            elif device.get_device_info() == "DLC":
                _, curr_pzt = device.get_piezo_voltage()
                if abs(difference) > diff_threshold and difference < 0:
                        target_pzt = float(curr_pzt) + max(-1*weight * difference*2, 0.01)
                        device.set_piezo_voltage(target_pzt)
                elif abs(difference) > diff_threshold and difference > 0:
                    target_pzt = float(curr_pzt) + min(-1*weight * difference*2, -0.01)
                    device.set_piezo_voltage(round(target_pzt, 2))
                else:
                    time.sleep(5)
                    continue
                
            time.sleep(1)
        
    def pressed_PLE_start(self):
        if self.ui.pushButton_PLE_start.text() == "Start":
            self.init_PLE_params()
            PLE_exp_thread = threading.Thread(
                target=self.PLE_start,
                daemon=True,
            )
            PLE_exp_thread.start()
            self.ui.pushButton_PLE_start.setText("Stop")
        elif self.ui.pushButton_PLE_start.text() == "Stop":
            self.flag_PLE.set()
            self.ui.pushButton_PLE_start.setText("Start")

    def pressed_PLE_repeat(self, flag_PLE_repeat):
        if self.ui.pushButton_PLE_repeat.text() == "Start":
            self.experice_PLE_repeat = threading.Thread(target=self.start_PLE_repeat, daemon = True,)
            self.experice_PLE_repeat.start()
            self.ui.pushButton_PLE_repeat.setText("Stop")

        elif self.ui.pushButton_PLE_repeat.text() == "Stop":
            self.flag_PLE_repeat.set()
            self.ui.pushButton_PLE_repeat.setText("Start")

    def start_PLE_repeat(self):
        filepath = f'Configs/Laser_config.toml'
        with open(filepath, 'r') as f:
            self.green_config = toml.load(f)
        f.close()
        self.green_on_config = {
            'command': 'laser_on'
        }
        for key in self.green_config['green_laser'].keys():
            self.green_on_config[key] = self.green_config['green_laser'][key]
        self.soc.send(self.green_on_config)

        for i in range(iter):
            self.soc.send(self.green_on_config)
            self.PLE_start()
    
    #Repeat polarization change PLE
    def pressed_PLE_repeat_Pol(self):
        if self.ui.pushButton_PLE_repeat_Pol.text() == "Start":
            self.experice_PLE_repeat_Pol = threading.Thread(target=self.start_PLE_repeat_Pol, daemon = True,)
            self.experice_PLE_repeat_Pol.start()
            self.ui.pushButton_PLE_repeat_Pol.setText("Stop")

        elif self.ui.pushButton_PLE_repeat_Pol.text() == "Stop":
            self.flag_PLE_repeat_Pol.set()
            self.ui.pushButton_PLE_repeat_Pol.setText("Start")

    def start_PLE_repeat_Pol(self):
        filepath = f'Configs/Laser_config.toml'
        with open(filepath, 'r') as f:
            self.green_config = toml.load(f)


    def PLE_start(self):
        self.init_PLE_params()
        PLE_start = float(self.ui.lineEdit_PLE_start.text())
        PLE_end = float(self.ui.lineEdit_PLE_end.text())
        self.canvas_PLE.axes.clear()
        difference = 1
        diff_threshold = 1e-5

        while not self.flag_PLE.is_set() and abs(difference) > diff_threshold :
            difference = PLE_start - float(self.PLE_wl)
            weight = 20
            if self.device.get_device_info() == "newport":
                    if abs(difference) > diff_threshold and difference > 0:
                        target_pzt = float(self.device.pzt) + max(weight * difference, 0.01)
                        self.device.pzt = round(target_pzt, 2)
                    elif abs(difference) > diff_threshold and difference < 0:
                        target_pzt = float(self.device.pzt) + min(weight * difference, -0.01)
                        self.device.pzt = round(target_pzt, 2)
            elif self.device.get_device_info() == "DLC":
                _, curr_pzt = self.device.get_piezo_voltage()
                if abs(difference) > diff_threshold and difference < 0:
                        target_pzt = float(curr_pzt) + max(-1*weight * difference*2, 0.01)
                        self.device.set_piezo_voltage(target_pzt)
                elif abs(difference) > diff_threshold and difference > 0:
                    target_pzt = float(curr_pzt) + min(-1*weight * difference*2, -0.01)
                    self.device.set_piezo_voltage(round(target_pzt, 2))
            time.sleep(1)

        while self.PLE_wl < PLE_end:
            # shutdown
            if self.flag_PLE.is_set():
                break
            if self.device.get_device_info() == "newport":
                target_pzt = float(self.device.pzt) + self.PLE_step
            elif self.device.get_device_info() == "DLC":
                _, curr_pzt = self.device.get_piezo_voltage()
                target_pzt = float(curr_pzt) - self.PLE_step
            self.device.set_piezo_voltage(target_pzt)
            time.sleep(1)
            self.soc.send(self.soc_config)
            self.soc.recv()
            PLE_count = self.soc.getCount0() * 1e6 / (self.soc_config['reps'] * self.soc_config['ro_len'])

            self.PLE_count_array = np.append(self.PLE_count_array, PLE_count)
            self.PLE_axis_array = np.append(self.PLE_axis_array, self.PLE_wl)

            self.canvas_PLE.axes.scatter(self.PLE_axis_array, self.PLE_count_array, c = 'red')
            self.canvas_PLE.draw()

        self.save()


    def init_WL_scan_params(self):
        self.WL_scan_array = np.array([])
        self.WL_axis_array = np.array([])
        self.flag_wl_scan.clear()
        self.canvas_WLscan.axes.clear()

    def pressed_WL_scan_start(self):
        if self.ui.pushButton_wavelength_scan_start.text() == "Start":
            start_voltage = float(self.ui.lineEdit_WL_start_voltage.text())
            end_voltage = float(self.ui.lineEdit_WL_end_voltage.text())
            voltage_step = float(self.ui.lineEdit_WL_step_size.text())
            self.init_WL_scan_params()

            if self.ui.radioButton_WL_scan_CH1.isChecked():
                device = self.CH1_device
                self.scan_ch = self.CH1_WLM_ch
            elif self.ui.radioButton_WL_scan_CH2.isChecked():
                device = self.CH2_device
                self.scan_ch = self.CH2_WLM_ch

            wl_scan_thread = threading.Thread(
                target=self.start_wavelength_scan,
                daemon=True,
                args=(start_voltage, end_voltage, voltage_step, device, ),
            )
            self.ui.pushButton_wavelength_scan_start.setText("Stop")
            wl_scan_thread.start()

        elif self.ui.pushButton_wavelength_scan_start.text() == "Stop":
            self.flag_wl_scan.set()
            self.ui.pushButton_wavelength_scan_start.setText("Start")
        
    def start_wavelength_scan(self, start, end, step, device):
        device.set_piezo_voltage(start)
        time.sleep(3)
        array_voltage = np.arange(start, end, step, dtype = float)
        print(array_voltage)
        for curr_voltage in array_voltage:
            if self.flag_wl_scan.is_set():
                break
            device.set_piezo_voltage(curr_voltage)
            time.sleep(2)
            wl = self.wlm_client.wl_from_wlmList(self.scan_ch)
            self.WL_scan_array = np.append(self.WL_scan_array, wl)
            self.WL_axis_array = np.append(self.WL_axis_array, curr_voltage)

            self.canvas_WLscan.axes.scatter(self.WL_axis_array, self.WL_scan_array, c = 'red')
            self.canvas_WLscan.draw()
        self.ui.pushButton_wavelength_scan_start.setText("Start")

    def pressed_view_local(self):
        self.left_axis = float(self.ui.lineEdit_view_left.text())
        self.right_axis = float(self.ui.lineEdit_view_right.text())

        self.temp_PLE_axis_array = self.PLE_axis_array[np.where((self.PLE_axis_array > self.left_axis) & (self.PLE_aixs_array < self.right_axis))]
        print(self.temp_PLE_axis_array)
        
        self.canvas_PLE
        self.local_x

    #red gain control
    def adjust_red_gain(self):
        self.soc_config['red_gain'] = int(self.ui.lineEdit_red_gain.text())
    
    def save(self):
        path = f'{FILEPATH}/PLE/{time.strftime("%Y%m%d")}/'

        try:
            os.mkdir(path)
        except Exception:
            None
    
        # add self.experiment for identifying experiment
        filename = 'PLE' + '_' + time.strftime("%H") + '시' + time.strftime("%M") + '분' + \
                            time.strftime("%S") + '초'
                            
        np.savez(f'{path}/{filename}', Wavelength=self.PLE_axis_array, count=self.PLE_count_array, )
        self.canvas_PLE.fig.savefig(f'{path}/{filename}')
        
        # save as csv
        df = pd.DataFrame({'Wavelength' : self.PLE_axis_array,'count' : self.PLE_count_array})
        df.to_csv(f'{path}/{filename}.csv')
        
    @property
    def PLE_wl(self):
        """
        Real-time property to get the current wavelength based on the selected channel.
        """
        if self.ui.radioButton_PLE_CH1.isChecked():
            return self.curr_wl_ch1
        elif self.ui.radioButton_PLE_CH2.isChecked():
            return self.curr_wl_ch2
        return None

class Flag(threading.Event):
    """A wrapper for the typical event class to allow for overriding the
    `__bool__` magic method, since it looks nicer.
    """

    def __bool__(self):
        return self.is_set()