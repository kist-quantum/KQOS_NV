# refernce link : https://github.com/attocube-systems/AMC-APIs

from Drivers.AMC_API.python import AMC
import logging

class AMC300:
    def __init__(self, ip : str):
        try:
            self.Device = AMC.Device("192.168.0.145")
            self.Device.connect()
        except:
            logging.warning("cant find AMC 300")
    
    def get_positions(self):
        self.x_axis = self.Device.move.getPosition(0)
        self.y_axis = self.Device.move.getPosition(1)
        self.z_axis = self.Device.move.getPosition(2)

    def close(self):
        self.Device.close()