from gtts import gTTS
import sys
import os
language = 'tr'
m = raw_input("Text : ")
s = sys.argv[1]
myobj = gTTS(text=m, lang=language, slow=False)
name = s + ".mp3"
while True:
	try:
		print "Kaydoluyor..."
		myobj.save(name)
		break
	except:
		print "\n\n\nNo Kayit....\n\n\n"
		exit()
os.system("mpg321 " + name)
print "\n\n\n[+] Done"
