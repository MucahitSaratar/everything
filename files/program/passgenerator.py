import wordlist
import sys
import subprocess
#import os


try:
	b = int(sys.argv[1])
	s = int(sys.argv[2])
	k = sys.argv[3]
	i = sys.argv[4]
	print "[+] OK."
except:
	print "python passgenerator.py <baslanic_karakter> <bitis_karakter> <nelerden_olussun> <file_name>"
	exit()


generator = wordlist.Generator(k)
for word in generator.generate(b, s):
	subprocess.Popen("echo " + word + " >> " + i, shell=True)
print "[+] Done."
