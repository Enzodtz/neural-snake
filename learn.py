from game import SnakeGame
from sensors import getInput, processOutput

import os
import neat
import visualize
import pickle

def eval_genome(genome, config):

    net = neat.nn.FeedForwardNetwork.create(genome, config)
    game = SnakeGame()

    while game.snake_alive:

        input_layer = getInput(game)

        output = net.activate(input_layer)
        output = processOutput(game.snake_direction, output)

        game.step(output)

    return game.score

if __name__ == '__main__':

    local_dir = os.path.dirname(__file__)
    config_file = os.path.join(local_dir, 'config')
    
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                        neat.DefaultSpeciesSet, neat.DefaultStagnation,
                        config_file)

    population = neat.Population(config)
    # population = neat.Checkpointer().restore_checkpoint(local_dir + '/neat-checkpoint-823')

    population.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    population.add_reporter(stats)
    # population.add_reporter(neat.Checkpointer(5))

    threader = neat.ThreadedEvaluator(10, eval_genome,)

    winner = population.run(threader.evaluate)

    threader.stop()

    visualize.plot_stats(stats, ylog=False, view=True)
    visualize.plot_species(stats, view=True)

    winner_network = neat.nn.FeedForwardNetwork.create(winner, config)

    with open("winner_network", "wb") as winner_file:
        pickle.dump(winner_network, winner_file, protocol=pickle.HIGHEST_PROTOCOL)
