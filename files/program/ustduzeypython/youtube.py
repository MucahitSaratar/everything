import time
from selenium import webdriver
import sys
vi = sys.argv[1]
print "[*] Link :", vi
br = webdriver.Firefox(executable_path="/root/Belgeler/geckodriver")
indir = "https://www.onlinevideoconverter.com/tr/mp3-converter"
br.get(indir)
br.find_element_by_id("texturl").send_keys(vi)
br.find_element_by_id("convert1").click()


while True:
	if "tamamland" in br.title:
		break


br.find_element_by_id("downloadq").click()
#br.find_element_by_id("downloadq").click()
print "[+] Indirme Basarili..!"
sor = raw_input("Indirme bittiyse enter e basin....")
try:
	br.close()
except:
	pass
