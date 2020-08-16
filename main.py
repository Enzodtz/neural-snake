import pygame
from pygame.locals import *
import neural_network
import game
import sensors 

pygame.init()
screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption('Snake')

snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255))

apple_skin = pygame.Surface((10,10))
apple_skin.fill((255, 0, 0))

clock = pygame.time.Clock()

line_skin = pygame.Surface((2,600))
line_skin.fill((255, 255, 255))

neural_output = 'left'

while True: 

    neural_output = 'down'
    snake_game = game.SnakeGame() 

    while snake_game.snake_alive: 
        clock.tick(2)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()'

        input_layer = sensors.getInput(snake_game)

        #neural_output = neural_network_cicle(input_layer)

        snake_game.gameCicle(neural_output)

        screen.fill((0,0,0))
        screen.blit(apple_skin, snake_game.apple)
        screen.blit(line_skin, [600, 0])
        for pos in snake_game.snake: 
            screen.blit(snake_skin, pos)
            
        pygame.display.update()