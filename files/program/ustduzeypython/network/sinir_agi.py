from numpy import exp, array, random, dot


class Siniragi():
	def __init__(self):
		random.seed(1)
		self.agirlik = 2 * random.random((3, 1)) - 1

	def sigmoid(self, x):
#		print 1 / (1 + exp(-x))
#		print "-" * 20
		return 1 / (1 + exp(-x))

	def ters_sigmoid(self, x):
#		print x * (1 - x)
#		print "-" * 20
		return x * (1 - x)

	def dusun(self, girisler, cikislar, sayi):
		for items in xrange(sayi):
			cikis = self.tahmin(girisler)
			hata = girisler - cikis
			ek = dot(girisler.T, hata * self.ters_sigmoid(cikis))
#			print "Agirlik :\n", self.agirlik, "Ek:\n", ek
			self.agirlik += ek

	def tahmin(self, giris):
#		print self.sigmoid(dot(giris, self.agirlik))
#		print "-" * 20
		return self.sigmoid(dot(giris, self.agirlik))
