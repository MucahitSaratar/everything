import smtplib
import random
myadres = ""
mypass = ""
confrim = random.randint(100000, 999999)
st = str(confrim)
k_mail = raw_input("Mail adresinizi giriniz : ")


#message = "Your Confrim code: %s" % confrim

try:
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	server.login(myadres,mypass)
	server.sendmail(myadres,k_mail,str(confrim))
	karsi = int(raw_input("Your confrim code: "))
except:
	print "Error Code: 500"
	exit()

if karsi == confrim:
	print "[+] Email confrim Successfull..!"
else:
	print "[!] Email confrim Unsuccesfull.!"

print "[*] Done."
