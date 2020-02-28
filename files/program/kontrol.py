import os


def at(deger):
	os.system("ping -w 2 " + deger)

for a in range(255):
	at("192.168.0." + str(a))
