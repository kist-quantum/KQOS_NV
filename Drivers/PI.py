from pipython import pitools
from pipython import GCSDevice
from pipython.pidevice.common.gcsbasedevice import GCSBaseDevice
from Drivers.Zaber_z import Zaber_z
import logging

class PI:
    def __init__(self, ip: str, port: int, autoconnect=True):
        try:
            self.gcs = GCSDevice('E-727')
            self.gcs.gcsdevice.ConnectTCPIP(ipaddress=ip, ipport=port, autoconnect=autoconnect)
        except:
            logging.warning("E-727 doesn't connected")
    
    def moveTo(self, x=None, y=None) -> dict:
        if x >= 0 and x <= 35 and y >= 0 and y <= 35:
            if x != None:
                self.gcs.MOV(('1'), x)
            if y != None:
                self.gcs.MOV(('2'), y)
            pitools.waitontarget(self.gcs, self.gcs.axes)
        else:
            print(x, y)
        return self.position()
    
    def home(self) -> dict:
        self.moveTo(17.5, 17.5)
        return self.position()
    
    def position(self) -> dict:
        return {'x': (round(self.gcs.qPOS('1').get('1'), 3)),
                'y': (round(self.gcs.qPOS('2').get('2'), 3)),
                }


    