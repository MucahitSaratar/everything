from numpy import exp, array, random, dot
import sinir_agi


# uyku gelmesi # dikkatsizlik # asiri hiz # kaza ihtimali
#     1        #       0      #    0      #      1
#     0        #       1      #    0      #      1
#     1        #       1      #    1      #      1
#     0        #       0      #    1      #      0




###########################################################################
#                                 Tahmin  			          #
# 				  0, 1, 1 				  #
###########################################################################




try:
	ag = sinir_agi.Siniragi()
	b = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
	i = array([[0, 1, 1, 0]]).T
#	g = array([[1, 0, 0], [0, 1, 0], [1, 1, 1], [0, 0, 1]])
#	c = array([[1, 1, 1, 0]]).T
	print "Random agirlik:\n", ag.agirlik
	print "\n\nDusunuyorum...\n"
	ag.dusun(b, i, 1000)
	print "0, 1, 0 icin tahminim:\n", ag.tahmin(array([[0, 1, 0]]))
except:
	print "Ters Giden Bir seyler var..." 
