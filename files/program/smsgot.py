from selenium import webdriver



while True:
	n = raw_input("Numara -10 haneli- :>:")
	if len(n) != 10:
		print "hatali numara"
	else:
		no = "0090" + n
		print "numara okundu"
		break

sms = raw_input(">")
print str(no) + " numarasina " + sms + " mesaji gidecektir"

br = webdriver.Firefox(executable_path="/root/Belgeler/geckodriver")

br.get("https://www.uzbekweb.net")
br.find_element_by_name("terms").submit()
br.get("https://www.uzbekweb.net/b/https://www.smsgott.de/free-sms.html")
br.find_element_by_id("sms_recipient").send_keys(no)
br.find_element_by_id("sms_text").send_keys(sms)
##########adim bir################
br.find_element_by_id("weiter_btn").submit()
g = raw_input("Guvenlik kodu :>:")
br.find_element_by_id("captchatext").send_keys(g)
br.find_element_by_id("lm_banner").submit()
