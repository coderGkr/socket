# Import socket module
import socket
import time
import threading

flag = 1

def listen(conn):
	while flag:
		try:
			conn.setblocking(0)
			data = conn.recv(1024)
			print "\nserver :"+data
			time.sleep(0.1)
			if data == "":
				print "no more data"
				break

		except socket.error as err:
			#have to increase Err 10035
			if "10035" in err:
				pass

		except socket.timeout:
				print "Timeout"
				pass




def send(conn):
	try:
		while flag:
			conn.setblocking(0)
			message = raw_input("\nClient : ")
			conn.sendall(message)
			time.sleep(0.1)
	except EOFError as err:
		print "Encountered EOF Error %s" %(err)
		pass
	except socket.error as err:
		#have to increase Err 10035
		if "10035" in err:
			print "hit interrupt in send"
			pass



# Create a socket object
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Define the port on which you want to connect 
port = 12345

# connect to the server on local computer 
s.connect(('127.0.0.1', port))
s.setblocking(0)
s.settimeout(60)
a=raw_input("Connected...Press any Key to start")


tx = threading.Thread(target=send,args=(s,))
rx = threading.Thread(target=listen,args=(s,))
tx.start()
rx.start()

# while True:
# 	try:
# 		time.sleep(0.5)
# 	except KeyboardInterrupt:
# 		flag=1
# 		pass
# 		break

#wait for stop event
try:
	while True:
			time.sleep(0.5)
except KeyboardInterrupt:
	flag=0
	print "hit interrupt"
	pass

a=raw_input("Press any key to close")

rx.join()
tx.join()

# close the connection
s.close() 