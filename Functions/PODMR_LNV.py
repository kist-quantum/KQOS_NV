from qick import AveragerProgram
from qick.qick_asm import AbsGenManager as qasm
import numpy as np
from utils import *

class PODMR_LNV(AveragerProgram):

    def initialize(self):
        # declaring generation channel
        self.declare_gen(ch = self.cfg["lnv_ch1"])
        self.declare_gen(ch = self.cfg["lnv_ch2"])
        self.declare_gen(ch = self.cfg["mw_ch"])

        # prepare lnv_ch1
        freq = self.freq2reg(0, gen_ch = self.cfg["lnv_ch1"], ro_ch = self.cfg["CNT1_memory"][0])
        phase = self.deg2reg(0, gen_ch = self.cfg["lnv_ch1"])
        self.default_pulse_registers(ch = self.cfg["lnv_ch1"], style = "const", mode = "oneshot", freq = freq, phase = phase)

        # prepare lnv_ch2
        freq = self.freq2reg(0, gen_ch = self.cfg["lnv_ch2"], ro_ch = self.cfg["CNT1_memory"][0])
        phase = self.deg2reg(0, gen_ch = self.cfg["lnv_ch2"])
        self.default_pulse_registers(ch = self.cfg["lnv_ch2"], style = "const", mode = "oneshot", freq = freq, phase = phase)

        # prepare mw_ch
        freq_mw = self.freq2reg(self.cfg['x'], gen_ch = self.cfg["mw_ch"], ro_ch = self.cfg["CNT1_memory"][0])
        phase_mw = self.deg2reg(0, gen_ch = self.cfg["mw_ch"])
        self.default_pulse_registers(ch = self.cfg["mw_ch"], freq = freq_mw, phase = phase_mw, gain = self.cfg["mw_gain"])
        self.set_pulse_registers(ch = self.cfg["mw_ch"], style = "const", mode = "oneshot", length = ns2cycle(self.cfg['mw_len'])) 
        
        self.synci(200)

    def body(self):
        #1st (REF)
        self.set_pulse_registers(ch = self.cfg["lnv_ch1"], gain = self.cfg["init_gain"], length = ns2cycle(self.cfg["init_width"]))
        self.set_pulse_registers(ch = self.cfg["lnv_ch2"], gain = -1*self.cfg["init_gain"], length = ns2cycle(self.cfg["init_width"]))
        self.pulse(ch = self.cfg["lnv_ch1"])
        self.pulse(ch = self.cfg["lnv_ch2"])

        self.set_pulse_registers(ch = self.cfg["lnv_ch1"], gain = self.cfg["free_gain"], length = ns2cycle(self.cfg["free_width"]))
        self.set_pulse_registers(ch = self.cfg["lnv_ch2"], gain = -1*self.cfg["free_gain"], length = ns2cycle(self.cfg["free_width"]))
        self.pulse(ch = self.cfg["lnv_ch1"])
        self.pulse(ch = self.cfg["lnv_ch2"])

        self.set_pulse_registers(ch = self.cfg["lnv_ch1"], gain = self.cfg["readout_gain"], length = ns2cycle(self.cfg["readout_width"]))
        self.set_pulse_registers(ch = self.cfg["lnv_ch2"], gain = -1*self.cfg["readout_gain"], length = ns2cycle(self.cfg["readout_width"]))
        self.pulse(ch = self.cfg["lnv_ch1"])
        self.pulse(ch = self.cfg["lnv_ch2"])
        self.trigger(pins = [0], t = ns2cycle(self.cfg["apd_delay"]))
        
        self.set_pulse_registers(ch = self.cfg["lnv_ch1"], gain = self.cfg["after_gain"], length = ns2cycle(self.cfg["after_width"]))
        self.set_pulse_registers(ch = self.cfg["lnv_ch2"], gain = -1*self.cfg["after_gain"], length = ns2cycle(self.cfg["after_width"]))
        self.pulse(ch = self.cfg["lnv_ch1"])
        self.pulse(ch = self.cfg["lnv_ch2"])

        #2nd
        self.set_pulse_registers(ch = self.cfg["lnv_ch1"], gain = self.cfg["init_gain"], length = ns2cycle(self.cfg["init_width"]))
        self.set_pulse_registers(ch = self.cfg["lnv_ch2"], gain = -1*self.cfg["init_gain"], length = ns2cycle(self.cfg["init_width"]))
        self.pulse(ch = self.cfg["lnv_ch1"])
        self.pulse(ch = self.cfg["lnv_ch2"])

        self.set_pulse_registers(ch = self.cfg["lnv_ch1"], gain = self.cfg["free_gain"], length = ns2cycle(self.cfg["free_width"]))
        self.set_pulse_registers(ch = self.cfg["lnv_ch2"], gain = -1*self.cfg["free_gain"], length = ns2cycle(self.cfg["free_width"]))
        self.pulse(ch = self.cfg["lnv_ch1"])
        self.pulse(ch = self.cfg["lnv_ch2"])

        #MW Setting
        self.safe_regwi(rp=self.ch_page(self.cfg["mw_ch"]), 
                        reg=self.sreg(self.cfg["mw_ch"], "mode"),
                        imm=qasm.get_mode_code(self=self,
                                                length=ns2cycle(self.cfg['mw_offset']+self.cfg['mw_len']),
                                                outsel='dds')
                        )
        self.pulse(ch=self.cfg["mw_ch"], t=ns2cycle(self.cfg['mw_delay']))

        self.set_pulse_registers(ch = self.cfg["lnv_ch1"], gain = self.cfg["readout_gain"], length = ns2cycle(self.cfg["readout_width"]))
        self.set_pulse_registers(ch = self.cfg["lnv_ch2"], gain = -1*self.cfg["readout_gain"], length = ns2cycle(self.cfg["readout_width"]))
        self.pulse(ch = self.cfg["lnv_ch1"])
        self.pulse(ch = self.cfg["lnv_ch2"])
        self.trigger(pins = [1], t = ns2cycle(self.cfg["apd_delay"]))

        self.set_pulse_registers(ch = self.cfg["lnv_ch1"], gain = self.cfg["after_gain"], length = ns2cycle(self.cfg["after_width"]))
        self.set_pulse_registers(ch = self.cfg["lnv_ch2"], gain = -1*self.cfg["after_gain"], length = ns2cycle(self.cfg["after_width"]))
        self.pulse(ch = self.cfg["lnv_ch1"])
        self.pulse(ch = self.cfg["lnv_ch2"])

        self.sync_all(ns2cycle(2000))