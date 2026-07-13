from Drivers.RFSoC import RFSoC
from Drivers.PI import *
from Drivers.Zaber_z import Zaber_z
from PySide6.QtWidgets import QWidget, QFileDialog
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import threading
from PySide6.QtGui import QPixmap, QIcon
import os
from pipython import GCSDevice
from Functions.canvas.canvas_2D import *
from Functions.canvas.canvas_autofocus import *
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import time
from Functions.utils import FILEPATH
import toml
from Drivers.Actuator_piezo import *
from Functions.canvas.canvas_1D import *
from Functions.utils import *


class confocal:
    def __init__(self, ui, soc: RFSoC, stage: GCSDevice, Zaber: Zaber_z, actuator_red : actuator, actuator_zpl : actuator):
        self.ui = ui
        self.soc = soc
        self.stage = stage
        self.Zaber = Zaber
        self.actuator_red = actuator_red
        self.actuator_zpl = actuator_zpl
        self.canvas = canvas_1D(self)
        self.ui.counter_layout.addWidget(self.canvas)
        self.canvas_conofcal = canvas_2D(self)
        self.ui.confocal_layout.addWidget(self.canvas_conofcal)
        toolbar = NavigationToolbar(self.canvas_conofcal, self.ui.confocal_widget)
        self.ui.confocal_layout.addWidget(toolbar)
        self.canvas_autofocus = canvas_autofocus(self)
        self.ui.autofocus_layout.addWidget(self.canvas_autofocus)
        self.complete = threading.Event()

        self.counter_init_params()
        pos = self.stage.position()
        pos['z'] = self.Zaber.get_pos()
        self.ui.confocal_position_x.setText(str(pos['x']))
        self.ui.confocal_position_y.setText(str(pos['y']))
        self.ui.confocal_position_z.setText(str(round(self.Zaber.get_pos(), 3)))
        self.complete = threading.Event()
        self.auto_complete = threading.Event()
        self.init_params()
        self.complete.set()
        self.auto_complete.set()
        pixmap = QPixmap('UI_files/images/icons/cil-media-play.png')
        self.start_icon = QIcon()
        self.start_icon.addPixmap(pixmap)
        pixmap = QPixmap('UI_files/images/icons/cil-media-stop.png')
        self.stop_icon = QIcon()
        self.stop_icon.addPixmap(pixmap)
        pixmap = QPixmap('UI_files/images/icons/cil-smile.png')
        self.smile_icon = QIcon()
        self.smile_icon.addPixmap(pixmap)
        pixmap = QPixmap('UI_files/images/icons/cil-frown.png')
        self.frown_icon = QIcon()
        self.frown_icon.addPixmap(pixmap)
        pixmap = QPixmap('UI_files/images/icons/cil-media-play.png')
        self.start_icon = QIcon()
        self.start_icon.addPixmap(pixmap)
        pixmap = QPixmap('UI_files/images/icons/cil-media-stop.png')
        self.stop_icon = QIcon()
        self.stop_icon.addPixmap(pixmap)


        
    def init_params(self):
        self.complete.clear()
        self.vmax = 0
        self.pos = self.stage.position()
        self.x_pos = self.pos['x']
        self.y_pos = self.pos['y']
        self.z_pos = round(self.Zaber.get_pos(), 3)
        self.resolution = int(self.ui.confocal_resolution.text())
        self.x_fixed = self.ui.x_fix.isChecked()
        self.y_fixed = self.ui.y_fix.isChecked()
        self.z_fixed = self.ui.z_fix.isChecked()
        
        self.x_from = float(self.ui.confocal_from_x.text())
        self.x_to = float(self.ui.confocal_to_x.text())
        self.x_delta = (self.x_to - self.x_from) / (self.resolution)
        
        self.y_from = float(self.ui.confocal_from_y.text())
        self.y_to = float(self.ui.confocal_to_y.text())
        self.y_delta = (self.y_to - self.y_from) / (self.resolution)
        
        self.z_from = float(self.ui.confocal_from_z.text())
        self.z_to = float(self.ui.confocal_to_z.text())
        self.z_delta = (self.z_to - self.z_from) / (self.resolution)
        self.gerenate_axis()
        self.counts = np.zeros((self.resolution+1, self.resolution+1))
        self.positions = [[{'x':'0', 'y':'0', 'z':'0'} for _ in range(self.resolution+1)] for _ in range(self.resolution+1)]
        for index_y, y in enumerate(self.positions):
            for index_x, x in enumerate(y): 
                if self.z_fixed:
                    self.positions[index_y][index_x]['x'] = self.x_from + self.x_delta * index_x
                    self.positions[index_y][index_x]['y'] = self.y_from + self.y_delta * index_y
                    self.positions[index_y][index_x]['z'] = self.z_pos
                elif self.y_fixed:
                    self.positions[index_y][index_x]['x'] = self.x_from + self.x_delta * index_x
                    self.positions[index_y][index_x]['y'] = self.y_pos
                    self.positions[index_y][index_x]['z'] = self.z_from + self.z_delta * index_y
                else:
                    self.positions[index_y][index_x]['x'] = self.x_pos
                    self.positions[index_y][index_x]['y'] = self.y_from + self.y_delta * index_x
                    self.positions[index_y][index_x]['z'] = self.z_from + self.z_delta * index_y

        self.confocal_config = {
            'command': 'confocal',
            'laser_ch': 0,
            'laser_power': 35000,
            'reps': 1,
            'trig_qick_offset': 0.177,
            'ro_len': float(self.ui.confocal_T_per_point.text()) * 1E+9
        }
        if self.ui.radioButton_CW_ZPL.isChecked():
            self.confocal_config['CNT2_memory'] = [0]
        elif self.ui.radioButton_PUL_PSB_GR.isChecked():
            filepath = f'Configs/pulse_PSB_GR.toml'
            with open(filepath, 'r') as f:
                self.config = toml.load(f)
            f.close()
            self.confocal_config = {
                'command': 'pulse_PSB_GR'
            }
            for key in self.config['soc'].keys():
                self.confocal_config[key] = self.config['soc'][key]
        elif self.ui.radioButton_PUL_ZPL_GR.isChecked():
            filepath = f'Configs/pulse_ZPL_GR.toml'
            with open(filepath, 'r') as f:
                self.config = toml.load(f)
            f.close()
            self.confocal_config = {
                'command': 'pulse_ZPL_GR'
            }
            for key in self.config['soc'].keys():
                self.confocal_config[key] = self.config['soc'][key]
        else : 
            self.confocal_config['CNT1_memory'] = [0]

    def counter_init_params(self):
        self.complete.clear()
        self.start_time = time.time()
        self.cur_time = 0
        self.time_axis = np.array([])
        self.counts_history = np.array([])
        self.counts_display = np.array([])
        self.T_per_point = float(self.ui.counter_T_per_sec.text())
        self.AA_per_point = float(self.ui.counter_AA_per_sec.text())
        self.T_trace = float(self.ui.counter_trace_length.text())
        self.laser_power = int(self.ui.counter_laser_power.text())
        self.confocal_config = {
            'command': 'confocal',
            'laser_ch': 5,
            'laser_power': self.laser_power,
            'reps': 1,
            'trig_qick_offset': 0.177,
            'ro_len': self.T_per_point * 1E+9
        }
        if self.ui.radioButton_CW_ZPL.isChecked():
            self.confocal_config['CNT2_memory'] = [0]
        elif self.ui.radioButton_PUL_PSB_GR.isChecked():
            filepath = f'Configs/pulse_PSB_GR.toml'
            with open(filepath, 'r') as f:
                self.config = toml.load(f)
            f.close()
            self.confocal_config = {
                'command': 'pulse_PSB_GR'
            }
            for key in self.config['soc'].keys():
                self.confocal_config[key] = self.config['soc'][key]
        elif self.ui.radioButton_PUL_ZPL_GR.isChecked():
            filepath = f'Configs/pulse_ZPL_GR.toml'
            with open(filepath, 'r') as f:
                self.config = toml.load(f)
            f.close()
            self.confocal_config = {
                'command': 'pulse_ZPL_GR'
            }
            for key in self.config['soc'].keys():
                self.confocal_config[key] = self.config['soc'][key]
        else : 
            self.confocal_config['CNT1_memory'] = [0]
    
    def start(self):
        # print(self.ui.confocal_start.text())
        if self.ui.confocal_start.text() == 'Start':
            thread_confocal = threading.Thread(target=self.start_scan, name='confocal')
            thread_confocal.daemon = True
            thread_confocal.start()
            self.ui.confocal_start.setText('Stop') 
            self.ui.confocal_start.setIcon(self.stop_icon)
        else:
            self.complete.set()
            self.ui.confocal_start.setText('Start')
            self.ui.confocal_start.setIcon(self.start_icon)
        
    def start_scan(self):
        self.init_params()
        for i in range(0, self.resolution+1, 1):
            for j in range(0, self.resolution+1, 1):
                if self.complete.is_set():
                    return self.end()
                self.moveDelta_and_count(i, j)
            self.image = self.canvas_conofcal.axes.imshow(self.counts, cmap='magma')
            self.plot()
        self.end()
        
    def end(self):
        self.ui.confocal_start.setText('Start')
        self.ui.confocal_start.setIcon(self.start_icon)
        self.save()
    
    def plot(self) -> None:
        self.canvas_conofcal.axes.clear()

        if self.vmax == 0:
            self.image = self.canvas_conofcal.axes.imshow(self.counts, cmap='magma')
        else:
            max = np.min(self.counts)
            min = np.max(self.counts)
            self.ui.verticalSlider_2.setRange(max, min)
            self.ui.verticalSlider_2.setTickInterval(int((max - min) / 50))
            self.image = self.canvas_conofcal.axes.imshow(self.counts, cmap='magma', vmax=self.vmax)
        self.canvas_conofcal.axes.set_xlim(0, self.resolution)
        self.canvas_conofcal.axes.set_ylim(0, self.resolution)
        if self.z_fixed:
            self.canvas_conofcal.axes.set_xlabel('X axis')
            self.canvas_conofcal.axes.set_ylabel('Y axis')
        elif self.y_fixed:
            self.canvas_conofcal.axes.set_xlabel('X axis')
            self.canvas_conofcal.axes.set_ylabel('Z axis')
        else:
            self.canvas_conofcal.axes.set_xlabel('Y axis')
            self.canvas_conofcal.axes.set_ylabel('Z axis')
        self.canvas_conofcal.axes.set_xticks(self.real_row)
        self.canvas_conofcal.axes.set_yticks(self.real_col)
        self.canvas_conofcal.axes.set_xticklabels(self.row)
        self.canvas_conofcal.axes.set_yticklabels(self.column)
        self.canvas_conofcal.axes.tick_params(axis='both', labelsize=20)

        if self.canvas_conofcal.colorbar is not None:
            try:
                self.canvas_conofcal.colorbar.remove()
            except Exception as e:
                pass
        self.canvas_conofcal.divider = make_axes_locatable(self.canvas_conofcal.axes)
        self.canvas_conofcal.cax = self.canvas_conofcal.divider.append_axes("right", size='2%', pad=0.5)
        self.canvas_conofcal.colorbar = self.canvas_conofcal.fig.colorbar(self.image, cax=self.canvas_conofcal.cax)
        try:
            self.canvas_conofcal.draw()
        except Exception:
            pass
    
    def save(self) -> None:
        path = f'{FILEPATH}/Confocal/{time.strftime("%Y%m%d")}'
        try:
            os.makedirs(path, exist_ok = True)
        except Exception:
            None
        
        filename = time.strftime("%H") + '시' + time.strftime("%M") + '분' + \
                            time.strftime("%S") + '초' + ', '        
       
        if self.z_fixed:
            filename += 'z=' + str(self.Zaber.get_pos()) # get Zaber position
        elif self.y_fixed:
            filename += 'y=' + str(self.stage.position()['y'])
        else:
            filename += 'x=' + str(self.stage.position()['x'])
        
        np.savez(f'{path}/{filename}.npz', pos=self.positions, count=self.counts)
        pd.DataFrame(self.counts).to_csv(f'{path}/{filename}.csv', index = False, header = False)
        self.canvas_conofcal.fig.savefig(f'{path}/{filename}.png')
    
    def load(self):
        explorer = QWidget()
        filename = QFileDialog.getOpenFileName(explorer, 'Open File')
        
        data = np.load(filename[0], allow_pickle=True)
        if filename[0].find('x=') != -1:
            self.x_Fixed = True
            self.y_Fixed = False
            self.z_Fixed = False
        elif filename[0].find('y=') != -1:
            self.x_Fixed = False
            self.y_Fixed = True
            self.z_Fixed = False
        else:
            self.x_Fixed = False
            self.y_Fixed = False
            self.z_Fixed = True
        self.counts = data['count']
        self.positions = data['pos']
        self.x_from = float((self.positions[0][0]['x']))
        self.x_to = float((self.positions[-1][-1]['x']))
        self.y_from = float((self.positions[0][0]['y']))
        self.y_to = float((self.positions[-1][-1]['y']))
        self.z_from = float((self.positions[0][0]['z']))
        self.z_to = float((self.positions[-1][-1]['z']))
        self.resolution = len(self.positions) - 1
        self.gerenate_axis()
        self.plot()
    
    def gerenate_axis(self) -> None:
        self.row = []
        self.column = []
        self.lable_step = 5  # 축 label 갯수
        if self.z_fixed:
            for i in range(0, self.lable_step + 1, 1):
                self.row.append(round(self.x_from + i * (self.x_to - self.x_from) / self.lable_step, 2))
                self.column.append(round(self.y_from + i * (self.y_to - self.y_from) / self.lable_step, 2))
        elif self.y_fixed:
            for i in range(0, self.lable_step + 1, 1):
                self.row.append(round(self.x_from + i * (self.x_to - self.x_from) / self.lable_step, 2))
                self.column.append(round(self.z_from + i * (self.z_to - self.z_from) / self.lable_step, 2))
        elif self.x_fixed:
            for i in range(0, self.lable_step + 1, 1):
                self.row.append(round(self.y_from + i * (self.y_to - self.y_from) / self.lable_step, 2))
                self.column.append(round(self.z_from + i * (self.z_to - self.z_from) / self.lable_step, 2))
        self.real_row = []
        self.real_col = []
        for i in range(0, self.lable_step + 1, 1):
            self.real_row.append(i * self.resolution / self.lable_step)
            self.real_col.append(i * self.resolution / self.lable_step)

    def moveTo(self, x, y, z) -> tuple:
        pos = self.stage.moveTo(x, y)
        self.Zaber.move_absolute(z)
        pos['z'] = round(self.Zaber.get_pos(), 3)
        self.ui.confocal_position_x.setText(str(pos['x']))
        self.ui.confocal_position_y.setText(str(pos['y']))
        self.ui.confocal_position_z.setText(str(pos['z']))
        return pos

    def moveDelta_and_count(self, i, j) -> None:
        if self.z_fixed:
            self.positions[i][j] = self.moveTo(x=self.x_from + self.x_delta * j,\
                                    y=self.y_from + self.y_delta * i,\
                                    z=self.z_pos)
        elif self.y_fixed:
            self.positions[i][j] = self.moveTo(x=self.x_from + self.x_delta * j,\
                                    y=self.y_pos,\
                                    z=self.z_from + self.z_delta * i)
        else:
            self.positions[i][j] = self.moveTo(x=self.x_pos,\
                                    y=self.y_from + self.y_delta * j,\
                                    z=self.z_from + self.z_delta * i)
        self.soc.send(self.confocal_config)
        self.soc.recv()
        self.counts[i][j] = self.soc.getCount0() / self.confocal_config['ro_len'] * 1E+9 / 1000
        
    def moveDelta_and_red_count(self, i, j) -> None:
        if self.z_fixed:
            self.positions[i][j] = self.moveTo(x=self.x_from + self.x_delta * j,\
                                    y=self.y_from + self.y_delta * i,\
                                    z=self.z_pos)
        elif self.y_fixed:
            self.positions[i][j] = self.moveTo(x=self.x_from + self.x_delta * j,\
                                    y=self.y_pos,\
                                    z=self.z_from + self.z_delta * i)
        else:
            self.positions[i][j] = self.moveTo(x=self.x_pos,\
                                    y=self.y_from + self.y_delta * j,\
                                    z=self.z_from + self.z_delta * i)
        self.soc.send(self.confocal_config)
        self.soc.recv()
        self.counts[i][j] = self.soc.getCount0() / self.confocal_config['ro_len'] * 1E+9 / 1000         
        
    def go_home(self) -> None:
        self.moveTo(14, 14, 50)
    
    def pressedMove(self) -> None:
        for _ in range(3):
            self.moveTo(x=float(self.ui.confocal_set_position_x.text()),\
                        y=float(self.ui.confocal_set_position_y.text()),\
                        z=float(self.ui.confocal_set_position_z.text()))

    def slided(self):
        # try:
            self.vmax = self.ui.verticalSlider_2.value()
            self.plot()
        # except Exception:
        #     pass
   
    def x_fix(self) -> None:
        self.ui.x_fix.setChecked(True)
        self.ui.y_fix.setChecked(False)
        self.ui.z_fix.setChecked(False)
    def y_fix(self) -> None:
        self.ui.x_fix.setChecked(False)
        self.ui.y_fix.setChecked(True)
        self.ui.z_fix.setChecked(False)
    def z_fix(self) -> None:
        self.ui.x_fix.setChecked(False)
        self.ui.y_fix.setChecked(False)
        self.ui.z_fix.setChecked(True)
    
    def T_001(self):
        self.ui.autofocus_001.setChecked(True)
        self.ui.autofocus_005.setChecked(False)
        self.ui.autofocus_01.setChecked(False)
    def T_005(self):
        self.ui.autofocus_001.setChecked(False)
        self.ui.autofocus_005.setChecked(True)
        self.ui.autofocus_01.setChecked(False)
    def T_01(self):
        self.ui.autofocus_001.setChecked(False)
        self.ui.autofocus_005.setChecked(False)
        self.ui.autofocus_01.setChecked(True)
    
    def start_autofocus(self):
        if self.ui.autofocus_start.text() == 'Start':
            self.canvas_autofocus.complete.clear()
            self.thread_autofocus = threading.Thread(
                target=self.canvas_autofocus.start_scan, name='autofocus')
            self.thread_autofocus.daemon = True
            self.thread_autofocus.start()
            self.ui.autofocus_start.setText('Stop') 
            self.ui.autofocus_start.setIcon(self.stop_icon)
        else:
            self.canvas_autofocus.complete.set()
            self.ui.autofocus_start.setText('Start')
            self.ui.autofocus_start.setIcon(self.start_icon)
            self.thread_autofocus.join() 

    def pushButton_laser(self):
        filepath = f'Configs/Laser_config.toml'
        with open(filepath, 'r') as f:
            self.config = toml.load(f)
        f.close()
        self.soc_config = {
            'command': 'laser_on'
        }

        if self.ui.counter_laser_on.text() == 'Green Laser on':
            for key in self.config['green_laser'].keys():
                self.soc_config[key] = self.config['green_laser'][key]
            self.soc.send(self.soc_config)
            self.ui.counter_laser_on.setText('Green Laser off')
        else:
            self.soc.send({'command': 'laser_off'})
            self.ui.counter_laser_on.setText('Green Laser on')
    
    def pushButton_red1_laser(self):
        filepath = f'Configs/Laser_config.toml'
        with open(filepath, 'r') as f:
            self.config = toml.load(f)
        f.close()
        self.soc_config = {
            'command': 'laser_on'
        }

        if self.ui.counter_laser_on_2.text() == 'Red 1 Laser on':
            for key in self.config['red1_laser'].keys():
                self.soc_config[key] = self.config['red1_laser'][key]
            self.soc.send(self.soc_config)
            self.ui.counter_laser_on_2.setText('Red 1 Laser off')
            
        else:
            self.soc.send({'command': 'laser_off'})
            self.ui.counter_laser_on_2.setText('Red 1 Laser on')
    
    def pushButton_red2_laser(self):
        filepath = f'Configs/Laser_config.toml'
        with open(filepath, 'r') as f:
            self.config = toml.load(f)
        f.close()
        self.soc_config = {
            'command': 'laser_on'
        }
        
        if self.ui.counter_laser_on_3.text() == 'Red 2 Laser on':
            for key in self.config['red2_laser'].keys():
                self.soc_config[key] = self.config['red2_laser'][key]
            self.soc.send(self.soc_config)
            self.ui.counter_laser_on_3.setText('Red 2 Laser off')
            
        else:
            self.soc.send({'command': 'laser_off'})
            self.ui.counter_laser_on_3.setText('Red 2 Laser on')

    def counter_start(self):
        if self.ui.counter_start.text() == 'Start':
            self.counter_init_params()
            thread_counter = threading.Thread(target=self.start_count)
            thread_counter.daemon = True
            thread_counter.start()
            self.ui.counter_start.setText('Stop')
            self.ui.counter_start.setIcon(self.stop_icon)
        else:
            self.complete.set()
            self.ui.counter_start.setText('Start')
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

    def pushButton_autoAlign_red(self):
        if self.ui.pushButton_AutoAlign_red.text() == 'red AutoAlign start':
            self.counter_init_params()
            self.confocal_config['ro_len'] = self.AA_per_point * 1E+9
            stepSize = int(self.ui.counter_autoAlign_stepSize.text())
            thread_counter = threading.Thread(target=self.start_autoAlign_red, args=(stepSize, ))
            thread_counter.daemon = True
            thread_counter.start()
            self.ui.pushButton_AutoAlign_red.setText('red AutoAlign stop')
            self.ui.pushButton_AutoAlign_red.setIcon(self.stop_icon)
        else:
            self.complete.set()
            self.ui.pushButton_AutoAlign_red.setText('red AutoAlign start')
            self.ui.pushButton_AutoAlign_red.setIcon(self.start_icon)

    def start_autoAlign_red(self, stepSize):
        step_M1_x = stepSize
        step_M1_y = stepSize
        step_M2_x = stepSize
        step_M2_y = stepSize
        i = 0
        self.soc.send(self.confocal_config)
        self.soc.recv()
        self.counts_history = np.append(self.counts_history, self.soc.getCount0() / self.AA_per_point / 1000)
        self.time_axis = np.append(self.time_axis, time.time() - self.start_time)
        while not self.complete.is_set():
            self.canvas.axes.clear()
            self.canvas.axes.grid()

            if i % 4 == 0:
                self.actuator_red.move_by(self.actuator_red.M1_x, step_M1_x)
                self.soc.send(self.confocal_config)
                self.soc.recv()
                self.counts_history = np.append(self.counts_history, self.soc.getCount0() / self.AA_per_point / 1000)
                self.time_axis = np.append(self.time_axis, time.time() - self.start_time)
                if self.counts_history[-1] - self.counts_history[-2] < 0:
                    step_M1_x = step_M1_x * -1
                i = i + 1
            elif i % 4 == 1:
                self.actuator_red.move_by(self.actuator_red.M1_y, step_M1_y)
                self.soc.send(self.confocal_config)
                self.soc.recv()
                self.counts_history = np.append(self.counts_history, self.soc.getCount0() / self.AA_per_point / 1000)
                self.time_axis = np.append(self.time_axis, time.time() - self.start_time)
                if self.counts_history[-1] - self.counts_history[-2] < 0:
                    step_M1_y = step_M1_y * -1
                i = i + 1
            elif i % 4 == 2:
                self.actuator_red.move_by(self.actuator_red.M2_x, step_M2_x)
                self.soc.send(self.confocal_config)
                self.soc.recv()
                self.counts_history = np.append(self.counts_history, self.soc.getCount0() / self.AA_per_point / 1000)
                self.time_axis = np.append(self.time_axis, time.time() - self.start_time)
                if self.counts_history[-1] - self.counts_history[-2] < 0:
                    step_M2_x = step_M2_x * -1
                i = i + 1
            elif i % 4 == 3:
                self.actuator_red.move_by(self.actuator_red.M2_y, step_M2_y)
                self.soc.send(self.confocal_config)
                self.soc.recv()
                self.counts_history = np.append(self.counts_history, self.soc.getCount0() / self.AA_per_point / 1000)
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
    
    def pushButton_autoAlign_zpl(self):
        if self.ui.pushButton_AutoAlign_zpl.text() == 'zpl AutoAlign start':
            self.counter_init_params()
            self.confocal_config['ro_len'] = self.AA_per_point * 1E+9
            stepSize = int(self.ui.counter_autoAlign_stepSize.text())
            thread_counter = threading.Thread(target=self.start_autoAlign_zpl, args=(stepSize, ))
            thread_counter.daemon = True
            thread_counter.start()
            self.ui.pushButton_AutoAlign_zpl.setText('zpl AutoAlign stop')
            self.ui.pushButton_AutoAlign_zpl.setIcon(self.stop_icon)
        else:
            self.complete.set()
            self.ui.pushButton_AutoAlign_zpl.setText('zpl AutoAlign start')
            self.ui.pushButton_AutoAlign_zpl.setIcon(self.start_icon)

    def start_autoAlign_zpl(self, stepSize):
        step_M1_x = stepSize
        step_M1_y = stepSize
        step_M2_x = stepSize
        step_M2_y = stepSize
        i = 0
        self.soc.send(self.confocal_config)
        self.soc.recv()
        self.counts_history = np.append(self.counts_history, self.soc.getCount0() / self.AA_per_point / 1000)
        self.time_axis = np.append(self.time_axis, time.time() - self.start_time)
        while not self.complete.is_set():
            self.canvas.axes.clear()
            self.canvas.axes.grid()

            if i % 4 == 0:
                self.actuator_zpl.move_by(self.actuator_zpl.M1_x, step_M1_x)
                self.soc.send(self.confocal_config)
                self.soc.recv()
                self.counts_history = np.append(self.counts_history, self.soc.getCount0() / self.AA_per_point / 1000)
                self.time_axis = np.append(self.time_axis, time.time() - self.start_time)
                if self.counts_history[-1] - self.counts_history[-2] < 0:
                    step_M1_x = step_M1_x * -1
                i = i + 1
            elif i % 4 == 1:
                self.actuator_zpl.move_by(self.actuator_zpl.M1_y, step_M1_y)
                self.soc.send(self.confocal_config)
                self.soc.recv()
                self.counts_history = np.append(self.counts_history, self.soc.getCount0() / self.AA_per_point / 1000)
                self.time_axis = np.append(self.time_axis, time.time() - self.start_time)
                if self.counts_history[-1] - self.counts_history[-2] < 0:
                    step_M1_y = step_M1_y * -1
                i = i + 1
            elif i % 4 == 2:
                self.actuator_zpl.move_by(self.actuator_zpl.M2_x, step_M2_x)
                self.soc.send(self.confocal_config)
                self.soc.recv()
                self.counts_history = np.append(self.counts_history, self.soc.getCount0() / self.AA_per_point / 1000)
                self.time_axis = np.append(self.time_axis, time.time() - self.start_time)
                if self.counts_history[-1] - self.counts_history[-2] < 0:
                    step_M2_x = step_M2_x * -1
                i = i + 1
            elif i % 4 == 3:
                self.actuator_zpl.move_by(self.actuator_zpl.M2_y, step_M2_y)
                self.soc.send(self.confocal_config)
                self.soc.recv()
                self.counts_history = np.append(self.counts_history, self.soc.getCount0() / self.AA_per_point / 1000)
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
       
    def pushButton_pulse_gen(self):
        filepath = f'Configs/pulse_gen.toml'
        with open(filepath, 'r') as f:
            self.config = toml.load(f)
        f.close()
        self.soc_config = {
            'command': 'pulse_gen'
        }

        if self.ui.pushButton_pulse_gen.text() == 'pulse gen':
            for key in self.config.keys():
                self.soc_config[key] = self.config[key]
            self.soc.send(self.soc_config)
            self.ui.pushButton_pulse_gen.setText('pulse off')
        else:
            self.soc.send({'command': 'laser_off'})
            self.ui.pushButton_pulse_gen.setText('pulse gen')