import sys
import ftplib

try:
	host = sys.argv[1]
	useranme = sys.argv[2]
	password = sys.argv[3]
	print "[*] Ok."
except:
	print "Yanlis Arguman..."
	exit()

try:
	baglan = ftplib.FTP(host)
except:
	print "[-] Server is down"
	exit()


try:
	baglan.login(username, password)
except:
	print "[-] Hatali kullanici adi yada sifre"
	exit()

