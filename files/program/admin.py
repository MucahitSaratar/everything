import requests
import sys



try:
	url = sys.argv[1]
	try:
		pat = sys.argv[2]
	except:
		pat = "dorks"
	ac = open(pat, "r")
	eklenti = ac.readlines()
	liste= []
	for ekle in eklenti:
		istek = url + "/" + ekle.replace("\n", "")
		yolla = requests.get(istek)
		kod = yolla.status_code
		if kod != 301 and kod != 404:
			if not "Page not found" in yolla.content:
				print "Var :                                                        " + istek
				liste.append(istek)
			else:
				print "Yok : " + istek
		else:
			print "Sayfa yok : " + istek


	if not liste:
		print "Yok..."
	else:
		print "-------------------bulundu---------------------------------"
	for i in liste:
		print i
except:
	print "Control-C yapildi..."
