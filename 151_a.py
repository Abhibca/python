import socket

#take the server name and port number
host='localhost'
port=5000

#create a socket at server side to use UDP_Protocol
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#connect it to server with host name and port number
s.bind((host,port))

#recive message from server,at time 1024 bytes
msg,addr=s.recvfrom(1024)

try:
    #let the socket blocks after 5 second if the server disconnect
    s.settimeout(5)

    #repeat as longas message strings are not empty
    while msg:
        print('Recive : '+msg.decode())
        msg,addr=s.recvfrom(1024)

except socket.timeout:
    print('Time is over and hence termminating........')

#disconnect server
s.close()

#disconnect the server
s.close()