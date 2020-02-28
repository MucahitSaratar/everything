import os
giris = """1-) Tema tara
2-) Eklenti tara
3-) Kullanici isimlerini tara
4-) kullaniciya brute force yap"""

site = raw_input("Site ex.google.com : ")

def run(komut):
	os.system("sudo wpscan --url " + site + " " + komut)


while True:
	print giris
	quest = raw_input("Choose a number : ")
	if quest == "1":
		ekle = "--enumerate -t"
		run(ekle)
	sor = raw_input("y-) Devam, n-) bitir : ")
	if sor == "y" or sor == "Y":
		pass
	else:
		break

print "\n\n\n[*] Done."
