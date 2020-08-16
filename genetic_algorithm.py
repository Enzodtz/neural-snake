import neural_network as nn
import game
import sensors

class GeneticAlgorithm():
    
    def __init__(self, nn_size, population_size, initial_population_size): 

        self.population = []
        self.games = []

        for i in range(initial_population_size):

            self.population.append(nn.NeuralNetwork(nn_size))
            self.population[-1].weights, self.population[-1].biases = nn.networkRandomStart(nn_size)
            self.games.append(game.SnakeGame())

    def populationCicle(self):

        snakes = [True for i in range(len(self.population))]
        while sum(snakes) !=  0:

            for i in range(len(self.population)):
            
                if self.games[i].snake_alive:
                    input_layer = sensors.getInput(self.games[i])
                    neural_output = self.population[i].cicle(input_layer)
                    neural_output = nn.processOutput(self.games[i].snake_direction, neural_output)
                    self.games[i].gameCicle(neural_output)

                else: 
                    snakes[i] = False

        self.scores = []
        for game in self.games:
            self.scores.append(game.score)