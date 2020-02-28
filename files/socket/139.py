import sys
import socket


try:
	host = sys.argv[1]
except:
	print "Lutfen 1. argumana host adresini giriniz...."
	exit()

ag = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

liste = ["139", "445", "443", "80", "25", "22"]

for port in liste:
	try:
		ag.connect((ip, port))
		print "[+] Baglandi. :", port
	except:
		print "[!] Baglanamadi.:", port
