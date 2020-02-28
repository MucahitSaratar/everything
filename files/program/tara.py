from scapy.all import *
import sys
import netifaces

Gw = netifaces.gateways()["default"][2]
print Gw

print "-" * 50
print " Arp Scanner Uygulamasi "
print "-" * 50

conf.verb = 0


ipadd = "192.168.0."

for i in range (1,254):
	try:
		ip = ipadd + str(i)
		deger = i * 0
		ans=srp1(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip),timeout=1,retry=1)
		if ans:
			print "IP: " + ans.psrc + " MAC : " + ans.hwsrc
	except:
		print "durduruldu..."
