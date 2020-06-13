

import socket#imports socket library so python can understand terms

HOST = '127.0.0.1'#sets the host, current ip is local
PORT = 2048#sets port to plug into, hopefully unused

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:#creates a socket that follows ipv4 and tcp
    s.connect((HOST, PORT))#connects the client to the socket
    s.sendall(b'Hello, world')#once connected sends the text hello, world
    data = s.recv(1024)#data recieved is of that many bytes

print('Received', repr(data))#print recieved when function is completed^^^