ob = raw_input("Aklina gelen ilk kelimeyi yaz : ")
mesaj = "\n{} deme {} olursun..!\n{} a\e kurban olursun"
soru = "{} kapina gelse ne verirsin.. ::>"
while True:
	try:
		print mesaj.format(ob, ob, ob)
		ob = raw_input(soru.format(ob))
		if ob == "q":
			break
	except:
		print "\n" + "-" * 20 + " AA yapma ama boyle .d xD" + "-" * 20 + "\n"
