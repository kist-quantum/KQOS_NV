import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable
import threading
from Drivers.PI import *
from Drivers.Zaber_z import Zaber_z
import time
from pprint import pprint
import os
from PySide6.QtGui import QIcon, QPixmap
from Functions.utils import FILEPATH# , LASER_ON_CONFIG
import toml

class canvas_autofocus(FigureCanvas):
    def __init__(self, func):
        self.func = func
        self.ui = func.ui
        self.stage = func.stage
        self.Zaber = func.Zaber
        self.soc = func.soc
        self.fig = plt.Figure(figsize=(50, 20))
        self.fig.set_facecolor((40/255, 44/255, 52/255))
        self.fig.set_tight_layout(0.2)
        plt.rcParams['font.size'] = 12
        plt.rcParams['font.family'] = 'Segoe UI Semibold'
        plt.rcParams['font.family'] = 'Gulim'
        plt.rcParams['xtick.color'] = 'White'
        plt.rcParams['ytick.color'] = 'White'
        plt.rcParams['axes.labelcolor'] = 'White'
        self.axes_xy = self.fig.add_subplot(121)
        self.axes_xy.set_xlabel('X axis')
        self.axes_xy.set_ylabel('Y axis')
        self.counts = np.zeros((10, 10))
        self.image = self.axes_xy.imshow(self.counts, cmap='magma')
        self.divider = make_axes_locatable(self.axes_xy)
        self.cax = self.divider.append_axes("right", size='2%', pad=0.1)
        self.colorbar = self.fig.colorbar(self.image, cax=self.cax)
            
        self.axes_z = self.fig.add_subplot(122)
        self.axes_z.patch.set_facecolor((40/255, 44/255, 52/255))
        self.axes_z.set_xlabel('Z (um)')
        self.axes_z.set_ylabel('Count [kcps]')
        self.axes_z.grid(True)
        
        FigureCanvas.__init__(self, self.fig)
        self.blit()
        self.draw()
        self.mpl_connect('motion_notify_event', self.pos_cursor)
        
        #########################
        self.complete = threading.Event()
        self.complete.set()
        
        pixmap = QPixmap('UI_files/images/icons/cil-media-play.png')
        self.start_icon = QIcon()
        self.start_icon.addPixmap(pixmap)
    
    def save(self):
        path = f'{FILEPATH}/Confocal/{time.strftime("%Y%m%d")}/Autofocus'
        try:
            os.mkdir(path)
        except Exception:
            None
        
        filename = time.strftime("%H") + '시' + time.strftime("%M") + '분' + \
                            time.strftime("%S") + '초'
        
        np.savez(f'{path}/{filename}', xy_pos=self.positions, xy_counts=self.counts,\
                    z_pos=self.z_pos_average, z_counts=self.z_counts_average)
        self.fig.savefig(f'{path}/{filename}')
        
    def pos_cursor(self, event):
        if event.inaxes != self.axes_xy:
            return
        try:
            x = int(event.xdata); y = int(event.ydata)
            self.func.ui.confocal_set_position_x.setText(str(self.positions[y][x]['x']))
            self.func.ui.confocal_set_position_y.setText(str(self.positions[y][x]['y']))
            self.func.ui.confocal_set_position_z.setText(str(self.positions[y][x]['z']))
            self.func.ui.confocal_counts.setText(str(round(self.counts[y][x])))
        except Exception:
            pass
        
    def init_params(self):
        self.complete.clear()
        # self.soc.send(LASER_ON_CONFIG)
        time.sleep(0.01)
        cur_pos = self.stage.position()
        cur_pos['z'] = round(self.Zaber.get_pos(), 3)
        self.z_fixed = True
        self.x_pos = float(cur_pos['x'])
        self.y_pos = float(cur_pos['y'])
        self.z_pos = float(cur_pos['z'])
        self.xy_size = float(self.ui.autofocus_size_xy.text())
        self.xy_step = float(self.ui.confocal_step_xy.text())
        self.resolution = int(self.xy_size/self.xy_step)
        self.counts = np.zeros((self.resolution+1, self.resolution+1))
        self.positions = [[{'x':'0', 'y':'0', 'z':'0'} for _ in range(self.resolution+1)] for _ in range(self.resolution+1)]
        self.x_from = self.x_pos - self.xy_size/2
        self.x_to = self.x_pos + self.xy_size/2
        self.x_delta = self.xy_step
        self.y_delta = self.xy_step
        self.y_from = self.y_pos - self.xy_size/2
        self.y_to = self.y_pos + self.xy_size/2
        for index_y, y in enumerate(self.positions):
            for index_x, x in enumerate(y): 
                self.positions[index_y][index_x]['x'] = self.x_from + self.xy_step * index_x
                self.positions[index_y][index_x]['y'] = self.y_from + self.xy_step * index_y
                self.positions[index_y][index_x]['z'] = self.z_pos
                
        self.z_size = float(self.ui.autofocus_size_z.text())
        self.z_step = float(self.ui.confocal_step_z.text())
        self.z_resolution = int(self.z_size/self.z_step)
        
        self.z_from = self.z_pos - self.z_size/2
        self.z_to = self.z_pos + self.z_size/2
        self.z_axis = np.linspace(self.z_from, self.z_to, self.z_resolution)
        
        self.z_pos_average = np.linspace(self.z_from, self.z_to, self.z_resolution)
        self.z_pos_forward = np.linspace(self.z_from, self.z_to, self.z_resolution)
        self.z_pos_backward = np.linspace(self.z_from, self.z_to, self.z_resolution)
        self.z_3pos = [0 for _ in range(self.z_resolution)]
        self.z_counts_forward = np.zeros(self.z_resolution)
        self.z_counts_backward = np.zeros(self.z_resolution)
        self.z_counts_average = np.zeros(self.z_resolution)
        
        if self.ui.autofocus_01.isChecked():
            self.T_per_point = 0.1
        elif self.ui.autofocus_005.isChecked():
            self.T_per_point = 0.05
        else:
            self.T_per_point = 0.01
        self.gerenate_axis()
        self.confocal_config = {
            'command': 'confocal',
            'laser_ch': 5,
            'CNT1_memory': [0],
            'laser_power': 35000,
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
    
    def gerenate_axis(self):
        self.row = []
        self.column = []
        self.lable_step = 2  # 축 label 갯수
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
            
    def start_scan(self):
        self.init_params()
        # xy
        for i in range(0, self.resolution+1, 1):
            for j in range(0, self.resolution+1, 1):
                if self.complete.is_set():
                    return self.end()
                self.moveDelta_and_count(i, j)
            self.plot_xy()
        for _ in range(10):
            pos = self.goTo_xy_max()
        self.x_pos = pos['x']
        self.y_pos = pos['y']
        self.z_pos = pos['z']
        time.sleep(0.05)
        
        for index, z_pos in enumerate(self.z_axis):
            if index == 0:
                self.z_pos_forward[index] = self.moveTo(self.x_pos, self.y_pos, z_pos)['z']
                self.z_pos_forward[index] = self.moveTo(self.x_pos, self.y_pos, z_pos)['z']
            if self.complete.is_set():
                return self.end()
            self.z_pos_forward[index] = self.moveTo(self.x_pos, self.y_pos, z_pos)['z']
            self.soc.send(self.confocal_config)
            self.soc.recv()
            self.z_counts_forward[index] = self.soc.getCount0() / self.confocal_config['ro_len'] * 1E+9 / 1000
            self.plot_z()
        # backward
        self.z_axis = np.flip(self.z_axis)
        for index, z_pos in enumerate(self.z_axis):
            if self.complete.is_set():
                return self.end()
            self.z_pos_backward[len(self.z_pos_backward)-1-index] = self.moveTo(self.x_pos, self.y_pos, z_pos)['z']
            self.soc.send(self.confocal_config)
            self.soc.recv()
            self.z_counts_backward[len(self.z_pos_backward)-1-index] = self.soc.getCount0() / self.confocal_config['ro_len'] * 1E+9 / 1000
            self.plot_z()
        for _ in range(10):
            self.goTo_z_max()
        self.end()
        
    def end(self):
        self.complete.set()
        self.ui.autofocus_start.setText('Start')
        self.ui.autofocus_start.setIcon(self.start_icon)
        self.save()
        
    def plot_xy(self):
        self.axes_xy.clear()
        self.image = self.axes_xy.imshow(self.counts, cmap='magma')
        self.axes_xy.set_xlim(0, self.resolution)
        self.axes_xy.set_ylim(0, self.resolution)
        self.axes_xy.set_xlabel('X axis')  # set the label for the x-axis
        self.axes_xy.set_ylabel('Y axis')
        self.axes_xy.set_xticks(self.real_row)
        self.axes_xy.set_yticks(self.real_col)
        self.axes_xy.set_xticklabels(self.row, rotation=0)
        self.axes_xy.set_yticklabels(self.column)

        if self.colorbar is not None:
            try:
                self.colorbar.remove()
            except Exception as e:
                pass
        self.divider = make_axes_locatable(self.axes_xy)
        self.cax = self.divider.append_axes("right", size='2%', pad=0.1)
        self.colorbar = self.fig.colorbar(self.image, cax=self.cax)
        self.draw()
    
    def plot_z(self):
        self.z_counts_average = (self.z_counts_forward + self.z_counts_backward) / 2
        self.z_pos_average = (self.z_pos_forward + self.z_pos_backward) / 2
        self.axes_z.clear()
        
        self.axes_z.patch.set_facecolor((40/255, 44/255, 52/255))
        self.axes_z.grid()
        self.axes_z.plot(self.z_pos_forward, self.z_counts_forward, linewidth=1, c='#fe79c7', label='forward')
        self.axes_z.plot(self.z_pos_backward, self.z_counts_backward, linewidth=1, c='coral', label='backward')
        self.axes_z.plot(self.z_pos_average, self.z_counts_average, linewidth=2.5, c='red', label='average')
        # self.axes_z.legend()
        self.axes_z.set_xlabel('Z (um)')  # set the label for the x-axis
        self.axes_z.set_ylabel('Counts (kcps)')
        self.draw()
     
    def moveTo(self, x, y, z) -> tuple:
        pos = self.stage.moveTo(x, y)
        self.Zaber.move_absolute(z)
        pos['z'] = round(self.Zaber.get_pos(), 3)
        self.ui.confocal_position_x.setText(str(pos['x']))
        self.ui.confocal_position_y.setText(str(pos['y']))
        self.ui.confocal_position_z.setText(str(pos['z']))
        return pos

    def moveDelta_and_count(self, i, j) -> None:
        self.positions[i][j] = self.moveTo(x=self.x_from + self.x_delta * j,\
                                y=self.y_from + self.y_delta * i,\
                                z=self.z_pos)
        self.soc.send(self.confocal_config)
        self.soc.recv()
        self.counts[i][j] = self.soc.getCount0() / self.confocal_config['ro_len'] * 1E+9 / 1000

    def goTo_xy_max(self) -> tuple:
        y_index, x_index = np.where(self.counts==np.max(self.counts))
        
        y_index = y_index[0];   x_index = x_index[0]
        z_max = self.positions[y_index][x_index]['z']
        y_max = self.positions[y_index][x_index]['y']
        x_max = self.positions[y_index][x_index]['x']
        return self.moveTo(x_max, y_max, z_max)
    
    def goTo_z_max(self) -> tuple:
        index = np.where(self.z_counts_average==np.max(self.z_counts_average))[0][0]
        z_max = self.z_pos_average[index]
        return self.moveTo(self.x_pos, self.y_pos, z_max)