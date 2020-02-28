import hashlib
import sys

def MD5(string):
	return hashlib.md5(string.encode("utf")).hexdigest()


def sezar(string, kac):
	alfabe = ["a","b" ,"c" , "d", "e", "f", "g" ,"h" ,"i" ,"j", "k", "l" ,"m" ,"n" ,"o" ,"p" ,"r" ,"s" ,"t" ,"u" ,"v", "y" ,"z", "1", "2", "3", "4", "5", "6" ,"7" , "8", "9", "0"]
	sifre = ""
	for i in string:
		sifre += alfabe[(alfabe.index(i) + int(kac)) % len(alfabe)]
	return sifre

def ters(string):
	return string[::-1]

try:
	metin = sys.argv[1]
except:
	metin = raw_input("Sifrelenecek Metin: ")


bir = ters(metin)
iki = MD5(bir)
kaynak = ters(iki)
uc = sezar(kaynak, 8)
dort = ters(uc)
bes = MD5(dort)
alti = sezar(bes, 4)
parola = ters(alti)



print "[*] Original: {}\n[*] Encrypt: {}".format(metin, parola)
