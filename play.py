import pickle
from renderer import *
from genetic_algorithm.populations import *
from game.snake import *

screen = MainWindow()

population = newPopulation(random_start=True)

with open('winner_network', 'rb') as file:
    population.individuals[0] = pickle.load(file)
    
population.actual_individual = 0

while True:
        
    population.individuals[0].game = SnakeGame()

    while population.individuals[0].game.snake_alive:
        screen.update(population, 0, 0, [0])
        population.individuals[0].update()