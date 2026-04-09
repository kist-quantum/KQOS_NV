from qick import AveragerProgram
from qick.qick_asm import AbsGenManager as qasm
import numpy as np
from utils import *

class Rabi_GG_LNV(AveragerProgram):

    def initialize(self):
        # declaring generation channel
        self.declare_gen(ch = self.cfg["lnv_ch"])
        self.declare_gen(ch = self.cfg["ref_ch"])
        self.declare_gen(ch=self.cfg["mw_ch"])

        # prepare lnv_ch
        freq = self.freq2reg(0, gen_ch = self.cfg["lnv_ch"], ro_ch = self.cfg["ro_memory"][0])
        phase = self.deg2reg(0, gen_ch = self.cfg["lnv_ch"])
        self.default_pulse_registers(ch = self.cfg["lnv_ch"], style = "const", mode = "oneshot", freq = freq, phase = phase)

        # prepare ref_ch
        freq = self.freq2reg(0, gen_ch = self.cfg["ref_ch"], ro_ch = self.cfg["ro_memory"][0])
        phase = self.deg2reg(0, gen_ch = self.cfg["ref_ch"])
        self.default_pulse_registers(ch = self.cfg["ref_ch"], style = "const", mode = "oneshot", freq = freq, phase = phase)
        
        # prepare mw_ch
        freq_mw = self.freq2reg(self.cfg['mw_freq'], gen_ch = self.cfg["mw_ch"], ro_ch = self.cfg["ro_memory"][0])
        phase_mw = self.deg2reg(0, gen_ch = self.cfg["mw_ch"])
        self.default_pulse_registers(ch = self.cfg["mw_ch"], freq = freq_mw, phase = phase_mw, gain = self.cfg["mw_gain"])
        self.set_pulse_registers(ch = self.cfg["mw_ch"], style = "const", mode = "oneshot", length = ns2cycle(self.cfg['x'])) 
        
        self.synci(200)

    def body(self):
        #1st (REF)
        self.set_pulse_registers(ch = self.cfg["lnv_ch"], gain = self.cfg["init_gain"], length = ns2cycle(self.cfg["init_width"]))
        self.set_pulse_registers(ch = self.cfg["ref_ch"], gain = self.cfg["init_gain"], length = ns2cycle(self.cfg["init_width"]))
        self.pulse(ch = self.cfg["lnv_ch"])
        self.pulse(ch = self.cfg["ref_ch"])

        self.set_pulse_registers(ch = self.cfg["lnv_ch"], gain = self.cfg["free_gain"], length = ns2cycle(self.cfg["free_width"] + self.cfg['dwell_left'] + self.cfg['x'] + self.cfg['dwell_right']))
        self.set_pulse_registers(ch = self.cfg["ref_ch"], gain = self.cfg["free_gain"], length = ns2cycle(self.cfg["free_width"] + self.cfg['dwell_left'] + self.cfg['x'] + self.cfg['dwell_right']))
        self.pulse(ch = self.cfg["lnv_ch"])
        self.pulse(ch = self.cfg["ref_ch"])

        self.set_pulse_registers(ch = self.cfg["lnv_ch"], gain = self.cfg["readout_gain"], length = ns2cycle(self.cfg["readout_width"]))
        self.set_pulse_registers(ch = self.cfg["ref_ch"], gain = self.cfg["readout_gain"], length = ns2cycle(self.cfg["readout_width"]))
        self.pulse(ch = self.cfg["lnv_ch"], t = ns2cycle(self.cfg['dwell_right']))
        self.pulse(ch = self.cfg["ref_ch"], t = ns2cycle(self.cfg['dwell_right']))
        self.trigger(pins = [0], t = ns2cycle(self.cfg["apd_delay"]))
        
        self.set_pulse_registers(ch = self.cfg["lnv_ch"], gain = self.cfg["after_gain"], length = ns2cycle(self.cfg["after_width"]))
        self.set_pulse_registers(ch = self.cfg["ref_ch"], gain = self.cfg["after_gain"], length = ns2cycle(self.cfg["after_width"]))
        self.pulse(ch = self.cfg["lnv_ch"])
        self.pulse(ch = self.cfg["ref_ch"])

        self.synci(ns2cycle(1000 + self.cfg['x']))

        #2nd
        self.set_pulse_registers(ch = self.cfg["lnv_ch"], gain = self.cfg["init_gain"], length = ns2cycle(self.cfg["init_width"]))
        self.set_pulse_registers(ch = self.cfg["ref_ch"], gain = self.cfg["init_gain"], length = ns2cycle(self.cfg["init_width"]))
        self.pulse(ch = self.cfg["lnv_ch"])
        self.pulse(ch = self.cfg["ref_ch"])

        self.set_pulse_registers(ch = self.cfg["lnv_ch"], gain = self.cfg["free_gain"], length = ns2cycle(self.cfg["free_width"] + self.cfg['dwell_left'] + self.cfg['x'] + self.cfg['dwell_right']))
        self.set_pulse_registers(ch = self.cfg["ref_ch"], gain = self.cfg["free_gain"], length = ns2cycle(self.cfg["free_width"] + self.cfg['dwell_left'] + self.cfg['x'] + self.cfg['dwell_right']))
        self.pulse(ch = self.cfg["lnv_ch"])
        self.pulse(ch = self.cfg["ref_ch"])

        self.pulse(ch=self.cfg["mw_ch"], t=ns2cycle(self.cfg["init_width"] + self.cfg['dwell_left'] + self.cfg['mw_delay']))

        self.set_pulse_registers(ch = self.cfg["lnv_ch"], gain = self.cfg["readout_gain"], length = ns2cycle(self.cfg["readout_width"]))
        self.set_pulse_registers(ch = self.cfg["ref_ch"], gain = self.cfg["readout_gain"], length = ns2cycle(self.cfg["readout_width"]))
        self.pulse(ch = self.cfg["lnv_ch"])
        self.pulse(ch = self.cfg["ref_ch"])
        self.trigger(pins = [1], t = ns2cycle(self.cfg["apd_delay"]))

        self.set_pulse_registers(ch = self.cfg["lnv_ch"], gain = self.cfg["after_gain"], length = ns2cycle(self.cfg["after_width"]))
        self.set_pulse_registers(ch = self.cfg["ref_ch"], gain = self.cfg["after_gain"], length = ns2cycle(self.cfg["after_width"]))
        self.pulse(ch = self.cfg["lnv_ch"])
        self.pulse(ch = self.cfg["ref_ch"])

        self.sync_all(ns2cycle(3000))