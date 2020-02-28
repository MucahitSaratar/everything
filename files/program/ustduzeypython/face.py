from selenium import webdriver
import time

e = ""
p = ""


mesaj = "Trre gen in kodlari sana sesleniyor...\n" * 5


print """[1] Resul
[2] izzet
[3] deniz p.
[4] ozan
[5] tipi
[7] yldzts
[8] erturul
[9] guzel
[10] manuel"""

sor = input("Secim yap ::>")

if sor == 1:
	link = "https://m.facebook.com/messages/read/?tid=cid.c.100006502941242%3A100009762252005&refid=11#fua"
elif sor == 2:
        link = "https://m.facebook.com/messages/read/?tid=cid.c.100006502941242%3A100013101395726&refid=11#fua"
elif sor == 3:
        link = "https://m.facebook.com/messages/read/?tid=cid.c.100006502941242%3A100011538078417&refid=11#fua"
elif sor == 4:
        link = "https://m.facebook.com/messages/read/?tid=cid.c.100006502941242%3A100011481184089&refid=11#fua"
elif sor == 5:
        link = "https://m.facebook.com/messages/read/?tid=cid.c.100006502941242%3A100007709264446&refid=11#fua"
elif sor == 7:
        link = "https://m.facebook.com/messages/read/?tid=cid.c.100006502941242%3A100010791342071&refid=11#fua"
elif sor == 8:
        link = "https://m.facebook.com/messages/read/?tid=cid.c.100006502941242%3A100007165158033&start=0&first_message_timestamp=1509298172891&pagination_direction=2&show_delete_message_button&refid=12"
elif sor == 9:
        link = "https://m.facebook.com/messages/read/?tid=cid.c.100006301650164%3A100006502941242&refid=11#fua"
elif sor == 10:
	link = raw_input("Link ::>")


print "[*] OK."






br = webdriver.Firefox(executable_path="/root/Belgeler/geckodriver")
br.get("https://www.facebook.com")
br.find_element_by_id("email").send_keys(e)
br.find_element_by_id("pass").send_keys(p)
br.find_element_by_id("loginbutton").submit()
br.get("https://m.facebook.com")
br.get(link)
print "-" * 20 + "Atack satarted" + "-" * 20 + "\n"

say = 0
dene = 0
while True:
	try:
		br.find_element_by_id("composerInput").send_keys(mesaj)
		br.find_element_by_name("send").submit()
		say += 1
		print "[+] message successful:", say
	except:
		print "[!] message unsuccessful:", dene
		time.sleep(5)
		dene += 1
		if dene == 5:
			break
