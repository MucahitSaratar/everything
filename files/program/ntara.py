import os
import sys



command = "sudo nmap -sS -sV"

try:
	ip = sys.argv[1]
except:
	ip = raw_input("Enter the Ip Adress :")

print "[*] ip :", ip

kod = command + " " + ip
print "Lutfen Bekleyiniz...."
print "-" * 50
os.system(kod)
