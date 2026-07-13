import numpy as np
from Functions.canvas.canvas_2D import canvas_2D
from Functions.utils import *
from Drivers.RFSoC import RFSoC
from Drivers.KST101 import KST101
from Drivers.BSC203 import BSC203
import threading    
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QPushButton
from mpl_toolkits.axes_grid1 import make_axes_locatable
import time
import os
from Functions.utils import FILEPATH

class B_align:
    def __init__(self, ui, soc: RFSoC, magent_stage: BSC203):
        self.ui = ui
        self.soc = soc
        self.magnet_stage = magent_stage
        self.canvas_B = canvas_2D(self)
        self.ui.magnet_layout.addWidget(self.canvas_B)

        pixmap = QPixmap('UI_files/images/icons/cil-media-play.png')
        self.start_icon = QIcon()
        self.start_icon.addPixmap(pixmap)
        pixmap = QPixmap('UI_files/images/icons/cil-media-stop.png')
        self.stop_icon = QIcon()
        self.stop_icon.addPixmap(pixmap)
        # self.set_pos()
        self.complete = threading.Event()
        self.move_event = threading.Event()

    def init_params(self):
        self.complete.clear()
        self.xz_size = float(self.ui.magnet_size.text())
        self.xz_step = float(self.ui.magnet_step.text())
        self.T_per_point = float(self.ui.magnet_per_point.text())
        self.resolution = int(self.xz_size / self.xz_step)
        self.counts = np.zeros((self.resolution + 1, self.resolution + 1))
        self.x_pos, self.z_pos, self.z_pos = self.magnet_stage.get_pos()
        self.x_from = self.x_pos - self.xz_size/2
        self.x_to = self.x_pos + self.xz_size/2
        self.z_from = self.z_pos - self.xz_size/2
        self.z_to = self.z_pos + self.xz_size/2
        self.row = []
        self.column = []
        self.lable_step = 3  # 축 label 갯수
        for i in range(0, self.lable_step + 1, 1):
            self.row.append(round(self.x_from + i * (self.x_to - self.x_from) / self.lable_step, 1))
            self.column.append(round(self.z_from + i * (self.z_to - self.z_from) / self.lable_step, 1))
        self.real_row = []
        self.real_col = []
        for i in range(0, self.lable_step + 1, 1):
            self.real_row.append(i * self.resolution / self.lable_step)
            self.real_col.append(i * self.resolution / self.lable_step)

        self.counts = np.zeros((self.resolution+1, self.resolution+1))
        self.pos_array = [[]]
        for i in range(0, self.resolution+1, 1):
            self.pos_array.append([])
            for j in range(0, self.resolution+1, 1):
                self.pos_array[i].append((j, i, 0, 0))
        self.magnet_config = {
            'command': 'confocal',
            'laser_ch': 5,
            'CNT1_memory': [0],
            'laser_power': 35000,
            'reps': 1,
            'trig_qick_offset': 0.177,
            'ro_len': self.T_per_point * 1E+9
        }
    
    def start(self):
        if self.ui.magnet_start.text() == ' Start':
            self.ui.magnet_start.setText(" Stop")
            self.ui.magnet_start.setIcon(self.stop_icon)
            thread_B_align = threading.Thread(target=self.start_scan)
            thread_B_align.daemon = True
            thread_B_align.start()
        else:
            self.complete.set()
            self.ui.magnet_start.setText(' Start')
            self.ui.magnet_start.setIcon(self.start_icon)
        
    def start_scan(self):
        self.init_params()
        for z in range(self.resolution + 1):
            self.magnet_stage.moveTo(z=(self.z_from + z*self.xz_step))
            time.sleep(0.1) # 컨트롤러에서 도착했다고 하더라도 흔들림이 멈출때 까지 기다려줘야함
            for x in range(self.resolution + 1):
                if self.complete.is_set():
                    return self.end()
                self.magnet_stage.moveTo(x=(self.x_from + x*self.xz_step))
                time.sleep(0.1)
                self.soc.send(self.magnet_config)
                self.soc.recv()
                self.counts[z][x] = self.soc.getCount0()\
                    / 1000 / self.T_per_point
                pos = self.magnet_stage.get_pos()
                self.pos_array[z][x] = {
                    'x': pos[0], 'y': pos[1], 'z': pos[2]
                }
                self.x_pos, self.y_pos, self.z_pos = self.magnet_stage.get_pos()
                self.ui.magnet_position_x.setText(str(self.x_pos))
                self.ui.magnet_position_y.setText(str(self.y_pos))
                self.ui.magnet_position_z.setText(str(self.z_pos))
                self.plot()
        self.end()
                
    def end(self):
        self.moveTo_MAX()
        self.ui.magnet_start.setText(' Start')
        self.ui.magnet_start.setIcon(self.start_icon)
        self.save()
    
    def save(self) -> None:
        path = f'{FILEPATH}/B_align/{time.strftime("%Y%m%d")}'
        try:
            os.makedirs(path, exist_ok = True)
        except Exception:
            None
        
        filename = time.strftime("%H") + '시' + time.strftime("%M") + '분' + \
                            time.strftime("%S") + '초' + ', '        
        
        np.savez(f'{path}/{filename}', count=self.counts)
        self.canvas_B.fig.savefig(f'{path}/{filename}')
        
    def plot(self):
        self.canvas_B.axes.clear()
        self.canvas_B.image = self.canvas_B.axes.imshow(self.counts, cmap='magma')
        self.canvas_B.axes.set_xticks(self.real_row)
        self.canvas_B.axes.set_yticks(self.real_col)
        self.canvas_B.axes.set_xticklabels(self.row, rotation=0)
        self.canvas_B.axes.set_yticklabels(self.column)
        if self.canvas_B.colorbar is not None:
            try:
                self.canvas_B.colorbar.remove()
            except Exception as e:
                pass
        self.canvas_B.divider = make_axes_locatable(self.canvas_B.axes)
        self.canvas_B.cax = self.canvas_B.divider.append_axes("right", size='2%', pad=0.5)
        self.canvas_B.colorbar = self.canvas_B.fig.colorbar(self.canvas_B.image, cax=self.canvas_B.cax)
        self.canvas_B.draw()
    
    def moveTo_MAX(self):
        max = np.max(self.counts)
        index = np.where(self.counts==max)
        x_max_index = index[1][0]; z_max_index = index[0][0]
        x_max = self.pos_array[z_max_index][x_max_index]['x']
        z_max = self.pos_array[z_max_index][x_max_index]['z']
        
    def set_pos(self):
        x_pos, y_pos, z_pos = self.magnet_stage.get_pos()
        self.ui.magnet_position_x.setText(str(np.round(x_pos, 2)))
        self.ui.magnet_position_y.setText(str(np.round(y_pos, 2)))
        self.ui.magnet_position_z.setText(str(np.round(z_pos, 2)))
            
    def move(self):
        if self.ui.magnet_set_position_x.text() != '':
            x = float(self.ui.magnet_set_position_x.text())
        else:
            x = None
        if self.ui.magnet_set_position_y.text() != '':
            y = float(self.ui.magnet_set_position_y.text())
        else:
            y = None
        if self.ui.magnet_set_position_z.text() != '':
            z = float(self.ui.magnet_set_position_z.text())
        else:
            z = None
        self.magnet_stage.moveTo(x, y, z)
        self.x_pos, self.y_pos, self.z_pos = self.magnet_stage.get_pos()
        self.ui.magnet_position_x.setText(str(self.x_pos))
        self.ui.magnet_position_y.setText(str(self.y_pos))
        self.ui.magnet_position_z.setText(str(self.z_pos))
    
    def jog(self, button: QPushButton):
        name = button.text()
        if name == ' Jog foward x':
            bools = self.magnet_stage.move_relative(x=float(self.ui.magnet_step_jog.text()))
        elif name == ' Jog foward y':
            bools = self.magnet_stage.move_relative(y=float(self.ui.magnet_step_jog.text()))
        elif name == ' Jog foward z':
            bools = self.magnet_stage.move_relative(z=float(self.ui.magnet_step_jog.text()))
        elif name == ' Jog backward x':
            bools = self.magnet_stage.move_relative(x=-1*float(self.ui.magnet_step_jog.text()))
        elif name == ' Jog backward y':
            bools = self.magnet_stage.move_relative(y=-1*float(self.ui.magnet_step_jog.text()))
        elif name == ' Jog backward z':
            bools = self.magnet_stage.move_relative(z=-1*float(self.ui.magnet_step_jog.text()))
        thread_wait = threading.Thread(target=self.wait, args=bools)
        thread_wait.daemon = True
        thread_wait.start()