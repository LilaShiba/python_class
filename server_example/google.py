# let's connect to google
import socket
import sys

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print ("Socket created!")
except socket.error as err:
	print ("Socket failed dude %s"%(err))

#default port
port = 80

try:
	host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
	print("There was an error with host")
	sys.exit()

# connecting to server
s.connect((host_ip, port))

print ("Worked Yeah Ween \ on port == %s" %(host_ip))