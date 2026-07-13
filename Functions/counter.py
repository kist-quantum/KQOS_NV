from Drivers.RFSoC import RFSoC
import numpy as np
from PySide6.QtGui import QPixmap, QIcon
import threading
import time
from Drivers.Actuator_piezo import *
from Functions.utils import *
import os
from Functions.canvas.canvas_1D import *
# from Functions.utils import LASER_ON_CONFIG
import toml

class counter:
    def __init__(self, ui, soc: RFSoC, actuator = actuator):
        self.ui = ui
        self.soc = soc
    #     self.actuator = actuator
    #     self.canvas = canvas_1D(self)
    #     self.ui.counter_layout.addWidget(self.canvas)
    #     self.complete = threading.Event()

    #     pixmap = QPixmap('UI_files/images/icons/cil-smile.png')
    #     self.smile_icon = QIcon()
    #     self.smile_icon.addPixmap(pixmap)
    #     pixmap = QPixmap('UI_files/images/icons/cil-frown.png')
    #     self.frown_icon = QIcon()
    #     self.frown_icon.addPixmap(pixmap)
        
    #     pixmap = QPixmap('UI_files/images/icons/cil-media-play.png')
    #     self.start_icon = QIcon()
    #     self.start_icon.addPixmap(pixmap)
    #     pixmap = QPixmap('UI_files/images/icons/cil-media-stop.png')
    #     self.stop_icon = QIcon()
    #     self.stop_icon.addPixmap(pixmap)
    #     self.counter_init_params()
        
    # def pushButton_laser(self):
    #     filepath = f'Configs/Laser_config.toml'
    #     with open(filepath, 'r') as f:
    #         self.config = toml.load(f)
    #     f.close()
    #     self.soc_config = {
    #         'command': 'laser_on'
    #     }

    #     if self.ui.counter_laser_on_4.text() == ' Green Laser on':
    #         for key in self.config['green_laser'].keys():
    #             self.soc_config[key] = self.config['green_laser'][key]
    #         self.soc.send(self.soc_config)
    #         self.ui.counter_laser_on_4.setText(' Green Laser off')
    #     else:
    #         self.soc.send({'command': 'laser_off'})
    #         self.ui.counter_laser_on_4.setText(' Green Laser on')
    
    # def pushButton_red1_laser(self):
    #     filepath = f'Configs/Laser_config.toml'
    #     with open(filepath, 'r') as f:
    #         self.config = toml.load(f)
    #     f.close()
    #     self.soc_config = {
    #         'command': 'laser_on'
    #     }

    #     if self.ui.counter_laser_on_2.text() == ' Red 1 Laser on':
    #         for key in self.config['red1_laser'].keys():
    #             self.soc_config[key] = self.config['red1_laser'][key]
    #         self.soc.send(self.soc_config)
    #         self.ui.counter_laser_on_2.setText(' Red 1 Laser off')
            
    #     else:
    #         self.soc.send({'command': 'laser_off'})
    #         self.ui.counter_laser_on_2.setText(' Red 1 Laser on')
    
    # def pushButton_red2_laser(self):
    #     filepath = f'Configs/Laser_config.toml'
    #     with open(filepath, 'r') as f:
    #         self.config = toml.load(f)
    #     f.close()
    #     self.soc_config = {
    #         'command': 'laser_on'
    #     }
        
    #     if self.ui.counter_laser_on_3.text() == ' Red 2 Laser on':
    #         for key in self.config['red2_laser'].keys():
    #             self.soc_config[key] = self.config['red2_laser'][key]
    #         self.soc.send(self.soc_config)
    #         self.ui.counter_laser_on_3.setText(' Red 2 Laser off')
            
    #     else:
    #         self.soc.send({'command': 'laser_off'})
    #         self.ui.counter_laser_on_3.setText(' Red 2 Laser on')
        
    # def counter_init_params(self):
    #     self.complete.clear()
    #     self.start_time = time.time()
    #     self.cur_time = 0
    #     self.time_axis = np.array([])
    #     self.counts_history = np.array([])
    #     self.counts_display = np.array([])
    #     self.T_per_point = float(self.ui.counter_T_per_sec.text())
    #     self.T_trace = float(self.ui.counter_trace_length.text())
    #     self.laser_power = int(self.ui.counter_laser_power.text())
    #     self.confocal_config = {
    #         'command': 'confocal',
    #         'laser_ch': 5,
    #         'CNT1_memory': [0],
    #         'laser_power': self.laser_power,
    #         'reps': 1,
    #         'trig_qick_offset': 0.177,
    #         'ro_len': self.T_per_point * 1E+9
    #     }

    def count_start(self):
        if self.ui.counter_start.text() == ' Start':
            self.counter_init_params()
            thread_counter = threading.Thread(target=self.start_count)
            thread_counter.daemon = True
            thread_counter.start()
            self.ui.counter_start.setText(' Stop')
            self.ui.counter_start.setIcon(self.stop_icon)
        else:
            self.complete.set()
            self.ui.counter_start.setText(' Start')
            self.ui.counter_start.setIcon(self.start_icon)
            
    def start_count(self):
        while not self.complete.is_set():
            self.canvas.axes.clear()
            self.canvas.axes.grid()
            self.soc.send(self.confocal_config)
            self.soc.recv()
            
            self.counts_history = np.append(self.counts_history, self.soc.getCount0() / self.T_per_point / 1000)
            self.time_axis = np.append(self.time_axis, time.time() - self.start_time)
            
            val, time_axis_start_idx = find_nearest(self.time_axis, self.time_axis[-1] - self.T_trace)
            val, time_axis_end_idx = find_nearest(self.time_axis, self.time_axis[-1])
            
            if len(self.time_axis) > 1 and len(self.counts_history) > 1:
                self.canvas.axes.set_xlim(self.time_axis[-1] - self.T_trace, self.time_axis[-1])
                self.canvas.axes.set_ylim(np.min(self.counts_history[time_axis_start_idx:time_axis_end_idx]) * 0.9,\
                                    np.max(self.counts_history[time_axis_start_idx:time_axis_end_idx]) * 1.1)
                
                # self.canvas.axes.plot(self.time_axis, self.counts_history, color='#fe79c7', lw=2)
                self.canvas.axes.plot(self.time_axis, self.counts_history, color='coral', lw=2)
                self.ui.counter_counts.setText(str(self.counts_history[-1]))
                self.ui.counter_average_counts.setText(\
                    str(round(np.average(self.counts_history[time_axis_start_idx:time_axis_end_idx]), 2)))
                self.ui.counter_standard_deviation.setText(\
                    str(round(np.std(self.counts_history[time_axis_start_idx:time_axis_end_idx]), 2)))
                self.canvas.draw()

    def pushButton_autoAlign(self):
        if self.ui.pushButton_AutoAlign.text() == 'AutoAlign start':
            self.counter_init_params()
            stepSize = int(self.ui.counter_autoAlign_stepSize.text())
            thread_counter = threading.Thread(target=self.start_autoAlign, args=(stepSize, ))
            thread_counter.daemon = True
            thread_counter.start()
            self.ui.pushButton_AutoAlign.setText('AutoAlign stop')
            self.ui.pushButton_AutoAlign.setIcon(self.stop_icon)
        else:
            self.complete.set()
            self.ui.pushButton_AutoAlign.setText('AutoAlign start')
            self.ui.pushButton_AutoAlign.setIcon(self.start_icon)

    def start_autoAlign(self, stepSize):
        step_M1_x = stepSize
        step_M1_y = stepSize
        step_M2_x = stepSize
        step_M2_y = stepSize
        i = 0
        self.soc.send(self.confocal_config)
        self.soc.recv()
        self.counts_history = np.append(self.counts_history, self.soc.getCount0() / self.T_per_point / 1000)
        self.time_axis = np.append(self.time_axis, time.time() - self.start_time)
        while not self.complete.is_set():
            self.canvas.axes.clear()
            self.canvas.axes.grid()

            if i % 4 == 0:
                self.actuator.move_by(self.actuator.M1_x, step_M1_x)
                self.soc.send(self.confocal_config)
                self.soc.recv()
                self.counts_history = np.append(self.counts_history, self.soc.getCount0() / self.T_per_point / 1000)
                self.time_axis = np.append(self.time_axis, time.time() - self.start_time)
                if self.counts_history[-1] - self.counts_history[-2] < 0:
                    step_M1_x = step_M1_x * -1
                i = i + 1
            elif i % 4 == 1:
                self.actuator.move_by(self.actuator.M1_y, step_M1_y)
                self.soc.send(self.confocal_config)
                self.soc.recv()
                self.counts_history = np.append(self.counts_history, self.soc.getCount0() / self.T_per_point / 1000)
                self.time_axis = np.append(self.time_axis, time.time() - self.start_time)
                if self.counts_history[-1] - self.counts_history[-2] < 0:
                    step_M1_y = step_M1_y * -1
                i = i + 1
            elif i % 4 == 2:
                self.actuator.move_by(self.actuator.M2_x, step_M2_x)
                self.soc.send(self.confocal_config)
                self.soc.recv()
                self.counts_history = np.append(self.counts_history, self.soc.getCount0() / self.T_per_point / 1000)
                self.time_axis = np.append(self.time_axis, time.time() - self.start_time)
                if self.counts_history[-1] - self.counts_history[-2] < 0:
                    step_M2_x = step_M2_x * -1
                i = i + 1
            elif i % 4 == 3:
                self.actuator.move_by(self.actuator.M2_y, step_M2_y)
                self.soc.send(self.confocal_config)
                self.soc.recv()
                self.counts_history = np.append(self.counts_history, self.soc.getCount0() / self.T_per_point / 1000)
                self.time_axis = np.append(self.time_axis, time.time() - self.start_time)
                if self.counts_history[-1] - self.counts_history[-2] < 0:
                    step_M2_y = step_M2_y * -1
                i = i + 1

            
            val, time_axis_start_idx = find_nearest(self.time_axis, self.time_axis[-1] - self.T_trace)
            val, time_axis_end_idx = find_nearest(self.time_axis, self.time_axis[-1])
            
            if len(self.time_axis) > 1 and len(self.counts_history) > 1:
                self.canvas.axes.set_xlim(self.time_axis[-1] - self.T_trace, self.time_axis[-1])
                self.canvas.axes.set_ylim(np.min(self.counts_history[time_axis_start_idx:time_axis_end_idx]) * 0.9,\
                                    np.max(self.counts_history[time_axis_start_idx:time_axis_end_idx]) * 1.1)
                
                # self.canvas.axes.plot(self.time_axis, self.counts_history, color='#fe79c7', lw=2)
                self.canvas.axes.plot(self.time_axis, self.counts_history, color='coral', lw=2)
                self.ui.counter_counts.setText(str(self.counts_history[-1]))
                self.ui.counter_average_counts.setText(\
                    str(round(np.average(self.counts_history[time_axis_start_idx:time_axis_end_idx]), 2)))
                self.ui.counter_standard_deviation.setText(\
                    str(round(np.std(self.counts_history[time_axis_start_idx:time_axis_end_idx]), 2)))
                self.canvas.draw()

       
    def save(self):
        current_directory = os.getcwd()
        current_directory += '/Data/Counter/'
        try:
            os.mkdir(current_directory + time.strftime("%Y%m%d"))
        except Exception:
            pass
        current_directory += time.strftime("%Y%m%d")
        filename = '/' + time.strftime("%H") + '시' + time.strftime("%M") + '분' + \
                            time.strftime("%S") + '초'
        np.savez(current_directory+filename, ro_len=self.confocal_config['ro_len'], laser_power=self.confocal_config['laser_power'], \
            counts=self.counts_history)