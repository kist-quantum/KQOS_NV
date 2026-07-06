from qick import AveragerProgram
from qick.qick_asm import AbsGenManager as qasm
from utils import *

class Nuclear_ODMR(AveragerProgram):
    def initialize(self):
        self.declare_gen(ch = self.cfg["green_ch"])
        self.declare_gen(ch = self.cfg["mw_ch"])
        self.declare_gen(ch = self.cfg["RF_ch"])
        
        # prepare Laser channel 
        freq = self.freq2reg(self.cfg["laser_freq"], gen_ch = self.cfg["green_ch"], ro_ch = 0)
        phase = self.deg2reg(0, gen_ch = self.cfg["green_ch"])
        self.default_pulse_registers(ch = self.cfg["green_ch"], freq = freq, phase = phase, gain = self.cfg['green_gain'])
        self.set_pulse_registers(ch = self.cfg["green_ch"], style = "const", mode = "oneshot", length = ns2cycle(self.cfg['spin_init_time']))

        # prepare mw_ch
        phase_mw = self.deg2reg(0, gen_ch=self.cfg["mw_ch"])
        self.default_pulse_registers(ch=self.cfg["mw_ch"], phase=phase_mw)
        
        # prepare RF_ch
        freq_RF = self.freq2reg(self.cfg["x"], gen_ch=self.cfg["RF_ch"], ro_ch=0)
        phase_RF = self.deg2reg(0, gen_ch=self.cfg["RF_ch"])
        self.default_pulse_registers(ch=self.cfg["RF_ch"], freq=freq_RF, phase=phase_RF, gain=self.cfg["RF_gain"])
        self.set_pulse_registers(ch=self.cfg["RF_ch"], style="const", mode="oneshot", length=ns2cycle(self.cfg["ro_len"]))

        self.sync_all(200)
        
    def body(self):
        ### Reference ###
        # spin initialization
        self.safe_regwi(rp = self.ch_page(self.cfg["green_ch"]), reg = self.sreg(self.cfg["green_ch"], "mode"),imm = qasm.get_mode_code(self = self,length = ns2cycle(self.cfg['spin_init_time']),outsel = 'dds'))
        self.pulse(ch = self.cfg["green_ch"], t = ns2cycle(self.cfg['green_delay']))
        time_cursor_1 = self.cfg['spin_init_time'] + self.cfg['dwell_left']
        
        # MW setting
        freq_mw1 = self.freq2reg(self.cfg["mw_freq1"], gen_ch=self.cfg["mw_ch"], ro_ch=0)
        self.set_pulse_registers(ch=self.cfg["mw_ch"], freq=freq_mw1, style="const", mode="oneshot", gain=self.cfg["mw_gain"], length=ns2cycle(self.cfg["mw_pi_len1"]))
        self.pulse(ch=self.cfg["mw_ch"], t=ns2cycle(time_cursor_1 + self.cfg["mw_delay"]))
        time_cursor_1 += (self.cfg["mw_delay"] + self.cfg["mw_pi_len1"] + self.cfg["mw_gap"])
        
        freq_mw2 = self.freq2reg(self.cfg["mw_freq2"], gen_ch=self.cfg["mw_ch"], ro_ch=0)
        self.set_pulse_registers(ch=self.cfg["mw_ch"], freq=freq_mw2, style="const", mode="oneshot", gain=self.cfg["mw_gain"], length=ns2cycle(self.cfg["mw_pi_len2"]))
        self.pulse(ch=self.cfg["mw_ch"], t=ns2cycle(time_cursor_1 + self.cfg["mw_delay"]))
        time_cursor_1 += (self.cfg["mw_delay"] + self.cfg["mw_pi_len2"] + self.cfg["dwell_right"])
        
        # readout
        self.safe_regwi(rp = self.ch_page(self.cfg["green_ch"]), reg = self.sreg(self.cfg["green_ch"], "mode"), imm = qasm.get_mode_code(self = self, length = ns2cycle(self.cfg['ro_len']), outsel = 'dds'))
        self.pulse(ch = self.cfg["green_ch"], t = ns2cycle(time_cursor_1 + self.cfg['green_delay']))
        self.trigger(pins = [0], t = ns2cycle(time_cursor_1 + self.cfg['apd_delay']))
        
        # sleep between front and back
        self.sync_all(ns2cycle(1000))
        
        
        ### Signal ###
        # spin initialization
        self.safe_regwi(rp = self.ch_page(self.cfg["green_ch"]), reg = self.sreg(self.cfg["green_ch"], "mode"),imm = qasm.get_mode_code(self = self,length = ns2cycle(self.cfg['spin_init_time']),outsel = 'dds'))
        self.pulse(ch = self.cfg["green_ch"], t = ns2cycle(self.cfg['green_delay']))
        time_cursor_2 = self.cfg['spin_init_time'] + self.cfg['dwell_left']
        
        # MW setting
        freq_mw1 = self.freq2reg(self.cfg["mw_freq1"], gen_ch=self.cfg["mw_ch"], ro_ch=0)
        self.set_pulse_registers(ch=self.cfg["mw_ch"], freq=freq_mw1, style="const", mode="oneshot", gain=self.cfg["mw_gain"], length=ns2cycle(self.cfg["mw_pi_len1"]))
        self.pulse(ch=self.cfg["mw_ch"], t=ns2cycle(time_cursor_2 + self.cfg["mw_delay"]))
        time_cursor_2 += (self.cfg["mw_delay"] + self.cfg["mw_pi_len1"] + self.cfg["mw_gap"])
        
        freq_mw2 = self.freq2reg(self.cfg["mw_freq2"], gen_ch=self.cfg["mw_ch"], ro_ch=0)
        self.set_pulse_registers(ch=self.cfg["mw_ch"], freq=freq_mw2, style="const", mode="oneshot", gain=self.cfg["mw_gain"], length=ns2cycle(self.cfg["mw_pi_len2"]))
        self.pulse(ch=self.cfg["mw_ch"], t=ns2cycle(time_cursor_2 + self.cfg["mw_delay"]))
        time_cursor_2 += (self.cfg["mw_delay"] + self.cfg["mw_pi_len2"] + self.cfg["mw_RF_gap"])
        
        # RF setting
        self.safe_regwi(rp = self.ch_page(self.cfg["RF_ch"]), reg = self.sreg(self.cfg["RF_ch"], "mode"),imm = qasm.get_mode_code(self = self,length = ns2cycle(self.cfg['ro_len']),outsel = 'dds'))
        self.pulse(ch = self.cfg["RF_ch"], t = ns2cycle(time_cursor_2 + self.cfg['RF_delay']))
        time_cursor_2 += (self.cfg["RF_delay"] + self.cfg["ro_len"] + self.cfg["dwell_right"])
        
        # readout
        self.safe_regwi(rp = self.ch_page(self.cfg["green_ch"]), reg = self.sreg(self.cfg["green_ch"], "mode"), imm = qasm.get_mode_code(self = self, length = ns2cycle(self.cfg['ro_len']), outsel = 'dds'))
        self.pulse(ch = self.cfg["green_ch"], t = ns2cycle(time_cursor_2 + self.cfg['green_delay']))
        self.trigger(pins = [1], t = ns2cycle(time_cursor_2 + self.cfg['apd_delay']))
        
        self.sync_all(500)