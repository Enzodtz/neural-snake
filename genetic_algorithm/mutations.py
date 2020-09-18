import sys
sys.path.append(".")

import numpy as np
import random
import settings

def gaussianMutation(chromosome, prob_mutation, scale):

    rand_array = np.random.random(chromosome.shape) < prob_mutation

    gaussian_mutation = np.random.normal(size=chromosome.shape)
    
    gaussian_mutation[rand_array] *= scale

    chromosome[rand_array] += gaussian_mutation[rand_array]

    return chromosome

def randomUniformMutation(chromosome, prob_mutation):

    mutation_array = np.random.random(chromosome.shape) < prob_mutation

    uniform_mutation = np.random.uniform(-1, 1, size=chromosome.shape)

    chromosome[mutation_array] = uniform_mutation[mutation_array]

    return chromosome

def mutate(population):
    
    prob_random_uniform_mutation = settings.genetic_algorithm['random uniform mutation probability']
    prob_gaussian_mutation = settings.genetic_algorithm['gaussian mutation probability']
    prob_mutation = settings.genetic_algorithm['mutation probability']

    gaussian_mutation_scale = settings.genetic_algorithm['gaussian mutation scale']

    if prob_gaussian_mutation + prob_random_uniform_mutation != 1:
        raise Exception("The sum of the gaussian and random uniform mutation must be equal to 1.")

    for individual in population.individuals:

        for layer in range(len(individual.neural_network.weights)):

            chromosome = individual.neural_network.weights[layer]

            mutation_type = random.random()

            if mutation_type < prob_gaussian_mutation:
                
                chromosome = gaussianMutation(chromosome, prob_mutation, gaussian_mutation_scale)

            else: 

                chromosome = randomUniformMutation(chromosome, prob_mutation)

            individual.neural_network.weights[layer] = chromosome
        
    return population