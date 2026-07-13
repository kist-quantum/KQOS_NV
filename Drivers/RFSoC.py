from socket import *
import json

class RFSoC:
    def __init__(self, ip: str, port: int):
        self.client_socket = self.connect(ip, port)
        self.counts = {}
    
    def laser_on(self):
        self.send({
            'command': 'laser_on',
            'laser_ch': self.laser_ch,
            'laser_power': 35000,
            'reps': 1
            }
        )
                  
    def connect(self, ip: str, port: int) -> socket:
        try:
            _socket = socket(AF_INET, SOCK_STREAM)
            _socket.connect((ip, port))
            return _socket
        except:
            print('Connection failed')
            return None
        
    def recv(self):
        response = json.loads(self.client_socket.recv(1024))
        self.counts = response['results']
    
    def send(self, config: dict):
        self.client_socket.send(json.dumps(config).encode())
    
    def getCount0(self):
        return self.counts['0']
    def getCount1(self):
        return self.counts['1']
    def getCount2(self):
        return self.counts['2']
    def getCount3(self):
        return self.counts['3']
    def getCount4(self):
        return self.counts['4']
    def getCount5(self):
        return self.counts['5']
    def getCount6(self):
        return self.counts['6']
    def getCount7(self):
        return self.counts['7']
    def getCount8(self):
        return self.counts['8']
    def getCount9(self):
        return self.counts['9']
    def getCount10(self):
        return self.counts['10']
    def getCount11(self):
        return self.counts['11']
    def getCount12(self):
        return self.counts['12']