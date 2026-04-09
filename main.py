import sys
sys.path.append('/usr/local/share/pynq-venv/lib/python3.8/site-packages')
sys.path.append('/home/xilinx/jupyter_notebooks/qick_version_0.2/qick_lib')
from qick import *
# Load bitstream file, hwh file also needed#
soc = QickSoc(bitfile="./qick_111_241112_v6.bit")

from socket import *
import threading
import time
from pprint import pprint
import json
from proc import process

def create_socket():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind(('', 6030))
    server_socket.listen(1)
    return server_socket

server_socket = create_socket()
pprint(f'Now ready.')
while True:
    try:
        client_sock, ip = server_socket.accept()
        pprint(f'Client {ip} is connected')
        while True:
            recv_data = client_sock.recv(1024)
            if not recv_data:
                client_sock.close()
            else:
                response = process(json.loads(recv_data), soc)
                if response['results']:
                    client_sock.send(json.dumps(response).encode())
                
    except Exception:
        pprint('Disconnected from the client. Waiting for a new one.')
        server_socket.close()
        server_socket = create_socket()