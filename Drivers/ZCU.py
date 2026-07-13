from Drivers.RFSoC import RFSoC

class ZCU_4x2(RFSoC):
    def __init__(self, ip: str, port: int):
        super().__init__(ip, port)
        self.laser_ch = 1
        self.mw_ch = 0
        # self.laser_on()
        
class ZCU_111(RFSoC):
    def __init__(self, ip: str, port: int):
        super().__init__(ip, port)
        self.laser_ch = 5
        self.mw_ch = 4
        # self.laser_on()