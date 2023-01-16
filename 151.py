import socket
import time

#take the server name and port number
host='localhost'
port=5000

#create a socket at server side to use UDP_Protocol
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#let the server waits for 5 seconds
time.sleep(5)

#send a message to the client after encoding intp binary string
s.sendto(b"Hello client ! How are you?",(host,port))
msg="Bye!"
s.sendto(msg.encode(),(host,port))

#disconnect the server
s.close()