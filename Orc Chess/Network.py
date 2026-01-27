import socket
import time


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
        self.server = "192.168.4.47"
        self.port = 55555
        self.addr = (self.server, self.port)        
        self.player = self.connect()
        self.client.setblocking(False)

    def getPlayer(self):
        return self.player

    def connect(self):
        try:           
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass
        
    def isConnected(self):
        
        try: 
            self.client.send(str.encode('connected?'))
            if self.client.recv(2048).decode() == 'yes':           
                return True
            else:            
                return False
        except socket.error as e:
            return False
        
    def send(self, data):
        try: 
            self.client.send(str.encode(data))
        except socket.error as e:
            print(e)
    def getData(self):
        
        try: 
            return self.client.recv(2048).decode()
        except BlockingIOError as e:
            return None
