from qick import AveragerProgram
from qick.qick_asm import AbsGenManager as qasm
from utils import ns2cycle

class T1(AveragerProgram):
    def initialize(self):       
        self.declare_gen(ch=self.cfg["green_ch"])
        self.declare_gen(ch=self.cfg["mw_ch"])

        # prepare Laser channel 
        freq = self.freq2reg(200, gen_ch=self.cfg["green_ch"], ro_ch=0)
        phase = self.deg2reg(0, gen_ch=self.cfg["green_ch"])
        self.default_pulse_registers(ch=self.cfg["green_ch"], freq=freq, phase=phase, gain=self.cfg["laser_power"])
        self.set_pulse_registers(ch=self.cfg["green_ch"], style="const", mode="oneshot", length=ns2cycle(100) ) # 원본
        
        # prepare mw_ch
        freq_mw = self.freq2reg(self.cfg['resonance_freq'], gen_ch=self.cfg["mw_ch"], ro_ch=0)
        phase_mw = self.deg2reg(0, gen_ch=self.cfg["mw_ch"])
        self.default_pulse_registers(ch=self.cfg["mw_ch"], freq=freq_mw, phase=phase_mw, gain=self.cfg["mw_power"])
        self.set_pulse_registers(ch=self.cfg["mw_ch"], style="const", mode="oneshot", length=ns2cycle(100)) #원본

        self.synci(200)

    def body(self):
        ##### FRONT (FOR REF VALUE) ####
        # spin initialization editing
        self.safe_regwi(rp=self.ch_page(self.cfg["green_ch"]), 
                        reg=self.sreg(self.cfg["green_ch"], "mode"),
                        imm=qasm.get_mode_code(self=self,
                                                length=ns2cycle(self.cfg['spin_init_time']),
                                                outsel='dds')
                        )
        self.pulse(ch=self.cfg["green_ch"], t=ns2cycle(self.cfg['laser_delay']))
        
        if self.cfg['without_pi']:
            self.synci(ns2cycle(self.cfg['spin_init_time'] + self.cfg['dwell_left'] + self.cfg['dwell_right']))
        else:
            self.synci(ns2cycle(self.cfg['spin_init_time'] + \
                self.cfg['dwell_left'] + self.cfg['x'] + self.cfg['pi_pulse'] + self.cfg['dwell_right']))
        
        # readout editing
        self.safe_regwi(rp=self.ch_page(self.cfg["green_ch"]), 
                        reg=self.sreg(self.cfg["green_ch"], "mode"),
                        imm=qasm.get_mode_code(self=self,
                                                length=ns2cycle(self.cfg['ro_len']),
                                                outsel='dds')
                        )
        self.pulse(ch=self.cfg["green_ch"], t=ns2cycle(self.cfg['laser_delay']))

        # detection
        self.trigger(pins=[0], t=ns2cycle(self.cfg['apd_delay'])) # this is count1

        # ################################
        # # borderline
        # sleep between front and back
        self.synci(ns2cycle(self.cfg['ro_len'] + 500))
        # ################################

        # # 2nd ####################################
        # spin initialization
        self.safe_regwi(rp=self.ch_page(self.cfg["green_ch"]), 
                        reg=self.sreg(self.cfg["green_ch"], "mode"),
                        imm=qasm.get_mode_code(self=self,
                                                length=ns2cycle(self.cfg['spin_init_time']),
                                                outsel='dds')
                        )
        self.pulse(ch=self.cfg["green_ch"], t=ns2cycle(self.cfg['laser_delay']))
        self.synci(ns2cycle(self.cfg['spin_init_time']))

        if self.cfg['without_pi']:
            self.synci(ns2cycle(self.cfg['dwell_left'] + self.cfg['x'] + self.cfg['dwell_right']))
        else:
        #MW setting
            self.safe_regwi(rp=self.ch_page(self.cfg["mw_ch"]), 
                            reg=self.sreg(self.cfg["mw_ch"], "mode"),
                            imm=qasm.get_mode_code(self=self,
                                                    length=ns2cycle(self.cfg['pi_pulse']),
                                                    outsel='dds')
                            )
            self.synci(ns2cycle(self.cfg['dwell_left']))
            self.pulse(ch=self.cfg["mw_ch"], t=ns2cycle(self.cfg['mw_delay']))
            self.synci(ns2cycle(self.cfg['pi_pulse'] + self.cfg['x'] + self.cfg['dwell_right']))
        
        #readout laser setting
        self.safe_regwi(rp=self.ch_page(self.cfg["green_ch"]), 
                        reg=self.sreg(self.cfg["green_ch"], "mode"),
                        imm=qasm.get_mode_code(self=self,
                                                length=ns2cycle(self.cfg['ro_len']),
                                                outsel='dds')
                        )
        self.pulse(ch=self.cfg["green_ch"], t=ns2cycle(self.cfg['laser_delay']))
        self.trigger(pins=[1], t=ns2cycle(self.cfg['apd_delay']))
        self.synci(ns2cycle(self.cfg['ro_len']))
        self.sync_all(ns2cycle(500))