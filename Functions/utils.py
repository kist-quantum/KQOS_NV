import numpy as np
from PySide6.QtWidgets import QWidget, QFileDialog
import threading

# 측정 결과 저장 경로
FILEPATH = f'C://Users/oprs1/Measurement'
#laser config

def find_nearest(array: list, value: object) -> list:
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx], idx

def explorer():
    explorer = QWidget()
    filename = QFileDialog.getOpenFileName(explorer, 'Open File')
    return filename

def lorentzian(x, x0, HWFM, y0, A):
    return (HWFM*A) / ((x-x0)**2 + (1*HWFM)**2) + y0

def damped_sin(x, constant, amplitude, omega, phase, y0):
    return np.exp(-1*constant*x) * amplitude * np.sin(omega * x + phase) + y0

def FFT(x, sub):
    N = len(x)
    T = (x[-1] - x[0])/N
    y_f = np.fft.fft(sub)
    x_f = np.linspace(0, 1.0/(2.0*T), N//2) * 2
    y_f = 2.0/N * np.abs(y_f[:N//2])
    return x_f/2, y_f

def power_exp(x, A, tau, s):
    return A * np.exp(-(x/tau)**s)

class Flag(threading.Event):
    """A wrapper for the typical event class to allow for overriding the
    `__bool__` magic method, since it looks nicer.
    """

    def __bool__(self):
        return self.is_set()