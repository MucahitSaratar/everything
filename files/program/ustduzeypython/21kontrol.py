import sys
import ftplib

#robotistan = 37.58.83.77

try:
	host = sys.argv[1]
	print "[*] Ok."
except:
	print "[-] Arguman is not fount"
	exit()

try:
	baglan = ftplib.FTP(host)
	print "[+] Server is up"
except:
	print "\n[-] Server is down"
	exit()
