#a tcp/ip server  that sends message to client
import socket

#take the server name and port number
host='localhost'
port=5000

#create a socket at server side using Tcp/Ip protocol
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#bind the socket with server and port number
s.connect((host,port))

#receive message string from server  at a time 1024 buffer size
msg=s.recv(1024)

#here,1024 indicates the buffer size,this is the memory used
#while receiving the data that is at a time
#data can be received from the server
#repeat as long as message strings are not empty 
while msg:
    print('Received : '+msg.decode())
    msg=s.recv(1024)

#disconnect the client
s.close()