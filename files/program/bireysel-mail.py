import smtplib
e = ""
p = ""

target = raw_input("Target.? :>:")

if "@gmail.com" in target:
	print "[+] Var..."
else:
	target += "@gmail.com"
	print "[+] Eklendi...."
message = ""

print "lufen mesajinizi yazin ve bittiginde yeni satira 'q' yazip enterleyin..."
while True:
        m = raw_input("| ")
        if m != "q":
                message += m + "\n"
        else:
                break


try:
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.ehlo()
	server.login(e, p)
	server.sendmail(e, target, message)
	server.logout()
        print "[+] Sended..!"
except:
        print "[-] Not sended..!"

print "[*] Done!"

