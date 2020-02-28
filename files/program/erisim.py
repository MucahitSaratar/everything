import smtplib
import time


simdi = time.strftime("%S")

try:
	bir = time.strftime("%S")
	print "Kontrol ediliyor...."
	print "-" * 50
	server = smtplib.SMTP("smtp.gmail.com", 587)
	sonra = time.strftime("%S")
	vakit = int(sonra) - int(simdi)
	print "acik"
	print "\n" + str(vakit) + " Saniyede Kesfedildi..."
except:
	print "Kapali..."
	sonra = time.strftime("%S")
	vakit = int(sonra) - int(simdi)
	print "\n" + str(vakit) + " Saniyede Kesfedildi..."

