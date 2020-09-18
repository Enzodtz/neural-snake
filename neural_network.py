import numpy as np
import settings

class NeuralNetwork():
    
    def __init__(self):

        self.size = settings.neural_network['size']
        self.activation_function = settings.neural_network['activation function']

        self.weights  = []
        self.biases   = []

        if self.activation_function == 'relu':
            self.activation_function = self.relu

        elif self.activation_function == 'sigmoid':
            self.activation_function = self.sigmoid

        else:
            raise Exception("Activation function not found!")

    def feedFoward(self, actual_layer):

        for i in range(len(self.size)-1):

            actual_layer = np.array(actual_layer).repeat(self.size[i+1]).reshape(self.size[i], self.size[i+1])
            actual_layer = np.multiply(self.weights[i], actual_layer)
            actual_layer = actual_layer.sum(axis=0)
            actual_layer = actual_layer.reshape(actual_layer.shape[0], 1)
            actual_layer = actual_layer + self.biases[i]
            actual_layer = self.activation_function(actual_layer)

        return actual_layer

    def relu(self, layer):
        return np.maximum(0, layer)

    def sigmoid(self, layer):
        layer = np.clip(layer, -500, 500 )
        return 1.0 / (1.0 + np.exp(-layer))

def processOutput(snake_direction, neural_output):

    neural_output = list(neural_output)
    neural_output = neural_output.index(max(neural_output))

    if snake_direction == 'up':
        
        if neural_output == 0:
            neural_output = 'left'

        elif neural_output == 1: 
            neural_output = 'up'

        else:
            neural_output = 'right'

    elif snake_direction == 'right':
        
        if neural_output == 0:
            neural_output = 'up'

        elif neural_output == 1: 
            neural_output = 'right'

        else:
            neural_output = 'down'

    elif snake_direction == 'down':
        
        if neural_output == 0:
            neural_output = 'right'

        elif neural_output == 1: 
            neural_output = 'down'

        else:
            neural_output = 'left'

    elif snake_direction == 'left':
        
        if neural_output == 0:
            neural_output = 'down'

        elif neural_output == 1: 
            neural_output = 'left'

        else:
            neural_output = 'up'

    return neural_output