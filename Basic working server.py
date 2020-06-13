

import socket #imports socket library for understanding socket terms

HOST = '127.0.0.1'#defines local host
PORT = 2048 #defines port hopefully unused

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #creates a socket throught ipv4 that follows tcp
    s.bind((HOST, PORT)) #binds the socket to the local network
    s.listen() #allows the socket to listen in for connections from clients
    conn, addr = s.accept()#connects the client to the socket
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)#with the connection active print etc.. while recieving data infinitely
            if not data:
                break#if the data ends break the connection to the client
            conn.sendall(data)#send all the data 