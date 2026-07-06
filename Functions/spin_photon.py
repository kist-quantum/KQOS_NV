from qick import AveragerProgram
from qick.qick_asm import AbsGenManager as qasm
from utils import ns2cycle

class spin_photon(AveragerProgram):

    def initialize(self):
        self.declare_gen(ch=self.cfg["green_ch"])
        self.declare_gen(ch=self.cfg["red_ch"])
        self.declare_gen(ch=self.cfg["mw_ch"])
        
        # prepare mw_ch
        freq_mw = self.freq2reg(self.cfg['mw_freq'], gen_ch=self.cfg["mw_ch"], ro_ch=self.cfg["CNT1_memory"][0])
        phase_mw = self.deg2reg(0, gen_ch=self.cfg["mw_ch"])
        self.default_pulse_registers(ch=self.cfg["mw_ch"], freq=freq_mw, phase=phase_mw, gain=self.cfg["mw_gain"])
        self.set_pulse_registers(ch=self.cfg["mw_ch"], style="const", mode="oneshot", length=ns2cycle(self.cfg["mw_pi_pulse"])) #원본

        # prepare green channel 
        freq = self.freq2reg(200, gen_ch=self.cfg["green_ch"], ro_ch=self.cfg["CNT1_memory"][0])
        phase = self.deg2reg(0, gen_ch=self.cfg["green_ch"])
        self.default_pulse_registers(ch=self.cfg["green_ch"], freq=freq, phase=phase, gain=self.cfg["green_gain"])
        self.set_pulse_registers(ch=self.cfg["green_ch"], style="const", mode="oneshot", length=ns2cycle(self.cfg["spin_init_time"]) ) # 원본

        # prepare red channel 
        freq = self.freq2reg(200, gen_ch=self.cfg["red_ch"], ro_ch=self.cfg["CNT1_memory"][0])
        phase = self.deg2reg(0, gen_ch=self.cfg["red_ch"])
        self.default_pulse_registers(ch=self.cfg["red_ch"], freq=freq, phase=phase, gain=self.cfg["red_gain"])
        self.set_pulse_registers(ch=self.cfg["red_ch"], style="const", mode="oneshot", length=ns2cycle(self.cfg["ro_len"]) ) # 원본

        self.synci(1000)

    def body(self):
        ##### FRONT (FOR REF VALUE) ####
        # spin initialization
        self.pulse(ch=self.cfg["green_ch"], t = 0)

        time_cursor = self.cfg['spin_init_time'] + self.cfg['dwell_left']

        # pi/2 pulse
        self.safe_regwi(rp=self.ch_page(self.cfg["mw_ch"]), 
                        reg=self.sreg(self.cfg["mw_ch"], "mode"),
                        imm=qasm.get_mode_code(self=self,
                                                length=ns2cycle(self.cfg['mw_pi_pulse']/2),
                                                outsel='dds')
                        )
        self.pulse(ch=self.cfg["mw_ch"], t=ns2cycle(time_cursor + self.cfg['mw_delay']/2))

        time_cursor += self.cfg['mw_pi_pulse']/2 + self.cfg['dwell_right']

        # # readout 300ns 0
        self.pulse(ch=self.cfg["red_ch"], t=ns2cycle(time_cursor + self.cfg['red_delay']))
        self.trigger(pins=[0,1], t=ns2cycle(time_cursor + self.cfg['apd_delay']))
        time_cursor += self.cfg['ro_len'] + self.cfg['dwell_left']
        
        # pi pulse
        self.safe_regwi(rp=self.ch_page(self.cfg["mw_ch"]), 
                        reg=self.sreg(self.cfg["mw_ch"], "mode"),
                        imm=qasm.get_mode_code(self=self,
                                                length=ns2cycle(self.cfg['mw_pi_pulse']),
                                                outsel='dds')
                )
        self.pulse(ch = self.cfg["mw_ch"], t = ns2cycle(time_cursor + self.cfg['mw_delay'])) # ns2cycle(self.cfg['mw_delay']))
        time_cursor += self.cfg['mw_pi_pulse'] + self.cfg['dwell_right']

        # readout 300ns 1
        self.pulse(ch=self.cfg["red_ch"], t=ns2cycle(time_cursor + self.cfg['red_delay']))
        self.trigger(pins=[2,3], t=ns2cycle(time_cursor + self.cfg['apd_delay']))
        time_cursor += self.cfg['ro_len'] + self.cfg['dwell_left']
        
        time_cursor += self.cfg['dwell_right']

        # readout 300ns 2
        self.pulse(ch=self.cfg["red_ch"], t=ns2cycle(time_cursor + self.cfg['red_delay']))
        self.trigger(pins=[4,5], t=ns2cycle(time_cursor + self.cfg['apd_delay']))
        time_cursor += self.cfg['ro_len'] + self.cfg['dwell_left']

        # pi pulse
        self.pulse(ch = self.cfg["mw_ch"], t=ns2cycle(time_cursor + self.cfg['mw_delay']))
        time_cursor += self.cfg['mw_pi_pulse'] + self.cfg['dwell_right']

        # readout 300ns 3
        self.pulse(ch=self.cfg["red_ch"], t=ns2cycle(time_cursor + self.cfg['red_delay']))
        self.trigger(pins=[6,7], t=ns2cycle(time_cursor + self.cfg['apd_delay']))

        # end
        self.sync_all(ns2cycle(400))