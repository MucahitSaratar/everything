import socket
from sys import argv
host = argv[1]

def Tara(bir, iki):
	try:
		ag = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		kod = ag.connect_ex((host, port))
	except:
		pass
	return kod

print "Scanning..."
for port in xrange(60000):
	try:
		don = Tara(host, port)
		if don == 0:
			print "Open :", port
	except:
		pass
