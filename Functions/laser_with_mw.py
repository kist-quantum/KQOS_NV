from qick import AveragerProgram

class laser_with_mw(AveragerProgram):
    def initialize(self):
        # declaring generation channel
        self.declare_gen(ch=self.cfg["laser_ch"])
        self.declare_gen(ch=self.cfg['mw_ch'])
        
        # prepare laser_ch
        laser_freq = self.freq2reg(200, gen_ch=self.laser_ch, ro_ch=0)
        laser_phase = self.deg2reg(0, gen_ch=self.laser_ch)
        self.default_pulse_registers(ch=self.laser_ch, freq=laser_freq, phase=laser_phase, gain=self.laser_power)
        self.set_pulse_registers(ch=self.laser_ch, style="const", mode="periodic", length=10000)

        # prepare mw_ch
        laser_freq = self.freq2reg(200, gen_ch=self.laser_ch, ro_ch=0)
        laser_phase = self.deg2reg(0, gen_ch=self.laser_ch)
        self.default_pulse_registers(ch=self.laser_ch, freq=laser_freq, phase=laser_phase, gain=self.laser_power)
        self.set_pulse_registers(ch=self.laser_ch, style="const", mode="periodic", length=10000)
        
        self.synci(200)

    def body(self):
        self.pulse(ch=self.laser_ch, t=0)
        self.wait_all()
        self.sync_all()