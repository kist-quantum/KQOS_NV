from qick import AveragerProgram
from qick.qick_asm import AbsGenManager as qasm
import numpy as np
from utils import *

class check_EOM(AveragerProgram):

    def initialize(self):
        # declaring generation channel
        self.declare_gen(ch = self.cfg["red_ch"])
        self.declare_gen(ch = self.cfg["pulse_ch"])
        self.declare_gen(ch=self.cfg["green_ch"])

        # #envelope
        idata = np.array([self.cfg["idata_gain1"]]*self.cfg["idata_width1"] + [self.cfg["idata_gain2"]]*self.cfg["idata_width2"] + 
                         [self.cfg["idata_gain3"]]*self.cfg["idata_width3"] + [self.cfg["idata_gain4"]]*self.cfg["idata_width4"] +
                         [self.cfg["idata_gain5"]]*self.cfg["idata_width5"])
        self.add_pulse(self.cfg["pulse_ch"], name = "square_wave0", idata = idata, qdata = None)

        # green laser
        freq = self.freq2reg(200, gen_ch = self.cfg["green_ch"], ro_ch = 0)
        phase = self.deg2reg(0, gen_ch = self.cfg["green_ch"])
        self.default_pulse_registers(ch=self.cfg["green_ch"], freq=freq, phase=phase, gain=self.cfg['green_gain'])
        self.set_pulse_registers(ch=self.cfg["green_ch"], style="const", mode="oneshot", length=ns2cycle(self.cfg['init_len']))

        # prepare red channel 
        freq = self.freq2reg(200, gen_ch = self.cfg["red_ch"], ro_ch = self.cfg["ro_memory"][0])
        phase = self.deg2reg(0, gen_ch = self.cfg["red_ch"])
        self.default_pulse_registers(ch = self.cfg["red_ch"], freq = freq, phase = phase, gain = self.cfg["red_gain"])
        self.set_pulse_registers(ch = self.cfg["red_ch"], style = "const", mode = "oneshot", length = ns2cycle(self.cfg["red_len"])) # 원본

        # Conver freq to DAC freq(ensuring it is an availabble ADC freq)
        freq = self.freq2reg(0, gen_ch = self.cfg["pulse_ch"], ro_ch = self.cfg["ro_memory"][0])
        phase = self.deg2reg(0, gen_ch = self.cfg["pulse_ch"])
        self.default_pulse_registers(ch = self.cfg["pulse_ch"], freq = freq, phase = phase, gain = self.cfg["pulse_gain"])
        self.set_pulse_registers(ch = self.cfg["pulse_ch"], style = "arb", mode = self.cfg["idata_mode"], waveform = "square_wave0")

        self.synci(200)

    def body(self):
        self.pulse(ch = self.cfg["green_ch"], t = ns2cycle(self.cfg["green_delay"]))
        self.pulse(ch = self.cfg["pulse_ch"], t = ns2cycle(self.cfg["green_delay"] + self.cfg['init_len'] + self.cfg["pulse_delay"]))
        self.pulse(ch = self.cfg["red_ch"], t = ns2cycle(self.cfg["green_delay"] + self.cfg['init_len'] + self.cfg["red_delay"]))
        self.trigger(pins = [1], t = ns2cycle(self.cfg["green_delay"] + self.cfg['init_len'] + self.cfg["pulse_delay"] + self.cfg["apd_delay"]))
        self.trigger(pins = [0], t = ns2cycle(self.cfg["green_delay"] + self.cfg['init_len'] + self.cfg["pulse_delay"] + self.cfg["apd_delay"]))
        self.sync_all(3000)