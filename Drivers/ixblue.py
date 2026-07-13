import serial
import time
from Functions.device_config import *
import logging


class Ixblue:

    def __init__(self):
        
        try:
            self.ser = serial.Serial(
                port = IXBLUE_COMPORT,
                baudrate = 115200,
                stopbits = serial.STOPBITS_ONE,
                parity = serial.PARITY_NONE,
                bytesize = serial.EIGHTBITS,
                timeout = 1
            )
        except:
            logging.warning("The DLC doesn't connected")
    
    @property
    def get_BV(self):
        try:
            self.ser.write(("BV?" + '\r').encode())
            return float(self.ser.readline().decode().strip())
        except:
            logging.warning("The error has occured while get bias voltage")
    
    def set_BV(self, voltage):
        try:
            self.ser.write(("BV " + voltage + '\r').encode())
        except:
            logging.warning("The error has occured while set bias voltage")

    def set_RM(self, run_mode): # mode 
        try:
            self.ser.write(("RM " + run_mode + '\r').encode())
        except:
            logging.warning("The eorror has occured while set run mode")