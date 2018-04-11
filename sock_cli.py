import socket
import sys
import thread


host="blr01end1.bec.broadcom.net"
port=12345
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
s.send("Hello world")
while True:
	try:
		a=raw_input("Myname $")
		s.send(str(a))
		while s.recv(1024) != "ack":
			print "waiting for ACK"
		print "ack recieved"
	except KeyboardInterrupt:
		print "recived keyboardInterrupt"
		break
data=s.recv(1024)
s.close()
s.close()
print "recieved", repr(data)

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




# client.py:

# import socket
# import time

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect(("localhost", 8220))

# for index in xrange(5):
#     data = "GET\nSONAR%d\n\n" % index
#     print 'send to server: ' + data
#     client_socket.send(data)
#     while client_socket.recv(2048) != "ack":
#         print "waiting for ack"
#     print "ack received!"

# #send disconnect message                                                                                                                           
# dmsg = "disconnect"
# print "Disconnecting"
# client_socket.send(dmsg)

# client_socket.close()
# server.py:

# import socket
# import sys

# host = 'localhost'
# port = 8220
# address = (host, port)

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind(address)
# server_socket.listen(5)

# print "Listening for client . . ."
# conn, address = server_socket.accept()
# print "Connected to client at ", address
# #pick a large output buffer size because i dont necessarily know how big the incoming packet is                                                    
# while True:
#     output = conn.recv(2048);
#     if output.strip() == "disconnect":
#         conn.close()
#         sys.exit("Received disconnect message.  Shutting down.")
#         conn.send("dack")
#     elif output:
#         print "Message received from client:"
#         print output
#         conn.send("ack")