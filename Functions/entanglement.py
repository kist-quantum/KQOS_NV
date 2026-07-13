from Drivers.RFSoC import RFSoC
import numpy as np
from PySide6.QtGui import QPixmap, QIcon
import threading
import time
from Drivers.Actuator_piezo import *
from Functions.utils import *
import os
import toml
from Functions.canvas.canvas_1D import *
# from Functions.utils import LASER_ON_CONFIG

class entanglement:
    def __init__(self, ui, soc: RFSoC):
        self.ui = ui
        self.soc = soc
        self.canvas_SPE = canvas_1D(self) # SPE(spin photon entanglement)
        self.ui.verticalLayout_spin_photon_count.addWidget(self.canvas_SPE)
        self.spin_photon_flag = Flag()
        self.array_state = ["0E", "0L", "1E", "1L"]

    def init_params(self):
        self.stopping = False
        self.spin_photon_flag.clear()
        filepath = f'Configs/spin_photon.toml'
        with open(filepath, 'r') as f:
            self.config = toml.load(f)
        f.close()
        self.soc_config = {
            'command': 'spin_photon'
        }
        for key in self.config['soc'].keys():
            self.soc_config[key] = self.config['soc'][key]
        self.count_array = np.zeros(4)
        self.canvas_SPE.axes.clear()

    def pressed_spinPhoton_button(self):
        if self.ui.pushButton_spin_photon_start.text() == "start":
            self.init_params()
            print(self.soc_config)
            self.spin_photon_exp_thread = threading.Thread(
                target = self.start_spin_photon_Ent,
                args = (),
                daemon = True,
            )
            self.spin_photon_exp_thread.start()
            self.ui.pushButton_spin_photon_start.setText("stop")

        elif self.ui.pushButton_spin_photon_start.text() == "stop":
            self.spin_photon_flag.set()
            self.ui.pushButton_spin_photon_start.setText("start")
    
    def start_spin_photon_Ent(self):
        while not self.spin_photon_flag.is_set():
            self.soc.send(self.soc_config)
            self.soc.recv()
            count_0 = self.soc.getCount0()
            count_1 = self.soc.getCount2()
            count_2 = self.soc.getCount4()
            count_3 = self.soc.getCount6()
            if count_0 == 0 and count_1 > 0 and count_2 > 0 and count_3 == 0:
                self.count_array[0] += 1
            elif count_0 == 0 and count_1 > 0 and count_2 == 0 and count_3 > 0:
                self.count_array[1] += 1
            elif count_0 > 0 and count_1 == 0 and count_2 > 0 and count_3 == 0:
                self.count_array[2] += 1
            elif count_0 > 0 and count_1 == 0 and count_2 == 0 and count_3 > 0:
                self.count_array[3] += 1
            else:
                pass
            time.sleep(0.01)
            print(self.count_array)
            # self.canvas_SPE.axes.bar(self.array_state, self.count_array, color = 'blue')
            # self.canvas_SPE.draw()


    def spin_photon_stop(self):
        self.spin_photon_exp.shutdown()
        self.canvas_spin_photon.shutdown_draw()

class Flag(threading.Event):
    """A wrapper for the typical event class to allow for overriding the
    `__bool__` magic method, since it looks nicer.
    """

    def __bool__(self):
        return self.is_set()