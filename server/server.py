import socket
import os 
os.system('cls') 


server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(('192.168.1.7', 8080))
server.listen(5)
con , addr = server.accept()

print(addr)

while True :
    
    inp = input('in >>')
    con.send(inp.encode())     
    data = con.recv(8192)
    print('\nout >>',data.decode())

