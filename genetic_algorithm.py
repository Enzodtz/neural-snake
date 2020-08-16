import neural_network as nn
import game
import sensors

class GeneticAlgorithm():
    
    def __init__(self, nn_size, population_size, initial_population_size): 

        self.population = []
        for i in range(initial_population_size):
            self.population.append(nn.NeuralNetwork())
            self.population[i].biases = [np.random.randn(layer, 1) for layer in nn_size[1:]]
            self.population[i].weights = [np.random.randn(layer, next_layer) for layer, next_layer in zip(nn_size[:-1], nn_size[1:])]

        self.games = []
        for i in range(initial_population_size):
            self.games.append(game.SnakeGame())

    def populationCicle(self):

        snakes = [True for i in range(len(self.population))]
        while sum(snakes) !=  0:

            for i in range(len(self.population)):
            
                if self.games[i].snake_alive:

                    input_layer = sensors.getInput(self.games[i])
                    neural_output = self.population[i].cicle(input_layer)
                    self.games[i].gameCicle(neural_output)

                else: 
                    snakes[i] = False

        self.scores = []
        for game in self.games:
            score = game.apples
            scores.append(game)
            