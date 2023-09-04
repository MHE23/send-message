import socket
import os
os.system('cls')


server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.connect(('Enter your ip', 8080))

while True :
    data = server.recv(2048) 
    print(data.decode())
    i = input('in >>')
    server.send(i.encode())
            
