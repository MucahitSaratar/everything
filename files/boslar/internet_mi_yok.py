from os import system
from time import sleep
kod_1 = "sudo clear"
kod_2 = "sudo airmon-ng start wlan0"
kod_3 = "sudo airmon-ng stop wlan0mon"
kod_4 = "sudo ifconfig wlan0 down"
kod_5 = "sudo ifconfig wlan0 up"

liste = [kod_2, kod_3, kod_4, kod_5]

"""Bombaaaa"""

print ("Lutfen Sifrenizi giriniz...")
system(kod_1)


for i in liste:
	system(i + " > /dev/null")
	print "[*] Command Sucsessfull :", i
	sleep(7)
