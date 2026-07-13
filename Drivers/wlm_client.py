import logging
import threading, struct
import time, queue, random, socket
from queue import Queue
import ast

class WLMProducer:
    def __init__(self, ip, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect((ip, port))
        except:
            logging.warning('wlm server does not connected')
        self.delay = 0.2 # delay between wavelength requests
        self.WL_list = {'1' : None, '2' : None, '3' : None, '4' : None, '5' : None, '6' : None, '7' : None}
    
    def wl_from_wlmList(self, ch: int):
        current_wl = round(float(self.WL_list[str(ch)]), 6)
        return current_wl

    # get wavelength from server
    def WL_from_server(self):
        self.client_socket.sendall("{:d}".format(1).encode("utf-8"))
        WL = (self.client_socket.recv(1024)).decode("utf-8")
        self.WL_list = ast.literal_eval(WL)