import sys
SUBVERSION = 0
def usage():
	print "[+] KOD : %d" % (SUBVERSION)
	sys.exit(0)
def wps_pin_checksum(pin):
	accum = 0
	while(pin):
		accum += 3 * (pin % 10)
		pin /= 10
		accum += pin % 10
		pin /= 10
	return  (10 - accum % 10) % 10
try:
	if len(sys.argv[1]) == 6:
		p = int(sys.argv[1] , 16) % 10000000
		print "[+] KOD : %07%d%d" % (p, wps_pin_checksum(p))
	else:
        	usage()
except:
	usage()
