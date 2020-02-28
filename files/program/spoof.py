from scapy.all import *


def packetsniff(packet):
	if packet.haslayer(DNS) and packet.getlayer(DNS).qr==0:
		print packet.summary()


while True :
	print 'Dns paket analiz edildi'
	sniff(iface="wlan0",count=1,filter="udp port 53",prn=packetsniff)
