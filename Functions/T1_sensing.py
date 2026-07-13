import numpy as np
import threading
from Functions.canvas.canvas_autofocus import *
from Functions.canvas.canvas_3D import *
from Drivers.RFSoC import RFSoC
import threading
import toml
import time
import copy

class T1_sensing:
    def __init__(self, ui, soc: RFSoC, stage: PI, Zaber: Zaber_z):
        self.ui = ui
        self.soc = soc
        self.stage = stage
        self.Zaber = Zaber

        self.complete = threading.Event()
        self.canvas_autofocus = canvas_autofocus(self)
        self.ui.sensing_autofocus_layout.addWidget(self.canvas_autofocus)
        self.canvas_T1 = canvas_3D(self)
        self.ui.T1_contrast_layout.addWidget(self.canvas_T1)
        self.init_params()
        pixmap = QPixmap('UI_files/images/icons/cil-media-play.png')
        self.start_icon = QIcon()
        self.start_icon.addPixmap(pixmap)
        pixmap = QPixmap('UI_files/images/icons/cil-media-stop.png')
        self.stop_icon = QIcon()
        self.stop_icon.addPixmap(pixmap)
        
    def init_params(self):
        self.complete.clear()
        self.down_left = {
            'x': float(self.ui.left_down_x.text()),
            'y': float(self.ui.left_down_y.text()),
            'z': self.Zaber.get_pos()
        }
        self.down_right = {
                'x': float(self.ui.right_down_x.text()),
                'y': float(self.ui.right_down_y.text()),
                'z': self.down_left['z']    # z pos는 크게 상관 없음
        }
        self.bins = (
            int(self.ui.bins_x.text()),
            int(self.ui.bins_y.text())
        )
        
        # 완료 -> O, 진행중 -> @, 대기 -> X
        self.status = [['X' for _ in range(self.bins[0])] for _ in range(self.bins[1])]
        # self.update_staus()
        
        # 배열 생성
        self.pillars, self.T1s = self.gen_grid(self.down_left, self.down_right, self.bins)
        self.T1s = np.array([[0 for _ in range(20)] for _ in range(20)])
        self.T1s_contrast = [[0 for _ in range(self.bins[0])] for _ in range(self.bins[1])]
        
        self.soc_config = {}
        with open(f'Configs/spin_control/T1.toml', 'r') as f:
            self.config = toml.load(f)
        f.close()
        for key in self.config['soc'].keys():
            self.soc_config[key] = self.config['soc'][key]
        self.iteration = int(self.ui.sensing_iteration.text())
        self.soc_config['command'] = 'T1'
        self.soc_config['reps'] = int(self.ui.sensing_reps_2.text())
        self.soc_config['resonance_freq'] = float(self.ui.sensing_rf.text())
        self.soc_config['pi_pulse'] = float(self.ui.sensing_pi.text())
        self.soc_config['x'] = float(self.ui.sensing_tau.text())
    
    # target 바꿔야 T1으로 동작함!
    def start(self):
        if self.ui.sensing_start.text() == ' Start':
            thread_sensing = threading.Thread(
                target=self.test_func, name='T1 sensing'
            )
            thread_sensing.daemon = True
            thread_sensing.start()
            self.ui.sensing_start.setText(' Stop')
            self.ui.sensing_start.setIcon(self.stop_icon)
        else:
            self.complete.set()
            self.ui.sensing_start.setText(' Strat')
            self.ui.sensing_start.setIcon(self.start_icon)
        
    def update_staus(self):
        self.status.reverse()
        status_text = f''
        for x_axis in self.status:
            for chr in x_axis:
                status_text += f'{chr}      '
            status_text += f'\n\n'
        self.ui.pillars.setPlainText(status_text)
    
    def start_measure(self):
        self.init_params()
        for y_index, arr in enumerate(self.pillars):
            for x_index, next_pos in enumerate(arr):
                self.status[y_index][x_index] = 'o'
                if self.complete.is_set():
                    return self.end()
                for _ in range(10):
                    self.stage.moveTo(next_pos['x'], next_pos['y'], next_pos['z'])
                self.canvas_autofocus.start_scan()
                pos_cur = self.stage.position()
                self.drift_correction(self.pillars, next_pos, pos_cur)
                # time.sleep(0.5)
                
                temp = time.time()
                for _ in range(self.iteration):
                    self.soc.send(self.soc_config)
                    self.soc.recv()
                    self.T1s[y_index][x_index]['count0'] = np.append(
                        self.T1s[y_index][x_index]['count0'], self.soc.getCount0())
                    self.T1s[y_index][x_index]['count1'] = np.append(
                        self.T1s[y_index][x_index]['count1'], self.soc.getCount1())
                print(time.time() - temp)
                count0_avg = np.average(self.T1s[y_index][x_index]['count0'])
                count1_avg = np.average(self.T1s[y_index][x_index]['count1'])
                self.T1s_contrast[y_index][x_index] = np.subtract(1, np.divide(count1_avg, count0_avg)) * 100
                # print(x_index, y_index)
                # print(self.T1s_contrast)
                self.plot()
        self.end()
    
    def test_func(self):
        self.init_params()
        self.soc_config = {
            'command': 'confocal',
            'CNT1_memory': [0],
            'laser_power': 35000,
            'reps': 1,
            'trig_qick_offset': 0.177,
            'ro_len': 1.5 * 1E+9
        }
        for y_index, arr in enumerate(self.pillars):
            for x_index, next_pos in enumerate(arr):
                self.status[y_index][x_index] = 'o'
                print((x_index, y_index))
                if self.complete.is_set():
                    return self.end()
                for _ in range(10):
                    self.stage.moveTo(next_pos['x'], next_pos['y'], next_pos['z'])
                self.canvas_autofocus.start_scan()
                # pos_cur = self.stage.position()
                # self.drift_correction(self.pillars, next_pos, pos_cur)
                time.sleep(0.1)
                self.soc.send(self.soc_config)
                self.soc.recv()
                self.T1s[y_index][x_index] = self.soc.getCount0() / 0.5 / 1000
                
                self.plot()
        self.end()
                    
    def plot(self):
        self.canvas_T1.axes.clear()
        x = np.arange(0, self.bins[0], 1)
        y = np.arange(0, self.bins[1], 1)
        hist, xedges, yedges = np.histogram2d(x, y, bins=self.bins[0])
        
        # 각 히스토그램 막대의 위치 및 크기 설정
        xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
        xpos = xpos.ravel()
        ypos = ypos.ravel()
        zpos = np.zeros_like(xpos)

        # 히스토그램 막대의 폭과 높이 설정
        dx = dy = 0.3 * np.ones_like(zpos)
        dz = np.array(self.T1s_contrast).ravel()

        # 3D 히스토그램 그리기
        self.canvas_T1.axes.bar3d(xpos, ypos, zpos, 
                        dx, dy, dz, zsort='average', color='coral', edgecolor='black')

        # 축 설정
        self.canvas_T1.axes.set_xlabel('pillar x #', labelpad=10, fontsize=15)
        self.canvas_T1.axes.set_ylabel('pillar y #', labelpad=10, fontsize=15)
        self.canvas_T1.axes.set_zlabel('contrast (%)', labelpad=10, fontsize=15)

        # ticks 설정
        self.canvas_T1.axes.set_xticks([0, 10, 20])
        self.canvas_T1.axes.set_yticks([0, 10, 20])
        self.canvas_T1.axes.set_zticks([0, 10, 20, 30])
        self.canvas_T1.axes.tick_params(axis='x', labelsize=15)
        self.canvas_T1.axes.tick_params(axis='y', labelsize=15)
        self.canvas_T1.axes.tick_params(axis='z', labelsize=15)

        self.canvas_T1.axes.view_init(elev=30, azim=180)

        self.canvas_T1.draw()
    
    def save(self):
        path = f'{FILEPATH}/T1_sensing/{time.strftime("%Y%m%d")}'
        try:
            os.mkdir(path)
        except Exception:
            None
        
        filename = time.strftime("%H") + '시' + time.strftime("%M") + '분' + \
                            time.strftime("%S") + '초'     
        
        np.savez(f'{path}/{filename}', T1s=self.T1s, config=self.soc_config)
        self.canvas_T1.fig.savefig(f'{path}/{filename}')
    
    def end(self):
        self.complete.set()
        self.ui.sensing_start.setText(' Start')
        self.ui.sensing_start.setIcon(self.start_icon)
        self.save()
        
    # TODO: test this function for real
    # call this function after the autofocus
    def drift_correction(self, pillar_arr: list, pos_prev: list, pos_cur: dict) -> list:
        x_delta = pos_cur['x'] - pos_prev['x']
        y_delta = pos_cur['y'] - pos_prev['y']
        z_delta = pos_cur['z'] - pos_prev['z']
        for i in range(len(pillar_arr)):
            for j in range(len(pillar_arr[0])):
                pillar_arr[j][i]['x'] += x_delta
                pillar_arr[j][i]['y'] += y_delta
                pillar_arr[j][i]['z'] += z_delta
        return pillar_arr
    
    def gen_grid(self, down_left: dict, down_right: dict, bins: tuple) -> list:
        x, y = bins
        x1 = down_left['x'];  y1 = down_left['y']
        x2 = down_right['x']; y2 = down_right['y']
        z = down_left['z']
        delta_x = (x2-x1) / (x-1);  delta_y = (y2-y1) / (y-1)
        arr = [[0 for _ in range(x)] for _ in range(y)]
        # starts from down left
        start_x = x1;    start_y = y1
        for i in range(y):
            for j in range(x):
                arr[i][j] = {'x': start_x + j*delta_x, 'y': start_y + j*delta_y, 'z': z}
            start_x -= delta_y
            start_y += delta_x
        T1s = [[{'count0': np.array([]), 'count1': np.array([])} for _ in range(y)] for _ in range(x)]
        return arr, T1s