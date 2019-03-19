# Import socket module
import socket
import time
import threading

def listen(conn):
	while True:
		try:
			data = conn.recv(1024)
			print "\nserver :"+data
			time.sleep(0.1)
			print "Client :",
			if data == "":
				print "no more data"
				break
		except socket.timeout:
			print "Timeout"
			break


def send(conn):
	while True:
		message = raw_input("\nClient : ")
		conn.sendall(message)
		time.sleep(0.1)


# Create a socket object
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Define the port on which you want to connect 
port = 12345

# connect to the server on local computer 
s.connect(('127.0.0.1', port))
s.setblocking(0)
s.settimeout(60)
a=raw_input("enter here")
print a

tx = threading.Thread(target=send,args=(s,))
rx = threading.Thread(target=listen,args=(s,))
tx.start()
rx.start()



a=raw_input("hre")

rx.join()
tx.join()

# close the connection
s.close() 