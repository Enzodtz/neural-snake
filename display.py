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
        self.delay = 5

        self.snake_skin = pygame.Surface((10, 10))
        self.snake_skin.fill((255, 255, 255))

        self.apple_skin = pygame.Surface((10, 10))
        self.apple_skin.fill((255, 0, 0))

        self.line_skin = pygame.Surface((2, 600))
        self.line_skin.fill((255, 255, 255))

        self.text_skin = pygame.font.SysFont('Calibri', 30)

        self.render = True

    def update(self, snake_game, best_score, generation, element):

        if self.render:

            self.clock.tick(self.delay)

            self.screen.fill((0, 0, 0))

            generation_text = self.text_skin.render('Generation: ' + str(generation), False, (255, 255, 255))
            self.screen.blit(generation_text, (604, 2))

            element_text = self.text_skin.render('Element: ' + str(element), False, (255, 255, 255))
            self.screen.blit(element_text, (604, 34))

            score_text = self.text_skin.render('Actual Fitness: ' + str(snake_game.score), False, (255, 255, 255))
            self.screen.blit(score_text, (604, 66))

            best_score_text = self.text_skin.render('Best Fitness: ' + str(best_score), False, (255, 255, 255))
            self.screen.blit(best_score_text, (604, 98))

            speed_text = self.text_skin.render('Display Speed: ' + str(self.delay), False, (255, 255, 255))
            self.screen.blit(speed_text, (604, 130))

            for snake_piece in snake_game.snake:
                self.screen.blit(self.snake_skin, snake_piece)

            self.screen.blit(self.apple_skin, snake_game.apple)
            self.screen.blit(self.line_skin, (600,0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    self.render = not self.render
                if event.key == K_LEFT:
                    self.delay += 1
                if event.key == K_RIGHT:
                    self.delay -= 1
                if event.key == K_UP:
                    self.delay += 5
                if event.key == K_DOWN:
                    self.delay -= 5

        pygame.display.update()