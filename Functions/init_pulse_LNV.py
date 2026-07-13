from qick import AveragerProgram
from qick.qick_asm import AbsGenManager as qasm
import numpy as np
from utils import *

class init_pulse_LNV(AveragerProgram):

    def initialize(self):
        # declaring generation channel
        self.declare_gen(ch = self.cfg["pulse_ch"])

        # #envelope
        idata = np.array([self.cfg["init_gain"]]*self.cfg["init_len"] + [self.cfg["pre_pulse_gain"]]*self.cfg["pre_pulse_len"] + 
                         [self.cfg["pulse_gain"]]*self.cfg["pulse_len"] + [self.cfg["after_pulse_gain"]]*self.cfg["after_pulse_len"])
        self.add_pulse(self.cfg["pulse_ch"], name = "square_wave0", idata = idata, qdata = None)
        # green laser
        freq = self.freq2reg(200, gen_ch = self.cfg["green_ch"], ro_ch = 0)
        phase = self.deg2reg(0, gen_ch = self.cfg["green_ch"])
        self.default_pulse_registers(ch=self.cfg["green_ch"], freq=freq, phase=phase, gain=self.cfg['green_gain'])
        self.set_pulse_registers(ch=self.cfg["green_ch"], style="const", mode="oneshot", length=ns2cycle(self.cfg['init_len']))
        
        # Conver freq to DAC freq(ensuring it is an availabble ADC freq)
        freq = self.freq2reg(0, gen_ch = self.cfg["pulse_ch"], ro_ch = self.cfg["CNT1_memory"][0])
        phase = self.deg2reg(0, gen_ch = self.cfg["pulse_ch"])
        self.default_pulse_registers(ch = self.cfg["pulse_ch"], freq = freq, phase = phase, gain = self.cfg["pulse_gain"])
        self.set_pulse_registers(ch = self.cfg["pulse_ch"], style = "arb", mode = self.cfg["idata_mode"], waveform = "square_wave0")

        self.synci(200)

    def body(self):
        self.pulse(ch = self.cfg["pulse_ch"], t = 0)
        self.trigger(pins = [1], t = 0)
        self.trigger(pins = [0], t = 0)
        self.sync_all(3000)