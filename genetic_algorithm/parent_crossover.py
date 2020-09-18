import sys
sys.path.append(".")

import numpy as np
import random
import settings

def simulatedBinaryCrossover(parent1, parent2, eta):

    rand = np.random.random(parent1.shape)
    beta = np.empty(parent1.shape)

    beta[rand <= 0.5] = (2 * rand[rand <= 0.5]) ** (1.0 / (eta + 1))
    beta[rand > 0.5] = (1.0 / (2.0 * (1.0 - rand[rand > 0.5])))

    child1 = 0.5 * ((1 + beta) * parent1 + (1 - beta) * parent2)
    child2 = 0.5 * ((1 - beta) * parent1 + (1 + beta) * parent2)

    return child1, child2

def uniformBinaryCrossover(parent1, parent2):

    child1 = parent1.copy()
    child2 = parent2.copy()
    
    rand = np.random.uniform(0, 1, size=child1.shape)

    child1[rand > 0.5] = parent2[rand > 0.5]
    child2[rand > 0.5] = parent1[rand > 0.5]

    return child1, child2

def singlePointCrossover(parent1, parent2, orientation):
    
    child1 = parent1.copy()
    child2 = parent2.copy()

    rows, cols = parent2.shape

    row = np.random.randint(0, rows)
    col = np.random.randint(0, cols)

    if orientation == 'rows':

        child1[:row, :] = parent2[:row, :]
        child2[:row, :] = parent1[:row, :]

        child1[row, :col+1] = parent2[row, :col+1]
        child2[row, :col+1] = parent1[row, :col+1]

    elif orientation == 'cols':

        child1[:, :col] = parent2[:, :col]
        child2[:, :col] = parent1[:, :col]

        child1[:row+1, col] = parent2[:row+1, col]
        child2[:row+1, col] = parent1[:row+1, col]

    else:
        raise Exception("Single point crossover option not found!")

    return child1, child2

def parentCrossover(population, parents):
    
    prob_simulated_binary_crossover = settings.genetic_algorithm['simulated binary crossover probability']
    prob_uniform_binary_crossover   = settings.genetic_algorithm['uniform binary crossover probability']
    prob_single_point_crossover     = settings.genetic_algorithm['single point crossover probability']

    eta = settings.genetic_algorithm['simulated binary crossover eta']
    orientation = settings.genetic_algorithm['single point crossover orientation']

    if prob_simulated_binary_crossover + prob_uniform_binary_crossover + prob_single_point_crossover != 1:
        raise Exception("Please use decimal notation for crossover probability, sum must be equal to 1.")

    num_parents = len(parents)

    for i in range(int(int(population.size/2))):

        parent1 = random.randint(0,len(parents)-1)
        parent2 = random.randint(0,len(parents)-1)
        while parent2 == parent1:
            parent2 = random.randint(0,len(parents)-1)

        parent1 = parents[parent1]
        parent2 = parents[parent2]

        selection_type = random.uniform(0, 1)

        if selection_type < prob_simulated_binary_crossover:

            for layer in range(len(parent1.neural_network.weights)):

                parent1_layer = parent1.neural_network.weights[layer]
                parent2_layer = parent2.neural_network.weights[layer]

                child1_layer, child2_layer = simulatedBinaryCrossover(parent1_layer, parent2_layer, eta)

                population.individuals[i].neural_network.weights.append(child1_layer)
                population.individuals[i + int(population.size/2)].neural_network.weights.append(child2_layer)

            for layer in range(len(parent1.neural_network.biases)):
    
                parent1_layer = parent1.neural_network.biases[layer]
                parent2_layer = parent2.neural_network.biases[layer]

                child1_layer, child2_layer = simulatedBinaryCrossover(parent1_layer, parent2_layer, eta)

                population.individuals[i].neural_network.biases.append(child1_layer)
                population.individuals[i + int(population.size/2)].neural_network.biases.append(child2_layer)

        elif selection_type < prob_uniform_binary_crossover + prob_simulated_binary_crossover:

            for layer in range(len(parent1.neural_network.weights)):
    
                parent1_layer = parent1.neural_network.weights[layer]
                parent2_layer = parent2.neural_network.weights[layer]

                child1_layer, child2_layer = uniformBinaryCrossover(parent1_layer, parent2_layer)

                population.individuals[i].neural_network.weights.append(child1_layer)
                population.individuals[i + int(population.size/2)].neural_network.weights.append(child2_layer)

            for layer in range(len(parent1.neural_network.biases)):
    
                parent1_layer = parent1.neural_network.biases[layer]
                parent2_layer = parent2.neural_network.biases[layer]

                child1_layer, child2_layer = uniformBinaryCrossover(parent1_layer, parent2_layer)

                population.individuals[i].neural_network.biases.append(child1_layer)
                population.individuals[i + int(population.size/2)].neural_network.biases.append(child2_layer)

        else:

            for layer in range(len(parent1.neural_network.weights)):
        
                parent1_layer = parent1.neural_network.weights[layer]
                parent2_layer = parent2.neural_network.weights[layer]

                child1_layer, child2_layer = singlePointCrossover(parent1_layer, parent2_layer, orientation)

                population.individuals[i].neural_network.weights.append(child1_layer)
                population.individuals[i + int(population.size/2)].neural_network.weights.append(child2_layer)

            for layer in range(len(parent1.neural_network.biases)):
    
                parent1_layer = parent1.neural_network.biases[layer]
                parent2_layer = parent2.neural_network.biases[layer]

                child1_layer, child2_layer = singlePointCrossover(parent1_layer, parent2_layer, orientation)

                population.individuals[i].neural_network.biases.append(child1_layer)
                population.individuals[i + int(population.size/2)].neural_network.biases.append(child2_layer)

    return population