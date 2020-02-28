from selenium import webdriver
import os
import sys
import time


try:
	link = sys.argv[1]
	print "[+] link alindi"
except:
	print "[*] usage : python garanti.py <youtube_link>"
	exit()


def olay():
	br = webdriver.Firefox()
	br.get("https://uzbekweb.net")
	br.find_element_by_name("terms").submit()
	br.get("https://uzbekweb.net/b/" + link)
	time.sleep(100)
	br.close()

say = 0
dene = 0
while True:
	try:
		olay()
		say += 1
		print "olumlu :", say
	except:
		br.close()
		break
print say, " kere acildi...."

exit()
