# import that sweet socket library
import socket 

# create a socket object bro
s = socket.socket()
print ("Socket was created. Good for you")

# reserve a port number because the lines are long
port = 1456

# bind to the port because life is scary alone
s.bind(('',port))
print ("Socket binded to %s" %(port))

#put the socket into listening mode
s.listen(5)
print ("I hear you bro. I'm listening")

# make a forever loop until we exit or bug out

while True:
	#Establish connection with client
	# test in terminal with telnet
	c, addr = s.accept()
	print ("got connection from", addr)