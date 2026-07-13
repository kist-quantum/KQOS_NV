from qick import AveragerProgram

class laser(AveragerProgram):
    def initialize(self):
        self.laser_ch = self.cfg["laser_ch"]
        self.laser_power = self.cfg["laser_gain"]
        freq = self.freq2reg(self.cfg["laser_freq"], gen_ch=self.laser_ch, ro_ch=0)
        phase = self.deg2reg(0, gen_ch=self.laser_ch)
        
        self.declare_gen(ch=self.laser_ch)
        self.declare_readout(ch=0, length=1000, freq=200, gen_ch=0)
        self.default_pulse_registers(ch=self.laser_ch, freq=freq, phase=phase, gain=self.laser_power)
        self.set_pulse_registers(ch=self.laser_ch, style="const", mode="periodic", length=10000)
        self.synci(200)

    def body(self):
        self.pulse(ch=self.laser_ch, t=0)
        self.wait_all()
        self.sync_all()