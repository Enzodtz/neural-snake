import numpy as np

class NeuralNetwork():
    def __init__(self, size):
        self.size = size

    def generateRandom(self):
        self.biases = [np.random.randn(layer, 1) for layer in self.size[1:]]
        self.weights = [np.random.randn(layer, next_layer) for layer, next_layer in zip(self.size[:-1], self.size[1:])]

    def cicle(self, data):

        data = np.array(data)
        data = data.reshape(1,2)

        for bias, weight in zip(self.biases, self.weights):
            
            data = np.maximum(0, np.dot(weight, data)+bias)

        return data

#example of runing

# nn = NeuralNetwork([2,1,2])
# nn.generateRandom()
# data = [1,1]
# print(nn.cicle(data))