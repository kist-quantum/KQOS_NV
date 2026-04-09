from qick import AveragerProgram
from qick.qick_asm import AbsGenManager as qasm
import numpy as np
from utils import *

class single_shot(AveragerProgram):

    def initialize(self):
        # declaring generation channel
        self.declare_gen(ch = self.cfg["red_ch"])
        self.declare_gen(ch = self.cfg["green_ch"])
        self.declare_gen(ch = self.cfg["pulse_ch"])

        # #envelope
        idata = np.array([self.cfg["idata_gain1"]]*self.cfg["idata_width1"] + [self.cfg["idata_gain2"]]*self.cfg["idata_width2"] + [self.cfg["idata_gain3"]]*self.cfg["idata_width3"])
        self.add_pulse(self.cfg["pulse_ch"], name = "square_wave0", idata = idata, qdata = None)

        # prepare green channel
        freq = self.freq2reg(200, gen_ch = self.cfg["green_ch"], ro_ch = 0)
        phase = self.deg2reg(0, gen_ch = self.cfg["green_ch"])
        self.default_pulse_registers(ch = self.cfg["green_ch"], freq = freq, phase = phase, gain = self.cfg['green_gain'])
        self.set_pulse_registers(ch = self.cfg["green_ch"], style = "const", mode = "oneshot", length = ns2cycle(self.cfg['spin_init_time'])) # 원본

        # prepare red channel 
        freq = self.freq2reg(200, gen_ch = self.cfg["red_ch"], ro_ch = self.cfg["ro_memory"][0])
        phase = self.deg2reg(0, gen_ch = self.cfg["red_ch"])
        self.default_pulse_registers(ch = self.cfg["red_ch"], freq = freq, phase = phase, gain = self.cfg["red_gain"])
        self.set_pulse_registers(ch = self.cfg["red_ch"], style = "const", mode = "oneshot", length = self.cfg["red_len"]) # 원본

        # Conver freq to DAC freq(ensuring it is an availabble ADC freq)
        freq = self.freq2reg(0, gen_ch = self.cfg["pulse_ch"], ro_ch = self.cfg["ro_memory"][0])
        phase = self.deg2reg(0, gen_ch = self.cfg["pulse_ch"])
        self.default_pulse_registers(ch = self.cfg["pulse_ch"], freq = freq, phase = phase, gain = self.cfg["pulse_gain"])
        self.set_pulse_registers(ch = self.cfg["pulse_ch"], style = "arb", mode = self.cfg["idata_mode"], waveform = "square_wave0")

        self.synci(200)

    def body(self):
        # self.reset_gen()
        # self.reset_phase(ch = self.cfg["pulse_ch"], t = 0)
        self.pulse(ch = self.cfg['green_ch'], t = self.cfg['green_delay'])
        self.pulse(ch = self.cfg["pulse_ch"], t = self.cfg['green_delay'] + self.cfg['term'] + self.cfg["pulse_delay"])
        self.pulse(ch = self.cfg["red_ch"], t = self.cfg['green_delay'] + self.cfg['term'] + self.cfg["red_delay"])
        self.trigger(pins = [1], t = self.cfg['green_delay'] + self.cfg['term'])
        self.trigger(pins = [0], t = self.cfg['green_delay'] + self.cfg['term'])
        self.sync_all(ns2cycle(2000))