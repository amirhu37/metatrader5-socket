import socket
import numpy as np



class socketserver:
    def __init__(self, address='', port=9090):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = address
        self.port = port
        self.sock.bind((self.address, self.port))
        self.cummdata = ''
        self.conn = None  # Initialize the connection socket

    def recvmsg(self):
        self.sock.listen(1)
        self.conn, self.addr = self.sock.accept()
        print('Connected to', self.addr)
        self.cummdata = ''
        
        while True:
            data = self.conn.recv(10)

            self.cummdata += data.decode("utf-8")
            if not data:
                
                break

        needs = self.cummdata.split(',')
        data = [needs[i: i+4] for i in range(0,len(needs), 4)][:-1]
        data = [tuple(float(i) for i in j) for j in data]
        return np.array(data)

    def sendmsg(self, Data):
        self.sock.listen(1)
        self.conn, self.addr = self.sock.accept()
        
        out = self.conn.send(bytes(Data, "utf-8"))  # Use utf-8 encoding for sending data
        
        return out  # Return the number of bytes sent

    def __del__(self):
        self.sock.close()

def data_open():
    msg = serv.recvmsg()
    return msg[:,0]

def data_high():
    msg = serv.recvmsg()
    return msg[:,1]

def data_low():
    msg = serv.recvmsg()
    return msg[:,2]
def data_close():
    msg = serv.recvmsg()
    return msg[:,3]

serv = socketserver('localhost', 9090)

print(data_open())
