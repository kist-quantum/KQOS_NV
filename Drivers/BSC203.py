# refernce link https://pylablib.readthedocs.io/en/stable/.apidoc/pylablib.devices.Thorlabs.html
from msl.equipment import EquipmentRecord, ConnectionRecord, Backend
from msl.equipment.resources.thorlabs import MotionControl
import os
import numpy as np
import threading
from pylablib.devices import Thorlabs
import logging

class BSC203:
    def __init__(self, serial_N: str):
        # identifying motor controler
        self.stage = serial_N
        try:
            self.stage = Thorlabs.KinesisMotor(serial_N, is_rack_system=True, default_channel=1)    
        except:
            logging.warning("The Magnetic piezo doesn't connected")
    
    def moveTo(self, x=None, y=None, z=None) -> list:
        bool_x, bool_y, bool_z = False, False, False
        try:
            if x is not None:
                bool_x = True
                self.stage.move_to(x*409600, 1)
                self.stage.wait_move(channel = 1)
            if y is not None:
                bool_y = True
                self.stage.move_to(y*409600, 2)
                self.stage.wait_move(channel = 2)
            if z is not None:
                bool_z = True
                self.stage.move_to(z*409600, 3)
                self.stage.wait_move(channel = 3)
        except Exception:
            print('Would result in an illegal position - moveTo')
        return bool_x, bool_y, bool_z
    
    def move_relative(self, x=None, y=None, z=None) -> list:
        bool_x, bool_y, bool_z = False, False, False
        try:
            if x != None:
                bool_x = True
                self.stage.move_by(x*409600, 1)
            if y != None:
                bool_y = True
                self.stage.move_by(y*409600, 2)
            if z != None:
                bool_z = True
                self.stage.move_by(z*409600, 3)
        except Exception:
            print('Would result in an illegal position - move_relative')
        return bool_x, bool_y, bool_z
        
    def get_pos(self) -> list:
        position_X = self.stage.get_position(1)/409600
        position_Y = self.stage.get_position(2)/409600
        position_Z = self.stage.get_position(3)/409600
        return position_X, position_Y, position_Z