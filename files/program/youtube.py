from selenium import webdriver
from time import sleep
#Site :http://dtunnel.gen.tr/
linkim = "https://www.youtube.com/watch?v=6htYtL4jolQ"
oklink = "http://www.dtunnel.gen.tr/px/index.php?q=2dnr1cSxoJTq6Nyl3sDs5drV1pPa1L6m6Mbn1M22246t2dnM5bGrz8Djwg"
br = webdriver.Firefox()


say = 0


while True:
	try:
		br.get(oklink)
		say += 1
		print "[" + str(say) + "] OK."
		sleep(13)
		if say == 245:
			break
	except:
		print "[Exiting] Control-C"
		break
print "[+] Done..."
