import socket
import sys
import threading

def SendRecv(connection,clien_address):

	try:
		print('Connection from,connection is',client_address,connection)

		while True:
			data=connection.recv(10)

			print('Received "%s"'%data)
			
			if data:
				print('Sending data back to the client')
				connection.sendall(data)

			else:
				print("No more data from",client_address)
				break;	
	
	finally:
		connection.close()


sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_address=('localhost',1004)

print('starting up on %s port %s'%server_address)

sock.bind(server_address)

sock.listen(5)

while True:
	print('waiting for a connection')

	connection,client_address=sock.accept()

	t1=threading.Thread(target=SendRecv,args=(connection,client_address))

	t1.start()

