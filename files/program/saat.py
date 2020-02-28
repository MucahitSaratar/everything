import time
import sys
import os

try:
	sat = sys.argv[1]
	dak = sys.argv[2]
	bir = int(sat)
	iki = int(dak)
	com = sys.argv[3]
except:
	print "Hata..!"
	exit()



while True:
	if bir == time.strftime("%H") and iki == time.strftime("%S"):
		break

print "sure doldu...."
os.system(com)
