import socket
import os
os.system('cls')


server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.connect(('192.168.1.102', 8080))

while True :
    data = server.recv(2048) 
    print(data.decode())
    i = input('in >>')
    server.send(i.encode())
            
