import sys


text = sys.argv[1]



def sifrele(q):
	alfabe = ["a","b" ,"c" , "d", "e", "f", "g" ,"h" ,"i" ,"j", "k", "l" ,"m" ,"n" ,"o" ,"p" ,"r" ,"s" ,"t" ,"u" ,"v", "y" ,"z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
	sifre = ""
	for i in q:
		sifre += alfabe[(alfabe.index(i) + 13) % len(alfabe)]

	return sifre[::-1]

print "Sifre :", sifrele(text)
