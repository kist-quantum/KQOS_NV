from zaber_motion import Units
from zaber_motion.ascii import Connection
import numpy as np
import logging
from concurrent.futures import ThreadPoolExecutor

class Zaber_z:
    def __init__(self, ip, port):
        try:
            connection = Connection.open_tcp(ip, port=55550)
            device_list = connection.detect_devices()
            self.device = connection.get_device(1)
            self.axis = self.device.get_axis(1)
            if not self.axis.is_homed():
                self.axis.home()
        except:
            logging.warning("Zaber doesn't connected")

    def move_absolute(self, absolute) -> None:

        try:
            self.axis.move_absolute(absolute, Units.LENGTH_MILLIMETRES)
            self.axis.wait_until_idle(throw_error_on_fault=True)

        except Exception:
            print("Would result in an illegal position - move_absolute")

    def move_relative(self, relative) -> None:
        # with Connection.open_tcp('192.168.0.3', port = 55550) as connection:
        try:
            if relative != None:
                bool_z = True
                self.axis.move_relative(relative, Units.LENGTH_MILLIMETRES)
                self.axis.wait_until_idle(throw_error_on_fault=True)
            else:
                bool_z = False

        except Exception:
            print("Would result in an illegal position - move_relative")
            return

    def home_z(self) -> None:
        self.axis.home()
        self.axis.wait_until_idle(throw_error_on_fault=True)

    def get_pos(self) -> float:
        pos = self.axis.get_position(Units.LENGTH_MILLIMETRES)
        return pos

    def set_ZcurPos(self) -> None:
        pos = self.get_pos()

    def move_max(self) -> None:
        self.axis.move_max(
            wait_until_idle=True,
            velocity=0,
            velocity_unit=Units.NATIVE,
            acceleration=0,
            acceleration_unit=Units.NATIVE,
        )

    def move_min(self) -> None:
        self.axis.move_min(
            wait_until_idle=True,
            velocity=0,
            velocity_unit=Units.NATIVE,
            acceleration=0,
            acceleration_unit=Units.NATIVE,
        )

    def stop(self) -> None:
        self.axis.stop(wait_until_idle=True)
