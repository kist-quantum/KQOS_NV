# import unittest
from pylablib.devices import Thorlabs
serial_N = "70351394"
stage = Thorlabs.KinesisMotor(serial_N, is_rack_system=True, scale=409600, default_channel=1)    
print(stage.get_device_info())
print(stage.move_to(30, 2))
stage.wait_move(2)
print(stage.get_position(2))