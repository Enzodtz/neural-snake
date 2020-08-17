import neural_network as nn
import game
import sensors
import random

class GeneticAlgorithm():
    
    def __init__(self, nn_size, population_size, initial_population_size, parents_number, mutation_rate, condition_to_finish): 

        if parents_number % 2 != 0:
            raise Exception("Parents Number must be even")

        print("\033[2J")
        print('\033[1;0HInitial Generation')

        self.generations = 1 
        self.population = []
        self.games = []
        self.parents_number = parents_number
        self.nn_size = nn_size
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.condition_to_finish = condition_to_finish
        self.steps_to_apple_limit = 250
        self.max_score = 0

        self.weights_number = 0
        for i in range(len(nn_size)-1):
            self.weights_number =+ nn_size[i] * nn_size[i+1]

        self.biases_number = sum(nn_size[1:])

        for i in range(initial_population_size):

            self.population.append(nn.NeuralNetwork(nn_size))
            self.population[-1].weights, self.population[-1].biases = nn.networkRandomStart(nn_size)
            self.games.append(game.SnakeGame(self.steps_to_apple_limit))

    def learn(self):

        learning = True

        while learning:

            self.steps_to_apple_limit += 1
            self.playGames()
            print('\033[5;0HBest Score:', self.best_score, '     ')
            self.newPopulation()
            
            if max(self.fitness) > self.condition_to_finish: 
                learning = False
                    
    def newPopulation(self):

        self.generations += 1 
        print('\033[1;0HGeneration', self.generations, '         ')
        print('\033[6;0HSteps Limit:', self.steps_to_apple_limit)
        self.parentSelection()
        self.population = []
        self.games = []

        for i in range(self.population_size):

            self.population.append(nn.NeuralNetwork(self.nn_size))
            self.games.append(game.SnakeGame(self.steps_to_apple_limit))

        self.parentCrossover()
        self.swapMutation

    def playGames(self):

        self.fitness = [0 for i in self.games]
        self.steps = 0

        snakes = [True for i in range(len(self.population))]
        while sum(snakes) !=  0:
            
            self.steps += 1 

            print('\033[2;0HElements Alive:', sum(snakes), '         ')
            print('\033[3;0HActual Best Score:', max(self.fitness), '      ')
            print('\033[4;0HActual Steps:', self.steps, '      ')

            for i in range(len(self.population)):

                if self.games[i].snake_alive:
                    input_layer = sensors.getInput(self.games[i])
                    neural_output = self.population[i].cicle(input_layer)
                    neural_output = nn.processOutput(self.games[i].snake_direction, neural_output)
                    self.games[i].gameCicle(neural_output)
                    self.fitness[i] = (self.games[i].score)

                else: 
                    snakes[i] = False

        self.best_score = max(self.fitness)

    def parentSelection(self):

        self.parents = []
        fitness_sum = sum(self.fitness)

        for _ in range(self.parents_number): 

            random_number = random.random() * fitness_sum
            selection_sum = 0
            for fit in self.fitness: 
                selection_sum += fit
                if selection_sum >= random_number:
                    self.parents.append(self.population[self.fitness.index(fit)])
                    break

    def parentCrossover(self):

        element = 0

        while element < len(self.population):

            for i in range(0, self.parents_number, 2):

                weight_divisions = [random.randint(1, self.weights_number), 0]
                weight_divisions[1] = random.randint(weight_divisions[0], self.weights_number)
                bias_divisions = [random.randint(1, self.biases_number), 0]
                bias_divisions[1] = random.randint(bias_divisions[0], self.biases_number), 0
                parents = [self.parents[i], self.parents[i+1]] 

                weights = []
                parent_using = 0
                creation_controller = 0

                for layer in self.nn_size[:-1]:
                    weights.append([])
                    layer_index = self.nn_size[:-1].index(layer)

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
                    layer_index = self.nn_size[1:].index(layer)

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

    def swapMutation(self):
        
        for element in self.population:

            if random.random() <= mutation_rate:
                
                elements = [random.randint(1, self.weights_number), random.randint(1, self.weights_number)]
                coordinates = [0, 0]
                counter = 0

                for layer in range(element.weights):
                    for neuron in range(element.weights[layer]):
                        for connection in range(element.weights[layer][neuron]):        
                            
                            counter += 1
                            if counter == elements[0]:
                                coordinates[0] = [layer, neuron, connection]
                            if counter == elements[1]:
                                coordinates[1] = [layer, neuron, connection]

                auxiliar = element.weights[coordinates[0][0]][coordinates[0][1]][coordinates[0][2]]
                element.weights[coordinates[0][0]][coordinates[0][1]][coordinates[0][2]] = element.weights[coordinates[1][0]][coordinates[1][1]][coordinates[1][2]]
                element.weights[coordinates[1][0]][coordinates[1][1]][coordinates[1][2]] = auxiliar

ga = GeneticAlgorithm([24, 16, 3], 2000, 10000, 4, 0.015, 10)
ga.learn()