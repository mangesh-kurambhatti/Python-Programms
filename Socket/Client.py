import socket
import sys
import string

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_address=('localhost',1004)
print("Connecting to %s port %s",%server_address)

sock.conect(server_address)

try:
	message="India is my country,all Indians are my brother and sister."
	print("Sending -:%s"%message)

	while 1:
		
		sock.sendall(message)

		amount_received=0
		amount_expected=len(message)

		while amount_received < amount_expected:
			data=sock.recv(10)
			amount_received+=len(data)

			print('Received "%s" '%data)

		message=input("Enter msg-:")

finally:
	print('closing socket')
	sock.close()
