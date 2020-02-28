import sys

try:
	try:
		file = open(sys.argv[1], "r")
		print "okunuyor..."
		acmak = file.read()
	except:
		print "Boyle bir dosya yok..!"
		exit()
except:
	print "usage: <file>"
	exit()



say = 0
for i in acmak:
	say += 1

print "-" * 50
print str(say) + " kadar satit var..!"
