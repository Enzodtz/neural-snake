import sys
sys.path.append(".")

from genetic_algorithm.individuals import *
from genetic_algorithm.random_start import *
from genetic_algorithm.parent_selection import *
from genetic_algorithm.parent_crossover import *
from genetic_algorithm.mutations import *
import settings

class Population():
    
    def __init__(self):
        
        self.size = settings.population['population size']
        if self.size % 2 != 0:
            raise Exception('Population size needs to be odd!')
        
        self.individuals = []
        for _ in range(self.size):
            self.individuals.append(Individual())

        self.actual_individual = 0
        self.max_fitness = 0
        self.max_score = 0
        self.finished = False

    def update(self):
        
        if self.individuals[self.actual_individual].playing:
            self.individuals[self.actual_individual].update()
        
        self.max_score = max(self.individuals[self.actual_individual].game.score, self.max_score)
        self.max_fitness = max(self.individuals[self.actual_individual].fitness, self.max_fitness)

        if not self.individuals[self.actual_individual].playing:
            self.actual_individual += 1
            if self.actual_individual == self.size:
                self.finished = True

def newPopulation(random_start=False, last_population=None):

    population = Population()

    if random_start:

        population = randomStart(population)

    else:

        parents = parentSelection(last_population)
        population = parentCrossover(population, parents)
        population = mutate(population)

    return population