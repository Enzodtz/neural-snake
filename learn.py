from renderer import *
from genetic_algorithm.populations import *
from genetic_algorithm.logger import *

import pickle

# screen = MainWindow()

max_score   = 0
max_fitness = 0
generation  = 0
max_generation_fitnesses = [0]

fitness_threshold = settings.genetic_algorithm['fitness threshold']

population = newPopulation(random_start=True)

while max_fitness < fitness_threshold:

    generation += 1
    max_generation_fitnesses.append(0)

    while not population.finished:

        # screen.update(population, generation, max_score, max_generation_fitnesses)
        updateConsole(generation, population, max_score)
        population.update()

        max_score = max(population.max_score, max_score)
        max_fitness = max(population.max_fitness, max_fitness)

        max_generation_fitnesses[-1] = population.max_fitness

    best_individual = sorted(population.individuals, key=lambda individual: individual.fitness, reverse=True)
    with open("winner_network", "wb") as file:
        pickle.dump(best_individual[0], file, protocol=pickle.HIGHEST_PROTOCOL)

    population = newPopulation(last_population=population)

