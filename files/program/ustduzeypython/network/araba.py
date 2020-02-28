from numpy import exp, array, random, dot


class Sinir():
    def ayar(self, bir, iki):
        random.seed(1)
        self.synaptic_weights = 2 * random.random((bir, iki)) - 1

    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))


    def __sigmoid_derivative(self, x):
        return x * (1 - x)



    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in xrange(number_of_training_iterations):
            output = self.think(training_set_inputs)
            error = training_set_outputs - output
            adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))
            self.synaptic_weights += adjustment


    def think(self, inputs):
        return self.__sigmoid(dot(inputs, self.synaptic_weights))







#motor aktif # onde engel # benzin # return
# 0               1           1       0
# 0               0           1       0
# 1               0           1       1
# 1               1           0       0
#####
# 1               1           1       ?



ag = Sinir()
ag.ayar(3, 1)
print "rastgele agirliklar:\n", ag.synaptic_weights
print "Baglanti Cozumleniyor....Lufen bekleyin...."


training_set_inputs = array([[0, 1, 1], [0, 0, 1], [1, 0, 1], [1, 1, 0]])
training_set_outputs = array([[0, 0, 1, 0]]).T
ag.train(training_set_inputs, training_set_outputs, 3000)
print "egitim sonrasi yeni agirliklar:\n", ag.synaptic_weights
mytahmin = ag.think(array([1, 0, 0]))
print "1, 0, 0 icin tahminim:\n", mytahmin # neural_network.think(array([1, 0, 1, 1]))
ileri = int(round(mytahmin))
print "Kisaca ileri %s olur" % ileri
