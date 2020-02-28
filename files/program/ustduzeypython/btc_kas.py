from selenium import webdriver
import time
import sys



try:
	if sys.argv[1] == "default":
		key = "133FzEzqX9BpAdtRASdsKyNJTGiwKx36ze"
	else:
		key = sys.argv[1]
except:
	key = "133FzEzqX9BpAdtRASdsKyNJTGiwKx36ze"




try:
	if sys.argv[2] == "default":
		sure = 1
	else:
		sure = int(sys.argv[2])
except:
	sure = 1

print "[*] KEY:", key
print "[*] Time:", sure


link = "https://bitminer.io/"
br = webdriver.Firefox()
br.get(link)
br.find_element_by_name("addr").send_keys(key)
br.find_element_by_class_name("btn-login").submit()

sasa = raw_input("Hazirsan bas entere...")

sa = 0

try:
	while True:
		br.refresh()
		sa += 1
		print "[+] Yenilendi:",sa
		time.sleep(sure)
except:
	try:
		br.close()
	except:
		pass
	print "[!] Kapatildi..."
