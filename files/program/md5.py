import hashlib
import sys
try:
	text = sys.argv[1]
	sifre = hashlib.md5(text).hexdigest()
	m = "Original :{}\nMd5      :{}".format(text, sifre)
	print m
except:
	print "usage : pytohn md5.py <text>"
