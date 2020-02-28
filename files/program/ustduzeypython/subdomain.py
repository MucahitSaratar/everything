import socket
import sys

try:
	def getsite():
		global site
		site = sys.argv[1] #raw_input("[!] Enter the URL: ")
		if site[:7] == "http://":
			site = site[7:]
		elif site[:8] == "https://":
			site=site[8:]
	getsite()
	print "Hedef :", site
	def getip():
		list = ["cpanel.","kpanel.","wordpress.","server.","ftp.","mail.","webmail.","direct.","direct-connect.", "record."]
		print("[!] Deniyorum....")
		ip = socket.gethostbyname(site)
		print "Ip address : " + ip
		for item in list:
			try:
				ip = socket.gethostbyname(item + site)
				print "[+] " + item + site +  " >>>>>> " + ip + " found."
			except:
				print("[-] " + item + site + " not found.")
	getip()
except:
	print "[-*SORRY*-] Birseyler ters gitti..!"
	exit()
