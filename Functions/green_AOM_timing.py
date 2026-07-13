from qick import AveragerProgram
from qick.qick_asm import AbsGenManager as qasm
from utils import ns2cycle

class green_AOM_timing(AveragerProgram):
    def initialize(self):
        self.declare_gen(ch = self.cfg["green_ch"])
        
        # prepare Laser channel 
        freq = self.freq2reg(200, gen_ch = self.cfg["green_ch"], ro_ch = 0)
        phase = self.deg2reg(0, gen_ch = self.cfg["green_ch"])
        self.default_pulse_registers(ch = self.cfg["green_ch"], freq = freq, phase = phase, gain = self.cfg['green_gain'])
        self.set_pulse_registers(ch = self.cfg["green_ch"], style = "const", mode = "oneshot", length =  ns2cycle(self.cfg['ro_len'])) # 원본

        self.synci(200)

    def body(self):
        ##### FRONT (FOR REF VALUE) ####
        # spin initialization editing
        self.pulse(ch=self.cfg["green_ch"], t=self.cfg["green_delay"])
        self.trigger(pins=[0, 1], t = ns2cycle(self.cfg["x"]))
        self.sync_all(10)