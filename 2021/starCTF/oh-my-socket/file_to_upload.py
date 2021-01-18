from socket import *

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(('172.24.0.2',21587))
tcpCliSock.send(b'*ctf')
data = b''
c = b''
while c != b'}':
	c = tcpCliSock.recv(1)
	data += c
print(data)
