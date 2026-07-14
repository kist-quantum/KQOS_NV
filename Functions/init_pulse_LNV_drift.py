from qick import AveragerProgram
from qick.qick_asm import AbsGenManager as qasm
import numpy as np
from utils import *

class init_pulse_LNV_drift(AveragerProgram):

    def initialize(self):
        # declaring generation channel
        self.declare_gen(ch = self.cfg["pulse_ch"])

        # #envelope
        idata = np.array([self.cfg["init_gain"]]*ns2cycle(self.cfg["init_len"]) + self.cfg["pre_pulse_gain"]*ns2cycle(self.cfg["pre_pulse_len"])
                         + self.cfg["pulse_gain"]*ns2cycle(self.cfg["pulse_len"]) + self.cfg["after_pulse_gain"]*ns2cycle(self.cfg["after_pulse_len"]) 
                         [-1*self.cfg["init_gain"]]*ns2cycle(self.cfg["init_len"]) + -1*self.cfg["pre_pulse_gain"]*ns2cycle(self.cfg["pre_pulse_len"])
                         + -1*self.cfg["pulse_gain"]*ns2cycle(self.cfg["pulse_len"]) + -1*self.cfg["after_pulse_gain"]*ns2cycle(self.cfg["after_pulse_len"]))
        self.add_pulse(self.cfg["pulse_ch"], name = "square_wave0", idata = idata, qdata = None)

        # Conver freq to DAC freq(ensuring it is an availabble ADC freq)
        freq = self.freq2reg(0, gen_ch = self.cfg["pulse_ch"], ro_ch = self.cfg["CNT1_memory"][0])
        phase = self.deg2reg(0, gen_ch = self.cfg["pulse_ch"])
        self.default_pulse_registers(ch = self.cfg["pulse_ch"], freq = freq, phase = phase, gain = self.cfg["pulse_gain"])
        self.set_pulse_registers(ch = self.cfg["pulse_ch"], style = "arb", mode = self.cfg["idata_mode"], waveform = "square_wave0")

        self.synci(200)

    def body(self):
        self.pulse(ch = self.cfg["pulse_ch"])
        self.trigger(pins = [1], t = ns2cycle(self.cfg["apd_delay"] + self.cfg['init_len'] + self.cfg["pre_pulse_len"] + self.cfg["pulse_len"]+ self.cfg["after_pulse_len"]))
        self.trigger(pins = [0], t = ns2cycle(self.cfg["apd_delay"] + self.cfg['init_len'] + self.cfg["pre_pulse_len"] + self.cfg["pulse_len"]+ self.cfg["after_pulse_len"]))
        self.sync_all(10)