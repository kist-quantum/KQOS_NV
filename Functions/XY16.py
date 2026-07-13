from qick import AveragerProgram
from qick.qick_asm import AbsGenManager as qasm
from utils import ns2cycle

class XY16(AveragerProgram):
    def initialize(self):
        self.cfg['half_pi_pulse'] = self.cfg['pi_pulse']/2 + self.cfg['mw_offset']
        self.declare_gen(ch=self.cfg["green_ch"])
        self.declare_gen(ch=self.cfg["mw_ch"])
        
        # prepare Laser channel 
        freq = self.freq2reg(200, gen_ch=self.cfg["green_ch"], ro_ch=0)
        phase = self.deg2reg(0, gen_ch=self.cfg["green_ch"])
        self.default_pulse_registers(ch=self.cfg["green_ch"], freq=freq, phase=phase, gain=self.cfg["laser_power"])
        self.set_pulse_registers(ch=self.cfg["green_ch"], style="const", mode="oneshot", length=ns2cycle(1000)) # 원본
        
        # prepare mw_ch
        freq_mw = self.freq2reg(self.cfg['resonance_freq'], gen_ch=self.cfg["mw_ch"], ro_ch=0)
        phase_mw = self.deg2reg(0, gen_ch=self.cfg["mw_ch"])
        self.default_pulse_registers(ch=self.cfg["mw_ch"], freq=freq_mw, phase=phase_mw, gain=self.cfg["mw_power"])
        self.set_pulse_registers(ch=self.cfg["mw_ch"], style="const", mode="oneshot", length=ns2cycle(1000)) #원본

        self.synci(200)

    # pulse 길이 설정은 함수에 포함되어 있지 않음
    # # tau-pi-tau
    def MW_pulse(self, phase):
        if phase == 'x':
            self.safe_regwi(rp=self.ch_page(self.cfg["mw_ch"]), 
                            reg=self.sreg(self.cfg["mw_ch"], "phase"),
                            imm=self.deg2reg(0)
                            )
        elif phase == 'y':
            self.safe_regwi(rp=self.ch_page(self.cfg["mw_ch"]), 
                            reg=self.sreg(self.cfg["mw_ch"], "phase"),
                            imm=self.deg2reg(90)
                            )
        elif phase == '-x':
            self.safe_regwi(rp=self.ch_page(self.cfg["mw_ch"]), 
                            reg=self.sreg(self.cfg["mw_ch"], "phase"),
                            imm=self.deg2reg(180)
                            )
        elif phase == '-y':
            self.safe_regwi(rp=self.ch_page(self.cfg["mw_ch"]), 
                            reg=self.sreg(self.cfg["mw_ch"], "phase"),
                            imm=self.deg2reg(270)
                            )
        self.synci(ns2cycle(self.cfg['x']))
        self.pulse(ch=self.cfg["mw_ch"], t=self.cfg['mw_delay'])
        self.synci(ns2cycle(self.cfg['pi_pulse'] + self.cfg['x']))
            
    def body(self):
        XY_16 = ['x', 'y', 'x', 'y', 'y', 'x', 'y', 'x', '-x', '-y', '-x', '-y', '-y', '-x', '-y', '-x']
        phase_arr = []
        phase_arr = XY_16*(self.cfg['N']//16)
        for index in range(self.cfg['N']%16):
            phase_arr.append(XY_16[index])
        ##### FRONT ####
        # spin initialization editing
        self.safe_regwi(rp=self.ch_page(self.cfg["green_ch"]), 
                        reg=self.sreg(self.cfg["green_ch"], "mode"),
                        imm=qasm.get_mode_code(self=self,
                                                length=ns2cycle(self.cfg['spin_init_time']),
                                                outsel='dds')
                        )
        self.pulse(ch=self.cfg["green_ch"], t=self.cfg['laser_delay'])
        self.synci(ns2cycle(self.cfg['spin_init_time'] + self.cfg['dwell_left']))
        
        # half_pi(x)
        self.safe_regwi(rp=self.ch_page(self.cfg["mw_ch"]), 
                        reg=self.sreg(self.cfg["mw_ch"], "mode"),
                        imm=qasm.get_mode_code(self=self,
                                                length=ns2cycle(self.cfg['half_pi_pulse']),
                                                outsel='dds')
                        )
        self.pulse(ch=self.cfg["mw_ch"], t=self.cfg['mw_delay'])
        self.synci(ns2cycle(self.cfg['half_pi_pulse']))

        # decoupling
        self.safe_regwi(rp=self.ch_page(self.cfg["mw_ch"]), 
                        reg=self.sreg(self.cfg["mw_ch"], "mode"),
                        imm=qasm.get_mode_code(self=self,
                                                length=ns2cycle(self.cfg['pi_pulse']),
                                                outsel='dds')
                        )
        for phase in phase_arr:
            self.MW_pulse(phase)
        
        # half_pi(-x)
        self.safe_regwi(rp=self.ch_page(self.cfg["mw_ch"]), 
                        reg=self.sreg(self.cfg["mw_ch"], "mode"),
                        imm=qasm.get_mode_code(self=self,
                                                length=ns2cycle(self.cfg['half_pi_pulse']),
                                                outsel='dds')
                        )
        self.safe_regwi(rp=self.ch_page(self.cfg["mw_ch"]), 
                            reg=self.sreg(self.cfg["mw_ch"], "phase"),
                            imm=self.deg2reg(180)
                            )
        self.pulse(ch=self.cfg["mw_ch"], t=self.cfg['mw_delay'])
        self.synci(ns2cycle(self.cfg['half_pi_pulse'] + self.cfg['dwell_right']))
        
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
        self.synci(ns2cycle((self.cfg['ro_len'] + 500)))
        # ################################

        # # 2nd ####################################
        # spin initialization
        self.safe_regwi(rp=self.ch_page(self.cfg["green_ch"]), 
                        reg=self.sreg(self.cfg["green_ch"], "mode"),
                        imm=qasm.get_mode_code(self=self,
                                                length=ns2cycle(self.cfg['spin_init_time']),
                                                outsel='dds')
                        )
        self.pulse(ch=self.cfg["green_ch"], t=ns2cycle((self.cfg['laser_delay'])))
        self.synci(ns2cycle(self.cfg['spin_init_time'] + self.cfg['dwell_left']))

        # half_pi(x)
        self.safe_regwi(rp=self.ch_page(self.cfg["mw_ch"]), 
                        reg=self.sreg(self.cfg["mw_ch"], "mode"),
                        imm=qasm.get_mode_code(self=self,
                                                length=ns2cycle(self.cfg['half_pi_pulse']),
                                                outsel='dds')
                        )
        self.safe_regwi(rp=self.ch_page(self.cfg["mw_ch"]), 
                            reg=self.sreg(self.cfg["mw_ch"], "phase"),
                            imm=self.deg2reg(0)
                            )
        self.pulse(ch=self.cfg["mw_ch"], t=self.cfg['mw_delay'])
        self.synci(ns2cycle(self.cfg['half_pi_pulse']))

        # decoupling
        self.safe_regwi(rp=self.ch_page(self.cfg["mw_ch"]), 
                        reg=self.sreg(self.cfg["mw_ch"], "mode"),
                        imm=qasm.get_mode_code(self=self,
                                                length=ns2cycle(self.cfg['pi_pulse']),
                                                outsel='dds')
                        )
        for phase in phase_arr:
            self.MW_pulse(phase)
        
        # half_pi(x)
        self.safe_regwi(rp=self.ch_page(self.cfg["mw_ch"]), 
                        reg=self.sreg(self.cfg["mw_ch"], "mode"),
                        imm=qasm.get_mode_code(self=self,
                                                length=ns2cycle(self.cfg['half_pi_pulse']),
                                                outsel='dds')
                        )
        self.safe_regwi(rp=self.ch_page(self.cfg["mw_ch"]), 
                            reg=self.sreg(self.cfg["mw_ch"], "phase"),
                            imm=self.deg2reg(0)
                            )
        self.pulse(ch=self.cfg["mw_ch"], t=self.cfg['mw_delay'])
        self.synci(ns2cycle(self.cfg['half_pi_pulse'] + self.cfg['dwell_right']))
        
        #readout laser setting
        self.safe_regwi(rp=self.ch_page(self.cfg["green_ch"]), 
                        reg=self.sreg(self.cfg["green_ch"], "mode"),
                        imm=qasm.get_mode_code(self=self,
                                                length=ns2cycle(self.cfg['ro_len']),
                                                outsel='dds')
                        )
        self.pulse(ch=self.cfg["green_ch"], t=ns2cycle(self.cfg['laser_delay']))
        self.trigger(pins=[1], t=ns2cycle((self.cfg['apd_delay'])))
        self.synci(ns2cycle((self.cfg['ro_len'])))
        self.sync_all(ns2cycle(0.5))