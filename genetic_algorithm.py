import neural_network as nn
import game
import sensors
import random

class GeneticAlgorithm():
    
    def __init__(self, nn_size, population_size, initial_population_size, parents_number): 

        if parents_number % 2 != 0:
            raise Exception("Parents Number must be even")

        self.generations = 1 
        self.population = []
        self.games = []
        self.parents_number = parents_number
        self.nn_size = nn_size

        self.weights_number = 0
        for i in range(len(nn_size)-1):
            self.weights_number =+ nn_size[i] * nn_size[i+1]

        self.biases_number = sum(nn_size[1:])

        for i in range(initial_population_size):

            self.population.append(nn.NeuralNetwork(nn_size))
            self.population[-1].weights, self.population[-1].biases = nn.networkRandomStart(nn_size)
            self.games.append(game.SnakeGame())

    def cicle(self):
        self.playGames()
        self.newPopulation()

    def newPopulation():

        self.generations += 1 
        self.population = []
        self.games = []

        for i in range(initial_population_size):

            self.population.append(nn.NeuralNetwork(nn_size))
            self.games.append(game.SnakeGame())

        self.parentSelection()
        self.parentCrossover()

    def playGames(self):

        self.generations += 1

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

        self.fitness = []
        for game in self.games:
            self.fitness.append(game.score)

    def parentSelection(self):

        self.parents = []
        fitness_sum = sum(self.fitness)

        for _ in self.parents_number: 

            random_number = random.random() * fitness_sum
            selection_sum = 0
            for fit in self.fitness: 
                selection_sum += fit
                if selection_sum > random_number:
                    self.parents.append(self.population[self.fitenss.index(fit)])

    def parentCrossover(self):

        element = 0

        while element < len(self.population):

            for i in range(0, self.parents_number, 2):

                weight_divisions = [random.randint(0, self.weights_number), random.randint(0, self.weights_number)]
                bias_divisions = [random.randint(0, self.biases_number), random.randint(0, self.biases_number)]
                parents = [self.parents[0], self.parents[1]] 

                weights = []
                parent_using = 0
                creation_controller = 0

                for layer in self.nn_size[:-1]:
                    weights.append([])
                    layer_index = self.nn_size.index(layer)

                    for neuron in range(layer): 
                        weights[-1].append([])

                        for connection in range(self.nn_size[layer_index+1]):
                            
                            if creation_controller >= weight_divisions[0] and creation_controller <= weight_divisions[1]:
                                parent_using = 1
                            else: 
                                parent_using = 0

                            weights[-1][-1].append(parents[parent_using].weights[layer_index][neuron][connection])
                            creation_controller += 1

                biases = []
                creation_controller = 0

                for layer in self.nn_size[1:]:
                    biases.append([])
                    layer_index = self.nn_size.index(layer)

                    for neuron in range(layer):

                        if creation_controller >= bias_divisions[0] and creation_controller <= bias_divisions[1]:
                            parent_using = 1
                        else: 
                            parent_using = 0

                        biases[-1].append(parents[parent_using].biases[layer_index][neuron])

                self.population[element].weights = weights
                self.population[element].biases = biases

                element += 1
                if element == len(self.population):
                    break