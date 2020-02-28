import sys
from os import system


def at(link):
	system("ping -w 1 -c 1 " + link)


liste = ["com", "info", "edu", "k12", "eu"]


try:
	url = sys.argv[1]
except:
	print "Hata..."
	exit()

for i in liste:
	bir = url.replace(".com", "")
	iki = bir + "." + i
	print "\n\n\t\t\t", i
	print "-" * 50
	at(iki)
