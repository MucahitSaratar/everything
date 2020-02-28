from numpy import exp, array, dot
import random


x1 = 0.5
x2 = 0.6
x3 = 0.2
x4 = 0.7
w1 = random.uniform(1.0, -1.0)
w2 = random.uniform(1.0, -1.0)
w3 = random.uniform(1.0, -1.0)
w4 = random.uniform(1.0, -1.0)



def sigmod(deger):
	print 1 / (1 + exp(-deger))

for i in range(4):
	net = x1 * w1 + x2 * w2 + x3 * w3 + x4 * w4


sigmod(net)
