import random as R
import sys

try:
	n = int(sys.argv[1])
	ks = int(sys.argv[2])
	bs = int(sys.argv[3])
	cs = int(sys.argv[4])
	js = int(sys.argv[5])
	debug = sys.argv[6]
	sifirlar = []
except:
	print "./"+sys.argv[0]+"<NxN icin N?> <kromozom sayisi> <baslaingic birey sayisi> <cocuk sayisi> <nesil-jenerasyon- sayisi> <Debug:False or True>"
	exit()

#n = 100 # int(raw_input("NXN matris icin N? :>"))
#ks = 30 #int(raw_input("Kronozom Sayisi :>"))
#bs = 5 # int(raw_input("Birey Sayisi :>"))
#cs = 5 #int(raw_input("Cocuk Sayisi :>"))
#js = 7 # nesil, jenerasyon sayisi

def rns(): # rastgele nokta sec
	x = R.randint(0, n-1)
	y = R.randint(0, n-1)
	return x, y



def inau(hx0, hy0, hx1, hy1): #iki nokta arasindaki uzaklik
	 return ((hx0-hx1)**2+(hy0-hy1)**2)**0.5




def bas(llll):
	for lalala in llll:
		print lalala + "\n"*5

def islem(bx, by, kron): ## kronuzoma gore yeni konumu belirler
	ix = bx
	iy = by
	for harf in kron:
		if harf == "W":
			if iy != 0:
				iy -= 1
			else:
				pass
		elif harf == "S":
			if iy != 99:
				iy += 1
			else:
				pass
		elif harf == "D":
			if ix != 99:
				ix += 1
			else:
				pass
		elif harf == "A":
			if ix != 0:
				ix -= 1
			else:
				pass
	if debug == "True":
		print "Sisteme Tam Adapte oldu:"
		print kron
		exit()
	if ix == bx and iy == by:
		sifirlar.append(kron)
	return ix, iy





def kc(L): # kronozom creator
	kkk = ""
	for i in xrange(L):
		ek = ""
		kkkno = R.randint(0, 3)
		if kkkno == 0:
			ek = "S"
		elif kkkno == 1:
			ek = "W"
		elif kkkno == 2:
			ek = "A"
		elif kkkno == 3:
			ek = "D"
		kkk += ek
	return kkk




def tb(bisa, khzm, krzmll): # tart bic en uygunu dondur (birey sayisi, "al" or "hazir", liste=> eger yeni olsutrulacaksa bos liste olmali)
	tblik = []
	tbliu = []
	ab = []
	xb, yb = rns()
	for birey in xrange(bisa):
		if khzm == "al":
			kro = kc(ks)
		if khzm == "hazir":
			kro = krzmll[birey]
		tblik.append(kro)
		sx, sy = islem(xb, yb, kro)
		uzaklik = inau(xb, yb, sx, sy)
		tbliu.append(uzaklik)
	m1 = tbliu.index(min(tbliu))
	tbliu.remove(tbliu[m1])
	m2 = tbliu.index(min(tbliu))
	tbliu.remove(tbliu[m2])
	ab.append(tblik[m1])
	ab.append(tblik[m2])
	return ab


avb = tb(bs, "al", [])

def mutasyon(kr): # mutasyon return eder
	mnok = R.randint(0, len(kr))
	kr = kr[:mnok] + kc(1) + kr[mnok+1:]
	return kr

def cocuk_yap(ielm): # aciklamama gerek yok diye dusunuyorum (iki elemanli liste alicak, biri disi bir erkek)
	cocuklistesi = []
	for cocuklar in xrange(cs):
		kesnok = R.randint(0, len(ielm[0]))
		ilk = ielm[0][:kesnok]
		iki = ielm[1][kesnok:]
		cocuklistesi.append(mutasyon(ilk+iki))
	return cocuklistesi




x0, y0 = rns()

def gosteri(cll): # cocuklarin listesini alip degerini hesaplar
	print "toplam eleman sayisi: ", len(cll)
	for aha in xrange(len(cll)):
		nxx, nyy = islem(x0, y0, cll[aha])
		uzak = inau(nxx, nyy, x0, y0)
		print "kromozom =>", cll[aha], "\n"  ,"Uzaklik degeri =>", uzak




avb = tb(bs, "al", [])
for saybakim in xrange(js):
	cocuklarim = cocuk_yap(avb)
	bs = len(cocuklarim)
	avb = tb(bs, "hazir", cocuklarim)

#gosteri(cocuklarim)
gosteri(sifirlar)
