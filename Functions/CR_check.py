import sys
from qick import AveragerProgram
from qick.qick_asm import AbsGenManager as qasm
from utils import *

class CR_check(AveragerProgram):
    def initialize(self):
        # self.cfg = self.cfg['cfg'] # this time parameters are set in nanoseconds, hence if needed covert to us
        self.declare_gen(ch=self.cfg["green_ch"])
        self.declare_gen(ch=self.cfg["red_ch1"])
        self.declare_gen(ch=self.cfg["red_ch2"])

        # prepare Green Laser channel 
        freq = self.freq2reg(200, gen_ch=self.cfg["green_ch"], ro_ch=0)
        phase = self.deg2reg(0, gen_ch=self.cfg["green_ch"])
        self.default_pulse_registers(ch=self.cfg["green_ch"], freq=freq, phase=phase, gain=self.cfg['green_ch_gain'])
        self.set_pulse_registers(ch=self.cfg["green_ch"], style="const", mode="oneshot", length=ns2cycle(self.cfg['spin_init_time'])) # 원본

        # prepare Red1 Laser channel 
        freq = self.freq2reg(200, gen_ch=self.cfg["red_ch1"], ro_ch=0)
        phase = self.deg2reg(0, gen_ch=self.cfg["red_ch1"])
        self.default_pulse_registers(ch=self.cfg["red_ch1"], freq=freq, phase=phase, gain=self.cfg["red_ch1_gain"])
        self.set_pulse_registers(ch=self.cfg["red_ch1"], style="const", mode="oneshot", length=ns2cycle(self.cfg["ro_len"])) # 원본


        # prepare Red2 Laser channel 
        freq = self.freq2reg(200, gen_ch=self.cfg["red_ch2"], ro_ch=0)
        phase = self.deg2reg(0, gen_ch=self.cfg["red_ch2"])
        self.default_pulse_registers(ch=self.cfg["red_ch2"], freq=freq, phase=phase, gain=self.cfg["red_ch2_gain"])
        self.set_pulse_registers(ch=self.cfg["red_ch2"], style="const", mode="oneshot", length=ns2cycle(self.cfg["ro_len"] )) # 원본

        self.synci(400)


    def body(self):
        ## run continuous mw_ch
        self.pulse(ch=self.cfg["green_ch"])
        
        #TODO delete here later
        self.pulse(ch=self.cfg["red_ch1"])
        self.pulse(ch=self.cfg["red_ch2"])
        self.trigger(pins=[0, 1], t = 0)
        self.sync_all(self.us2cycles(10))  ##  if it works well, it is good to be reduced to the smaller.