import random

def networkRandomStart(size):
    weights = []
    for layer in size[:-1]:
        weights.append([])
        for neuron in range(layer): 
            weights[-1].append([])
            for connection in range(size[size.index(layer)+1]):
                weights[-1][-1].append(random.random())

    biases = []
    for layer in size[1:]:
        biases.append([])
        for neuron in range(layer):
            biases[-1].append(random.random())

    return weights, biases

def processOutput(snake_direction, neural_output):

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

class NeuralNetwork():
    def __init__(self, size): 
        self.size = size

    def cicle(self, next_data):

        if len(next_data) != self.size[0]:
            raise Exception("Input data must have the same size as the input layer")

        for layer in self.size[:-1]:
            data = next_data
            next_data = []

            for neuron in range(layer):

                for connection in range(self.size[self.size.index(layer)+1]):
                    if neuron == 0:
                        next_data.append([])

                    next_data[connection].append(self.weights[self.size.index(layer)][neuron][connection] * data[neuron])

            for neuron in next_data:
                next_data[next_data.index(neuron)] = max(0, sum(neuron) + self.biases[self.size.index(layer)][next_data.index(neuron)])

        return next_data