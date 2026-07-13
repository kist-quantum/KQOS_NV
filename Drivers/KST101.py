from msl.equipment import EquipmentRecord, ConnectionRecord, Backend
from msl.equipment.resources.thorlabs import MotionControl
import os
import numpy as np
import threading
from pylablib.devices import Thorlabs

class KST101:
    def __init__(self, serial_x: str, serial_y: str, serial_z: str):
        #motor setting
        os.environ['PATH'] += os.pathsep + 'C:/Program Files/Thorlabs/Kinesis'
        # rather than reading the EquipmentRecord from a database we can create it manually
        self.motorX_record = EquipmentRecord(
            manufacturer='Thorlabs',
            model='KST101',
            serial=serial_x,  # update the serial number for your KST101
            connection=ConnectionRecord(
                backend=Backend.MSL,
                address='SDK::Thorlabs.MotionControl.KCube.StepperMotor.dll',
            ),
        )
        self.motorY_record = EquipmentRecord(
            manufacturer='Thorlabs',
            model='KST101',
            serial=serial_y,  # update the serial number for your KST101
            connection=ConnectionRecord(
                backend=Backend.MSL,
                address='SDK::Thorlabs.MotionControl.KCube.StepperMotor.dll',
            ),
        )
        self.motorZ_record = EquipmentRecord(
            manufacturer='Thorlabs',
            model='KST101',
            serial=serial_z,  # update the serial number for your KST101
            connection=ConnectionRecord(
                backend=Backend.MSL,
                address='SDK::Thorlabs.MotionControl.KCube.StepperMotor.dll',
            ),
        )
        MotionControl.build_device_list()
        self.motorX = self.motorX_record.connect()
        self.motorZ = self.motorZ_record.connect()
        self.motorY = self.motorY_record.connect()
        self.motorX.load_settings()
        self.motorZ.load_settings()
        self.motorY.load_settings()
        self.motorX.start_polling(1)
        self.motorZ.start_polling(1)
        self.motorY.start_polling(1)
        self.motorX.set_vel_params(int(55E+6), int(10E+6))
        self.motorY.set_vel_params(int(55E+6), int(10E+6))
        self.motorZ.set_vel_params(int(50E+6), int(25E+6))
    
    def moveTo(self, x=None, y=None, z=None) -> list:
        bool_x, bool_y, bool_z = False, False, False
        try:
            if x is not None:
                bool_x = True
                device_unit = self.motorX.get_device_unit_from_real_value(x, 'DISTANCE')
                self.motorX.move_to_position(device_unit)
            if y is not None:
                bool_y = True
                device_unit = self.motorY.get_device_unit_from_real_value(y, 'DISTANCE')
                self.motorY.move_to_position(device_unit)
            if z is not None:
                bool_z = True
                device_unit = self.motorZ.get_device_unit_from_real_value(z, 'DISTANCE')
                self.motorZ.move_to_position(device_unit)
        except Exception:
            print('Would result in an illegal position - moveTo')
        return bool_x, bool_y, bool_z
        
    def move_relative(self, x=None, y=None, z=None) -> list:
        bool_x, bool_y, bool_z = False, False, False
        # try:
        if x != None:
            bool_x = True
            device_unit = self.motorX.get_device_unit_from_real_value(x, 'DISTANCE')
            self.motorX.move_relative(device_unit)
        if y != None:
            bool_y = True
            device_unit = self.motorY.get_device_unit_from_real_value(y, 'DISTANCE')
            self.motorY.move_relative(device_unit)
        if z != None:
            bool_z = True
            device_unit = self.motorZ.get_device_unit_from_real_value(z, 'DISTANCE')
            self.motorZ.move_relative(device_unit)
        # except Exception:
        #     print('Would result in an illegal position - move_relative')
        return bool_x, bool_y, bool_z
        
    def get_pos(self) -> list:
        position_X = self.motorX.get_position()
        real_pos_X = self.motorX.get_real_value_from_device_unit(position_X, 'DISTANCE')
        position_Z = self.motorZ.get_position()
        real_pos_Z = self.motorZ.get_real_value_from_device_unit(position_Z, 'DISTANCE')
        position_Y = self.motorY.get_position()
        real_pos_Y = self.motorY.get_real_value_from_device_unit(position_Y, 'DISTANCE')
        return real_pos_X, real_pos_Y, real_pos_Z
    
