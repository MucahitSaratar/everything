import socket
import sys


try:
	ip = sys.argv[1]
	port = int(sys.argv[2])
except:
	print "usage : python sender.py <ip_adress> <port>"
	exit()


ag = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



try:
	ag.connect((ip, port))
	print "[+] Network is Done."
	hazir = True
except:
	print "[!] Server is down."
	hazir = False
	exit()




while hazir:
	cod = raw_input("Your Command : ")
	if cod == "QQQ":
		ag.close()
		hazir = False
	else:
		ag.send(cod)
		print "[+] Sended :", cod + "."


