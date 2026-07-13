from qick import AveragerProgram
from qick.qick_asm import AbsGenManager as qasm
from utils import *

class ODMR(AveragerProgram):
    def initialize(self):
        self.declare_gen(ch=self.cfg["mw_ch"])
        self.declare_gen(ch=self.cfg["green_ch"])
        
        ## Laser setting
        freq = self.freq2reg(200, gen_ch=self.cfg["green_ch"], ro_ch=0)
        phase = self.deg2reg(0, gen_ch=self.cfg["green_ch"])
        self.default_pulse_registers(ch=self.cfg["green_ch"], freq=freq, phase=phase, gain=self.cfg['laser_power'])
        self.set_pulse_registers(ch=self.cfg["green_ch"], style="const", mode="periodic", length=ns2cycle(self.cfg['ro_len']))
        
        # Convert frequency to DAC frequency (ensuring it is an available ADC frequency)
        freq_mw = self.freq2reg(self.cfg['x'], gen_ch=self.cfg["mw_ch"], ro_ch=0)
        phase_mw = self.deg2reg(0, gen_ch=self.cfg["mw_ch"])
        self.default_pulse_registers(ch=self.cfg["mw_ch"], freq=freq_mw, phase=phase_mw, gain=self.cfg["mw_power"])
        self.set_pulse_registers(ch=self.cfg["mw_ch"], style="const", mode="oneshot", length=ns2cycle(self.cfg['ro_len']))
        self.safe_regwi(rp = self.ch_page(self.cfg["mw_ch"]),
                        reg = self.sreg(self.cfg["mw_ch"], 'mode'),
                        imm = qasm.get_mode_code(self=self,
                                                length=ns2cycle(self.cfg['ro_len']),
                                                outsel='dds')
                        )        
        self.pulse(ch=self.cfg["green_ch"],t=0)

        # self.sync_all(self.us2cycles(200))
        self.sync_all(200)

    def body(self):
        # 1st
        self.pulse(ch=self.cfg["mw_ch"], t=0)
        self.trigger(pins=[0], t = ns2cycle(self.cfg["apd_delay"]))
        self.synci(ns2cycle(self.cfg['ro_len']+500))  # gap time between two APD

        # 2nd 
        self.trigger(pins=[1], t = ns2cycle(self.cfg["apd_delay"]))
        self.synci(ns2cycle(self.cfg['ro_len']))
        self.sync_all(5000)