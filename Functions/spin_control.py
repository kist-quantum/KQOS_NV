import numpy as np
import pandas as pd
from Drivers.PI import *
from Drivers.RFSoC import RFSoC
from Drivers.Zaber_z import *
import time
import threading
from Functions.canvas.canvas_1D import *
from Functions.canvas.canvas_autofocus import *
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PySide6.QtWidgets import QDialog
from UI_files.modules.ui_parmeter_dialog import *
import toml
from collections import defaultdict
import random
from Functions.utils import *
from scipy.optimize import curve_fit
import os

class parameter_dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

class spin_control:
    def __init__(self, ui, soc: RFSoC, stage: GCSDevice, Zaber = Zaber_z):
        self.ui = ui
        self.stage = stage
        self.soc = soc
        self.Zaber = Zaber
        self.canvas_autofocus = canvas_autofocus(self)
        self.ui.control_autofocus.addWidget(self.canvas_autofocus)
        self.complete = threading.Event()
        self.complete.set()
        self.canvas_average = canvas_1D(self)
        self.ui.control_average_layout.addWidget(self.canvas_average)
        self.toolbar_average = NavigationToolbar(self.canvas_average, self.ui.control_average_widget)
        self.canvas_contrast = canvas_1D(self)
        self.ui.control_contrast_layout.addWidget(self.canvas_contrast)
        self.toolbar_average = NavigationToolbar(self.canvas_average, self.ui.control_average_widget)
        # self.ui.control_average_layout.addWidget(self.toolbar_average)
        # self.param_dialog = parameter_dialog()
        pixmap = QPixmap('UI_files/images/icons/cil-media-play.png')
        self.start_icon = QIcon()
        self.start_icon.addPixmap(pixmap)
        pixmap = QPixmap('UI_files/images/icons/cil-media-stop.png')
        self.stop_icon = QIcon()
        self.stop_icon.addPixmap(pixmap)
        self.fit_flag = False
        self.canvas_contrast.mpl_connect("motion_notify_event", self.current_cursor)
        self.canvas_contrast.mpl_connect("button_press_event", self.setRange)

        toml_files = [self.ui.control_type.addItem(f.replace(".toml", "")) for f in os.listdir("Configs/spin_control") if f.endswith(".toml")]
        

        
        
    def init_params(self):
        self.need_auto = False
        self.stopping = False
        self.complete.clear()
        self.ui.reps.setText('1')
        self.experiment = self.ui.control_type.currentText()
        filepath = f'Configs/spin_control/{self.experiment}.toml'
        with open(filepath, 'r') as f:
            self.config = toml.load(f)
        f.close()
        self.x_axis = np.arange(self.config['pc']['start'],\
            self.config['pc']['end'], self.config['pc']['step'])
        self.cnt1_temp = 0
        self.cnt2_temp = 0
        self.i_apd0 = np.zeros((1, len(self.x_axis)))
        self.i_apd1 = np.zeros((1, len(self.x_axis)))
        self.ref = np.zeros((1, len(self.x_axis)))
        self.i_apd0_sum = np.zeros(len(self.x_axis))
        self.i_apd1_sum = np.zeros(len(self.x_axis))
        self.ref_sum = np.zeros(len(self.x_axis))
        
        self.i_apd0_average = np.zeros(len(self.x_axis))
        self.i_apd1_average = np.zeros(len(self.x_axis))
        self.ref_average = np.zeros(len(self.x_axis))
        self.contrast = np.zeros(len(self.x_axis))
        self.sub = np.zeros(len(self.x_axis))
        self.fit_y = np.zeros(len(self.x_axis))
        self.fit_x = np.zeros(len(self.x_axis))
        self.fft = np.zeros(len(self.x_axis))
        self.fft_x = np.zeros(len(self.x_axis))
        self.previous_filename = None
        self.soc_config = {
            'command': self.experiment
        }
        for key in self.config['soc'].keys():
            self.soc_config[key] = self.config['soc'][key]
        
    def start(self):
        if self.ui.control_start.text() == ' Start':
            thread_control = threading.Thread(target=self.start_control, daemon = True)
            thread_control.start()
            thread_timer = threading.Thread(target=self.timer, daemon = True)
            thread_timer.start()
            self.ui.control_start.setText(' Shutdown')
            self.ui.control_start.setIcon(self.stop_icon)
            self.ui.control_stop.setText(' Stop')
        else:
            self.complete.set()
            self.ui.control_start.setText(' Start')
            self.ui.control_start.setIcon(self.start_icon)

    def stop(self):
        if self.ui.control_stop.text() == ' Stop':
            self.stopping = True
            self.ui.control_stop.setText(' Proceed')
        else:
            self.ui.control_stop.setText(' Stop')
            self.stopping = False
        
    def start_control(self):
        self.init_params()
        self.index_mapper = defaultdict(int)
        for index, val in enumerate(self.x_axis):
            self.index_mapper[val] = index
        iter_x = self.x_axis
        #레이저 키는거 추가 해야하나?
        for cur_num_cycle in range(1, self.config['pc']['iteration']+1):
            self.ui.reps.setText(str(cur_num_cycle))
            if self.config['pc']['shuffle']:
                iter_x = sorted(self.x_axis, key=lambda k: random.random())
            # stop
            if self.stopping:
                return self.end() 
            for index, x in enumerate(iter_x):
                # shutdown
                if self.complete.is_set():
                    return self.end()
                # config에 sweep 값 업데이트
                self.soc_config['x'] = float(x)
                self.soc.send(self.soc_config)
                self.soc.recv()
                if self.config['pc']['shuffle']:
                    index = self.index_mapper[x]
                self.i_apd0[-1][index] = self.soc.getCount0()
                self.i_apd1[-1][index] = self.soc.getCount1()
                self.set_count()
                try:
                    self.plot(index)
                except Exception:
                    pass
                if not self.canvas_autofocus.complete.is_set():
                    self.autofocus()
            self.i_apd0 = np.append(self.i_apd0, np.zeros((1, len(self.x_axis))), axis=0)
            self.i_apd1 = np.append(self.i_apd1, np.zeros((1, len(self.x_axis))), axis=0)
        self.end()
                
    def autofocus(self):
        thread_autofocus = threading.Thread(target=self.canvas_autofocus.start_scan)
        thread_autofocus.daemon = True
        thread_autofocus.start()
        time.sleep(0.05)    # event가 clear 될 동안 시간 주는게 좋을지도?
        self.canvas_autofocus.complete.wait()
    
    def end(self):
        self.save()
        self.ui.control_start.setText(' Start')
        self.ui.control_start.setIcon(self.start_icon)
        
    def set_count(self):
        self.i_apd0_sum = np.sum(self.i_apd0, axis=0)
        self.i_apd1_sum = np.sum(self.i_apd1, axis=0)
        self.i_apd0_average = np.divide(self.i_apd0_sum, len(self.i_apd0))
        self.i_apd1_average = np.divide(self.i_apd1_sum, len(self.i_apd1))
        # self.sub = np.subtract(self.i_apd0_average, self.i_apd1_average)
        if 0 not in self.i_apd0_average:
            # self.contrast = self.sub/self.i_apd0_average
            self.contrast = np.subtract(1, self.i_apd0_average/self.i_apd1_average)
    
    def plot(self, current_index):
        self.canvas_average.axes.clear()
        self.canvas_contrast.axes.clear()
        self.canvas_average.axes.grid()
        self.canvas_contrast.axes.grid()
        self.canvas_contrast.axes.set_xlabel('tau (ns)')
        self.canvas_average.axes.set_ylabel('counts (a.u.)')
        self.canvas_contrast.axes.set_ylabel('contrast (%)')
        
        self.canvas_average.axes.plot(self.x_axis, self.i_apd0_average,\
            marker='o', label='first', c='r')
        self.canvas_average.axes.plot(self.x_axis, self.i_apd1_average,\
            marker='o', label='second', c='g')
        self.canvas_average.axes.legend()
        self.canvas_contrast.axes.plot(
            self.x_axis, np.multiply(self.contrast, 100),\
            marker='o', c='coral', label='experiment')
        if current_index == len(self.x_axis-1):
            self.canvas_average.axes.axvline(x=self.x_axis[0], c='yellow',\
                linestyle='dashed', label='current step', linewidth=0.5)
        else:
            self.canvas_average.axes.axvline(x=self.x_axis[current_index+1], \
                c='yellow', linestyle='dashed', label='current step', linewidth=0.5)
        
        if self.fit_flag:
            # try:
            self.fit() 
            # except Exception:
                # pass
            if self.experiment == 'Ramsey':
                pass
            else:
                self.canvas_contrast.axes.plot(
                    self.fit_x, np.multiply(self.fit_y, 100), label='fit', c='r')
                self.canvas_contrast.axes.legend()
        self.canvas_average.draw()
        self.canvas_contrast.draw()
    
    def fit(self):
        x_from = float(self.ui.fit_from.text())
        x_to = float(self.ui.fit_to.text())
        val, x_from_index = find_nearest(self.x_axis, x_from)
        val, x_to_index = find_nearest(self.x_axis, x_to)
        x = np.array(self.x_axis[x_from_index:x_to_index], dtype=np.float32) 
        y = np.array(self.contrast[x_from_index:x_to_index], dtype=np.float32)
        self.fit_x = np.linspace(x[0], x[-1], 1000)
        self.fit_y = np.zeros(len(self.fit_x))
        if self.experiment == 'ODMR':
            # p0 = [x0, HWFM, y0, A]
            p0 = [np.average(x), 50, np.average(y), (y[-1]-y[0])*np.average(y)]
            popt, pocv = curve_fit(lorentzian, x, y, p0=p0, maxfev=10000)
            self.fit_y = lorentzian(self.fit_x, *popt)
            self.ui.label_43.setText('Resonance frequency (MHz)')
            self.ui.fit_result.setText(str(round(popt[0], 4)))
        elif self.experiment == 'rabi_gg_PSB' or self.experiment == 'rabi_gr_PSB':
            # p0 = [constant, amplitude, omega, phase, y0]
            p0 = [0, np.max(y)-np.min(y), 0.05, np.pi/2, np.average(y)]
            popt, pocv = curve_fit(damped_sin, x, y, p0=p0, maxfev=10000)
            self.fit_y = damped_sin(self.fit_x, *popt)
            self.ui.fit_result.setText(str(round((2*np.pi) / (popt[2]*2), 1)))
            self.ui.label_43.setText('Pi pulse length (ns)')
        elif self.experiment == 'Ramsey':
            self.fft_x, self.fft = FFT(x, y)
        elif self.experiment == 'Echo':
            pass
        else:
            pass

    def save(self):
        path = f'{FILEPATH}/{self.experiment}/{time.strftime("%Y%m%d")}'
        try:
            os.makedirs(path, exist_ok = True)
        except Exception:
            None
        # add self.experiment for identifying experiment
        filename = self.experiment + '_' + time.strftime("%H") + '시' + time.strftime("%M") + '분' + time.strftime("%S") + '초'
                            
        # save as png
        self.canvas_contrast.fig.savefig(f'{path}/{filename}')
        
        # save as csv
        df = pd.DataFrame({'i_apd0' : self.i_apd0[-1],'i_apd1' : self.i_apd1[-1], 'i_apd0_sum' : self.i_apd0_sum, 'i_apd1_sum' : self.i_apd1_sum, 'apd_contrast' : self.contrast, })
        df = df.set_index(keys = [self.x_axis], inplace = False)
        df.to_csv(f'{path}/{filename}.csv')
            
    def current_cursor(self, event):
        pass

    def setRange(self, event):
        if event.inaxes != self.canvas_contrast.axes:
            return

        if event.button == 1:
            self.ui.fit_from.setText(str(round(event.xdata, 1)))

        if event.button == 3:
            self.ui.fit_to.setText(str(round(event.xdata, 1)))

    def fit_state_changed(self):
        self.fit_flag = self.ui.control_fitting.isChecked()
        try:
            self.plot()
        except Exception:
            pass
        
    def timer(self):
        start_time = time.time()
        while not self.complete.is_set():
            time.sleep(1)
            self.ui.autofocus_in.setText(
                str(int(self.config['pc']['autofocus_period'] - (time.time() - start_time))))
            if time.time() - start_time > self.config['pc']['autofocus_period']:
                self.canvas_autofocus.complete.clear()
                self.canvas_autofocus.complete.wait()
                start_time = time.time()