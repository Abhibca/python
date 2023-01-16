#a tcp/ip server  that sends message to client
import socket

#take the server name and port number
host='localhost'
port=5000

#create a socket at server side using Tcp/Ip protocol
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#bind the socket with server and port number
s.bind((host,port))

#allor maximum 1 Connection to the socket
s.listen(1)

#wait rill a client accepts coonection
c,addr=s.accept()

#display client address
print("Connection from : ",str(addr))

#send message to the client after encoding into binary string
c.send(b"Hello client , how are you")
msg="Bye!"
c.send(msg.encode())

#disconnect the server
c.close()