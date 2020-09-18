import sys
sys.path.append(".")

import settings
import numpy as np

def randomUniform():

    size = settings.neural_network['size']

    weights = []
    for layer in range(0, len(size) - 1, 1):
        weights.append(np.random.uniform(-1, 1, (size[layer], size[layer+1])))

    biases = []
    for layer in range(1, len(size), 1):
        biases.append(np.random.uniform(-1, 1, (size[layer], 1)))

    return weights, biases

def randomStart(population):

    if settings.genetic_algorithm['random start'] == 'random uniform':
        for individual in population.individuals:
            individual.neural_network.weights, individual.neural_network.biases = randomUniform()

    else:
        raise Exception("Random start option not found!")

    return population