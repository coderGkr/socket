import socket
import sys
import thread

trds={}

def broad(data):
	for cli in trds.keys():
		trds[cli][1].send(data)

def cback(cli,addr):
	bfr=""
	while True:
		data=cli.recv(2048)
		if data.strip() == "disconnect":
			cli.send("dack")
			cli.close()
		elif data:
			print "message recieved from client"
			print data
			broad(data)
			cli.send("ack")

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	print "socket successfully created"
except socket.error as err:
	print "connection failed with error %s" %(err)

port=12345

s.bind(('',port))
#for the server to listen to other computers in the networks we give empty string

print "socket binded to %s" %(port)

s.listen(5)
print "socket is listening"

while True:
		try:
			c,addr=s.accept()
			if addr not in trds.keys():
				trds[addr]=(thread.start_new_thread(cback,(c,addr)),c)
			print "Got connection From", addr
			c.send("Thank you for connecting")
		except KeyboardInterrupt:
			print "closing connection"
			c.close()
			exit(0)


# while True:
# 		c,addr=s.accept()
# 		if addr not in trds.keys():
# 			trds['addr']=thread.start_new_thread(cback,(c,addr))
# 		print "Got connection From", addr
# 		c.send("Thank you for connecting")
# 		c.close()

# First of all we import socket which is necessary.
# Then we made a socket object and reserved a port on our pc.
# After that we binded our server to the specified port. Passing an empty string means that the server can listen to incoming connections from other computers as well. If we would have passed 127.0.0.1 then it would have listened to only those calls made within the local computer.
# After that we put the server into listen mode.5 here means that 5 connections are kept waiting if the server is busy and if a 6th socket trys to connect then the connection is refused.
# At last we make a while loop and start to accept all incoming connections and close those connections after a thank you message to all connected sockets.