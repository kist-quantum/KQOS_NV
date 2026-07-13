# -*- coding: utf-8 -*-
"""
For toptica laser control
https://toptica.github.io/python-lasersdk/getting_started.html

Make sure to install usb driver
Follow:
https://www.toptica.com/products/tunable-diode-lasers/laser-driving-electronics/dlc-pro/#c2326
Download and extract
Right click on "dlcpro-usb-serial.inf" file and click install

Qudi is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Qudi is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Qudi. If not, see <http://www.gnu.org/licenses/>.

Copyright (c) the Qudi Developers. See the COPYRIGHT.txt file at the
top-level directory of this distribution and at <https://github.com/Ulm-IQO/qudi/>
"""

# from serial import Serial
# import TMCL
import toptica.lasersdk.dlcpro.v2_4_0 as dlcsdk
import toptica.lasersdk.decop as decop
import socket
import time
import numpy as np
import logging

class DLCcontrol:
    def __init__(self, ip=None):
        """Activate module."""
        self.ip = ip
        try:
            self.connection = dlcsdk.NetworkConnection(self.ip)
            self.dlc = dlcsdk.DLCpro(self.connection)
            self.Device_config = "DLC"
            self.set_voltage = 0
            self.dlc.open()
        except:
            logging.warning("The DLC doesn't connected")

    def activate(self):
        """Activate module."""
        self.dlc.open()

    def Deactivate(self):
        """deActivate module."""
        self.dlc.close()

    def get_device_info(self):
        return self.Device_config

    def get_piezo_voltage(self):
        return self.dlc.laser1.dl.pc.voltage_act.get(), self.set_voltage

    def set_piezo_voltage(self, voltage):
        self.v = voltage
        self.set_voltage = voltage
        self.dlc.laser1.dl.pc.voltage_set.set(voltage)

    def get_current(self):
        return self.dlc.laser1.dl.cc.current_set.get()

    def get_wavelength(self):
        WL = self.dlc.laser1.ctl.wavelength_set.get()
        print(WL)

    def set_wavelength(self, wavelength):
        # self.dlc.laser1.ctl.wavelength_set.set(wavelength)
        self.dlc.laser1.ctl.wavelength_set.set(wavelength)

    def set_current(self, current):
        self.dlc.laser1.dl.cc.current_set.set(current)

    def read_wavelength(self):
        msg = "WAVELENGTH {:d}".format(self.channel)
        self.socket.sendall(msg.encode())
        res = bytes.decode(self.socket.recv(1024))
        if res != "NONE":
            words = res.split()
            if len(words) == 2 and words[0] == "WAVELENGTH":
                return float(words[1])
            else:
                return 0.0
        else:

            return 0.0

    def scan(self, amp, offset, frequency):
        self.dlc.laser2.scan.amplitude.set(amp)
        self.dlc.laser2.scan.offset.set(offset)
        self.dlc.laser2.scan.frequency.set(frequency)
        self.dlc.laser2.scan.enabled.set(True)

    def wide_scan(self, start, end):
        self.dlc.laser2.wide_scan.scan_begin.set(start)
        self.dlc.laser2.wide_scan.scan_end.set(end)
        self.dlc.laser2.wide_scan.start()

    def get_wide_scan_state(self):
        return self.dlc.laser2.wide_scan.state.get()

    def stop_scan(self):
        self.dlc.laser2.scan.enabled.set(False)

    def stop_wide_scan(self):
        self.dlc.laser2.wide_scan.stop()

    def stabilize_wavelength(self):
        self.stabilize = True
        self.sig_stabilize.emit()

    def stop_stabilization(self):
        self.stabilize = False
