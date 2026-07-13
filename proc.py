from qick import *
import numpy as np
from Functions.laser_on import laser
from Functions.confocal import confocal
from Functions.ODMR import ODMR
from Functions.rabi_gg_PSB import rabi_gg_PSB
from Functions.ramsey import ramsey
from Functions.T1 import T1
from Functions.XY16 import XY16
from Functions.PLE import PLE
from Functions.rabi_gr_PSB import rabi_gr_PSB
from Functions.check_EOM import check_EOM
from Functions.spin_photon import spin_photon
from Functions.rabi_gr_ZPL import rabi_gr_ZPL
from Functions.rabi_gg_ZPL import rabi_gg_ZPL
from Functions.rabi_rr_PSB import rabi_rr_PSB
from Functions.PODMR import PODMR
from Functions.single_shot import single_shot
from Functions.PODMR_LNV import PODMR_LNV
from Functions.PODMR_LNV2 import PODMR_LNV2
from Functions.Rabi_GG_LNV import Rabi_GG_LNV
from Functions.init_pulse_LNV import init_pulse_LNV
from Functions.Echo_LNV import Echo_LNV
from Functions.green_AOM_timing import green_AOM_timing
from Functions.init_pulse_LNV_temp import init_pulse_LNV_temp
from Functions.Lifetime import Lifetime
from Functions.pulse_PSB_GR import pulse_PSB_GR
from Functions.pulse_ZPL_GR import pulse_ZPL_GR
from Functions.Nuclear_ODMR import Nuclear_ODMR
from Functions.pulse_gen import pulse_gen
from Functions.g2 import g2
from run_averager import run_and_count

# response data is dict that must have keys 'command' and 'results'.
def process(recv_data: dict, soc: QickSoc):
    response = {'command': recv_data['command'],
                'results': None}
    recv_data['soft_avgs'] = 1  # this parameter is mendatory

    if recv_data['command'] == 'laser_on':
        prog = laser(soc, recv_data)
        # prog.acquire_decimated(soc, load_pulses=True, progress=True)
        prog.run(soc, load_pulses=True)
    elif recv_data['command'] == 'laser_off':
        soc.reset_gens()
    elif recv_data['command'] == 'g2':
        response['results'] = g2(soc, recv_data)
    elif recv_data['command'] == 'confocal':
        prog = confocal(soc, recv_data)
        response['results'] = run_and_count(soc, prog, recv_data)
    elif recv_data['command'] == 'ODMR':
        prog = ODMR(soc, recv_data)
        response['results'] = run_and_count(soc, prog, recv_data)
    elif recv_data['command'] == 'rabi_gg_PSB':
        prog = rabi_gg_PSB(soc, recv_data)
        response['results'] = run_and_count(soc, prog, recv_data)
    elif recv_data['command'] == 'ramsey':
        prog = ramsey(soc, recv_data)
        response['results'] = run_and_count(soc, prog, recv_data)
    elif recv_data['command'] == 'T1':
        prog = T1(soc, recv_data)
        response['results'] = run_and_count(soc, prog, recv_data)
    elif recv_data['command'] == 'XY16':
        prog = XY16(soc, recv_data)
        response['results'] = run_and_count(soc, prog, recv_data)
    elif recv_data['command'] == 'PLE':
        prog = PLE(soc, recv_data)
        response['results'] = run_and_count(soc, prog, recv_data)
    elif recv_data['command'] == 'rabi_gr_PSB':
        prog = rabi_gr_PSB(soc, recv_data)
        response['results'] = run_and_count(soc, prog, recv_data)
    elif recv_data['command'] == 'check_EOM':
        prog = check_EOM(soc, recv_data)
        response['results'] = run_and_count(soc, prog, recv_data)
    elif recv_data['command'] == 'spin_photon':
        prog = spin_photon(soc, recv_data)
        response['results'] = run_and_count(soc, prog, recv_data)
    elif recv_data['command'] == 'rabi_gr_ZPL':
        prog = rabi_gr_ZPL(soc, recv_data)
        response['results'] = run_and_count(soc, prog, recv_data)
    elif recv_data['command'] == 'rabi_gg_ZPL':
        prog = rabi_gg_ZPL(soc, recv_data)
        response['results'] = run_and_count(soc, prog, recv_data)
    elif recv_data['command'] == 'rabi_rr_PSB':
        prog = rabi_rr_PSB(soc, recv_data)
        response['results'] = run_and_count(soc, prog, recv_data)
    elif recv_data['command'] == 'PODMR':
        prog = PODMR(soc, recv_data)
        response['results'] = run_and_count(soc, prog, recv_data)
    elif recv_data['command'] == 'single_shot':
        prog = single_shot(soc, recv_data)
        response['results'] = run_and_count(soc, prog, recv_data)
    elif recv_data['command'] == 'PODMR_LNV':
        prog = PODMR_LNV(soc, recv_data)
        response['results'] = run_and_count(soc, prog, recv_data)
    elif recv_data['command'] == 'Rabi_GG_LNV':
        prog = Rabi_GG_LNV(soc, recv_data)
        response['results'] = run_and_count(soc, prog, recv_data)
    elif recv_data['command'] == 'PODMR_LNV2':
        prog = PODMR_LNV2(soc, recv_data)
        response['results'] = run_and_count(soc, prog, recv_data)
    elif recv_data['command'] == 'init_pulse_LNV':
        prog = init_pulse_LNV(soc, recv_data)
        response['results'] = run_and_count(soc, prog, recv_data)
    elif recv_data['command'] == 'Echo_LNV':
        prog = Echo_LNV(soc, recv_data)
        response['results'] = run_and_count(soc, prog, recv_data)    
    elif recv_data['command'] == 'green_AOM_timing':
        prog = green_AOM_timing(soc, recv_data)
        response['results'] = run_and_count(soc, prog, recv_data)    
    elif recv_data['command'] == 'init_pulse_LNV_temp':
        prog = init_pulse_LNV_temp(soc, recv_data)
        response['results'] = run_and_count(soc, prog, recv_data)
    elif recv_data['command'] == 'Lifetime':
        prog = Lifetime(soc, recv_data)
        response['results'] = run_and_count(soc, prog, recv_data)
    elif recv_data['command'] == "pulse_PSB_GR":
        prog = pulse_PSB_GR(soc, recv_data)
        response['results'] = run_and_count(soc, prog, recv_data)
    elif recv_data['command'] == "pulse_ZPL_GR":
        prog = pulse_ZPL_GR(soc, recv_data)
        response['results'] = run_and_count(soc, prog, recv_data)
    elif recv_data['command'] == "Nuclear_ODMR":
        prog = Nuclear_ODMR(soc, recv_data)
        response['results'] = run_and_count(soc, prog, recv_data)
    elif recv_data['command'] == "pulse_gen":
        prog = pulse_gen(soc, recv_data)
        prog.acquire_decimated(soc, load_pulses=True, progress=True)
    
    return response
