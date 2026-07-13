from qick import AveragerProgram
from utils import ns2cycle

class confocal(AveragerProgram):
    def initialize(self):
        self.sync_all(ns2cycle(100))

    def body(self):
        self.trigger(pins=[0], t=self.us2cycles(self.cfg["trig_qick_offset"]) )
        self.sync_all(ns2cycle(100))
  