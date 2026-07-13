import sys
from qick import AveragerProgram
from qick.qick_asm import AbsGenManager as qasm
from utils import ns2cycle

class PLE(AveragerProgram):
    def initialize(self):
        # self.cfg = self.cfg['cfg'] # this time parameters are set in nanoseconds, hence if needed covert to us
        self.declare_gen(ch=self.cfg["mw_ch"])
        self.declare_gen(ch=self.cfg["green_ch"])
        self.declare_gen(ch=self.cfg["red_ch"])

        # prepare mw_ch
        freq_mw = self.freq2reg(self.cfg['mw_freq1'], gen_ch=self.cfg["mw_ch"], ro_ch=0)
        phase_mw = self.deg2reg(self.cfg["res_phase"], gen_ch=self.cfg["mw_ch"])
        self.default_pulse_registers(ch=self.cfg["mw_ch"],  phase=phase_mw, gain=self.cfg["mw_pulse_gain"])  ## for 2 different frequency. 24.10.29
        self.set_pulse_registers(ch=self.cfg["mw_ch"], freq= freq_mw, style="const", mode="oneshot", length=self.us2cycles(1))# self.cfg["pulse_len"]) ## for 2 different frequency. 24.10.29

        # prepare Green Laser channel 
        freq = self.freq2reg(200, gen_ch=self.cfg["green_ch"], ro_ch=0)
        phase = self.deg2reg(0, gen_ch=self.cfg["green_ch"])
        self.default_pulse_registers(ch=self.cfg["green_ch"], freq=freq, phase=phase, gain=self.cfg['green_laser_gain'])
        self.set_pulse_registers(ch=self.cfg["green_ch"], style="const", mode="oneshot", length=self.us2cycles(1) ) # 원본

        # prepare Red Laser channel 
        freq = self.freq2reg(200, gen_ch=self.cfg["red_ch"], ro_ch=0)
        phase = self.deg2reg(0, gen_ch=self.cfg["red_ch"])
        self.default_pulse_registers(ch=self.cfg["red_ch"], freq=freq, phase=phase, gain=self.cfg["red_laser_gain"])
        self.set_pulse_registers(ch=self.cfg["red_ch"], style="const", mode="oneshot", length=self.us2cycles(1) ) # 원본

        self.mw_freq_switchlength = 1 ## 1us

        self.synci(400)


    def body(self):
        ## run continuous mw_ch
        self.safe_regwi(rp=self.ch_page(self.cfg["green_ch"]), 
                        reg=self.sreg(self.cfg["green_ch"], "mode"),
                        imm=qasm.get_mode_code(self=self,
                                                length=self.us2cycles(self.cfg['green_laser_time'] / 1000), # 1000
                                                outsel='dds')
                        )
        self.pulse(ch=self.cfg["green_ch"])
        
        #TODO delete here later
        self.safe_regwi(rp=self.ch_page(self.cfg["red_ch"]), 
                        reg=self.sreg(self.cfg["red_ch"], "mode"),
                        imm=qasm.get_mode_code(self=self,
                                                length=self.us2cycles(self.cfg['red_laser_time'] / 1000),
                                                outsel='dds'))


        delay_for_red_laser = self.us2cycles(self.cfg['margin_between_laser'] / 1000) + self.us2cycles(self.cfg['green_laser_time'] / 1000)

        self.pulse(ch=self.cfg["red_ch"], t=delay_for_red_laser)

        delay_for_trigger = delay_for_red_laser + self.us2cycles(self.cfg['apd_time_delay'] / 1000)  + self.us2cycles(0.2)

        self.trigger(pins=[0, 1], t = delay_for_trigger)
        
        for jj in range(int(self.cfg['red_laser_time'] / 1000/2/self.mw_freq_switchlength)):  ## ns -> us,   fre1, freq2 -> divide by 2,   divided by length of MW.
            freq1 = self.freq2reg(self.cfg["mw_freq1"], gen_ch=self.cfg["mw_ch"], ro_ch=0)

            self.safe_regwi(rp=self.ch_page(self.cfg["mw_ch"]), 
                        reg=self.sreg(self.cfg["mw_ch"], "freq"),
                        imm= freq1)
                        # imm=self.cfg["pulse_freq1"])

            self.pulse(ch=self.cfg["mw_ch"],  t =self.us2cycles (jj*2*self.mw_freq_switchlength)+self.us2cycles(self.cfg['green_laser_time'] / 1000) ) ## need to calibration
            ##self.sync_all()
            freq2 = self.freq2reg(self.cfg["mw_freq2"], gen_ch=self.cfg["mw_ch"], ro_ch=0)

            self.safe_regwi(rp=self.ch_page(self.cfg["mw_ch"]), 
                        reg=self.sreg(self.cfg["mw_ch"], "freq"),
                        imm= freq2)
                        # imm=self.cfg["pulse_freq1"])

            self.pulse(ch=self.cfg["mw_ch"],    t =self.us2cycles ((jj*2*self.mw_freq_switchlength)+self.mw_freq_switchlength )+self.us2cycles(self.cfg['green_laser_time'] / 1000)) ## need to calibration

        self.sync_all(self.us2cycles(10))  ##  if it works well, it is good to be reduced to the smaller.

                
