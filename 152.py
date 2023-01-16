import socket

host='localhost'
port=6767

s=socket.socket()

s.bind((host,port))

s.listen(1)

c,addr=s.accept()
print('A Client accepted connection')

fname=c.recv(1024)

fname=str(fname.decode())
print("file name recived from client : "+fname)

try:
    f=open(fname,'rb')
    content=f.read()
    c.send(content)
    print('file content sent')
    f.close()

except FileNotFoundError:
    c.send()

c.close()