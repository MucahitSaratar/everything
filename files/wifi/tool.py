import os
import jammer
import tara
os.system("sudo airmon-ng start wlan0")
print "\nTaraniyor..."
tara.Tara()

def shell():
	kod = "Tools>"
	com = raw_input(kod)
	if com == "cik":
		os.system("sudo airmon-ng stop wlan0mon")
		exit()
	elif com == "jammer":
		jammer.bilgi()
		jammer.Jammer()
		shell()
	else:
		print "command not found :", com
		shell()

shell()
