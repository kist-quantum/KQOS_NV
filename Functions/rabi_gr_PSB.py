from qick import AveragerProgram
from qick.qick_asm import AbsGenManager as qasm
from utils import ns2cycle

class rabi_gr_PSB(AveragerProgram):

    def initialize(self):
        # assert  2500 <= self.cfg['mw_freq'] and  self.cfg['mw_freq'] <= 3000
        self.declare_gen(ch=self.cfg["mw_ch"])
        self.declare_gen(ch=self.cfg["green_ch"])
        self.declare_gen(ch=self.cfg["red_ch"])
        # prepare mw_ch
        freq_mw = self.freq2reg(self.cfg['mw_freq'], gen_ch=self.cfg["mw_ch"], ro_ch=0)
        phase_mw = self.deg2reg(0, gen_ch=self.cfg["mw_ch"])
        self.default_pulse_registers(ch=self.cfg["mw_ch"], freq=freq_mw, phase=phase_mw, gain=self.cfg["mw_power"])
        self.set_pulse_registers(ch=self.cfg["mw_ch"], style="const", mode="oneshot", length=ns2cycle(self.cfg['x'])) #원본
        # prepare green Laser channel 
        freq = self.freq2reg(200, gen_ch=self.cfg["green_ch"], ro_ch=0)
        phase = self.deg2reg(0, gen_ch=self.cfg["green_ch"])
        self.default_pulse_registers(ch=self.cfg["green_ch"], freq=freq, phase=phase, gain=self.cfg["green_laser_gain"])
        self.set_pulse_registers(ch=self.cfg["green_ch"], style="const", mode="oneshot", length=ns2cycle(self.cfg['spin_init_time'])) # 원본
        # prepare Red Laser channel 
        freq = self.freq2reg(200, gen_ch=self.cfg["red_ch"], ro_ch=0)
        phase = self.deg2reg(0, gen_ch=self.cfg["red_ch"])
        self.default_pulse_registers(ch=self.cfg["red_ch"], freq=freq, phase=phase, gain=self.cfg["red_laser_gain"])
        self.set_pulse_registers(ch=self.cfg["red_ch"], style="const", mode="oneshot", length=ns2cycle(self.cfg['red_ro_time']) ) # 원본
        self.synci(200)

    def body(self):
        ##### FRONT (FOR REF VALUE) ####
        # spin initialization editing
        self.pulse(ch=self.cfg["green_ch"], t=0)
        
        # readout editing
        time_cursor = ns2cycle(self.cfg['spin_init_time'] + self.cfg['dwell_left'] + self.cfg['x'] + self.cfg['dwell_right'])
        self.pulse(ch=self.cfg["red_ch"], t= time_cursor + ns2cycle(self.cfg['red_delay']))
        self.trigger(pins=[0], t= time_cursor + ns2cycle(self.cfg['apd_delay'])) # this is count1
        
        # ################################
        # # borderline
        # sleep between front and back
        # ################################
        self.sync_all(ns2cycle(1000))

        # # 2nd ####################################
        # spin initialization
        self.pulse(ch=self.cfg["green_ch"], t=0)

        #MW setting
        time_cursor2 = ns2cycle(self.cfg['spin_init_time'] + self.cfg['dwell_left'])
        self.pulse(ch=self.cfg["mw_ch"], t = time_cursor2 + ns2cycle(self.cfg['mw_delay']))
        time_cursor2 += ns2cycle(self.cfg['dwell_right'] + self.cfg['x'])
        
        #readout laser setting
        self.pulse(ch=self.cfg["red_ch"], t = time_cursor2 + ns2cycle(self.cfg['red_delay']))
        self.trigger(pins=[1], t = time_cursor2 + ns2cycle((self.cfg['apd_delay'])))
        
        self.sync_all(ns2cycle(1000))