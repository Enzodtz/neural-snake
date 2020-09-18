import sys
sys.path.append(".")

from game.snake import *
from game.vision import *
from neural_network import *
from genetic_algorithm.fitness_function import *

class Individual():

    def __init__(self):

        self.game = SnakeGame()
        self.neural_network = NeuralNetwork()
        self.fitness = 0
        self.playing = True

    def update(self):
        
        if self.game.snake_alive:

            input_layer = getInput(self.game)
            output_layer = self.neural_network.feedFoward(input_layer)
            action = processOutput(self.game.snake_direction, output_layer)
            self.game.step(action)
            self.fitness = fitnessFunction(self.game.steps, self.game.score)

        self.playing = self.game.snake_alive
    
    def viewFitness(self):
        return self.fitness