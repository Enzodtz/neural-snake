import sys
sys.path.append(".")

import numpy as np
import random
import settings

def elitismSelection(population, num_parents):

    individuals = sorted(population.individuals, key=lambda individual: individual.fitness, reverse=True)
    
    return individuals[:num_parents]

def rouletteWheelSelection(population, num_parents):

    selection = []
    wheel = sum(individual.fitness for individual in population.individuals)

    for _ in range(num_parents):

        rand = random.uniform(0, wheel)
        current = 0
        
        for individual in population.individuals:
            current += individual.fitness
            if current > rand:
                selection.append(individual)
                break

    return selection

def tournamentSelection(population, num_parents, tournament_size):

    selection = []

    for _ in range(num_parents):

        tournament = np.random.choice(population.individuals, tournament_size)
        best_from_tournament = max(tournament, key = lambda individual: individual.fitness)
        selection.append(best_from_tournament)

    return selection

def parentSelection(population):

    num_parents = settings.genetic_algorithm['parents number']                          
    selection_type = settings.genetic_algorithm['parents selection type']

    if selection_type == 'roulette wheel':
        parents = rouletteWheelSelection(population, num_parents)

    elif selection_type == 'elitism selection':
        parents = elitismSelection(population, num_parents)

    elif selection_type == 'tournament selection':
        tournament_size = settings.genetic_algorithm['tournament size']
        parents = tournamentSelection(population, num_parents, tournament_size)

    else:
        raise Exception("Parent selection not found")

    return parents