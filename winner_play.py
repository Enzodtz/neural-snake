from render import Renderer
from game import SnakeGame
from sensors import getInput, processOutput

import pickle

with open('winner_network', 'rb') as winner_file:
    winner_network = pickle.load(winner_file)

renderer = Renderer()

while True:

    game = SnakeGame()
    i = 0

    while game.snake_alive:

        i += 1

        renderer.update(game)
        
        input_layer = getInput(game)

        output = winner_network.activate(input_layer)

        output = processOutput(game.snake_direction, output)

        game.step(output)