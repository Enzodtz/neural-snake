import pygame
from pygame.locals import *
import neural_network as nn
import game
import sensors

pygame.init()
pygame.font.init()

class Renderer():
    def __init__(self):

        self.screen = pygame.display.set_mode((1200, 600))
        pygame.display.set_caption('neural-snake')

        self.clock = pygame.time.Clock()
        self.delay = 20

        self.snake_skin = pygame.Surface((10, 10))
        self.snake_skin.fill((255, 255, 255))

        self.apple_skin = pygame.Surface((10, 10))
        self.apple_skin.fill((255, 0, 0))

        self.text_skin = pygame.font.SysFont('Calibri', 30)

    def render(self, weights, biases, size, steps_to_apple_limit):

        neural_network = nn.NeuralNetwork(size)

        neural_network.weights = weights
        neural_network.biases = biases
    
        snake_game = game.SnakeGame(steps_to_apple_limit)

        while snake_game.snake_alive:

            self.clock.tick(self.delay)

            input_layer = sensors.getInput(snake_game)
            neural_output = neural_network.cicle(input_layer)
            neural_output = nn.processOutput(snake_game.snake_direction, neural_output)
            snake_game.gameCicle(neural_output)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()

            self.screen.fill((0, 0, 0))

            score_text = self.text_skin.render(str(snake_game.score), False, (255, 255, 255))
            self.screen.blit(score_text, (0, 0))

            for snake_piece in snake_game.snake:
                self.screen.blit(self.snake_skin, snake_piece)

            self.screen.blit(self.apple_skin, snake_game.apple)

            pygame.display.update()