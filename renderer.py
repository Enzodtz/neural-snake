import pygame
from pygame.locals import *
import settings
from charts import *

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,25)

class MainWindow():
    def __init__(self):

        self.TILE_SIZE = settings.screen['tile size']
        self.FONT_SIZE = settings.screen['font size']
        self.PADDING = settings.screen['padding']

        self.BORDER_HORIZONTAL  = self.TILE_SIZE * settings.snake_game['game size x']
        self.BORDER_VERTICAL  = self.TILE_SIZE * settings.snake_game['game size y']

        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((1360,768), pygame.RESIZABLE)
        pygame.display.set_caption('neural-snake')

        self.clock = pygame.time.Clock()
        self.fps = 5

        self.snake_texture = pygame.Surface((self.TILE_SIZE, self.TILE_SIZE))
        self.snake_texture.fill((255, 255, 255))

        self.apple_texture = pygame.Surface((self.TILE_SIZE, self.TILE_SIZE))
        self.apple_texture.fill((255, 0, 0))

        self.line_texture_horizontal = pygame.Surface((self.BORDER_HORIZONTAL + 2, 2))
        self.line_texture_horizontal.fill((255, 255, 255))

        self.line_texture_vertical = pygame.Surface((2, self.BORDER_VERTICAL))
        self.line_texture_vertical.fill((255, 255, 255))

        self.text_texture = pygame.font.SysFont('Calibri', self.FONT_SIZE)

        self.render = True
        self.generation_max_fitness_last = None

    def update(self, population, generation, max_score, max_generation_fitnesses):

        snake_game = population.individuals[population.actual_individual].game

        if self.render:

            self.clock.tick(self.fps)

            self.screen.fill((0, 0, 0))

            for snake_piece in snake_game.snake:
                self.screen.blit(self.snake_texture, [snake_piece[0] * self.TILE_SIZE, snake_piece[1] * self.TILE_SIZE])

            apple = [snake_game.apple[0] * self.TILE_SIZE, snake_game.apple[1] * self.TILE_SIZE]

            self.screen.blit(self.apple_texture, apple)

            self.screen.blit(self.line_texture_horizontal, (0, self.BORDER_HORIZONTAL))
            self.screen.blit(self.line_texture_vertical, (self.BORDER_VERTICAL, 0))

            generation_text = 'Generation: ' + str(generation)
            generation_text = self.text_texture.render(generation_text, False, (255, 255, 255))
            self.screen.blit(generation_text, (2, self.BORDER_VERTICAL + self.PADDING))

            element_text = 'Element: ' + str(population.actual_individual+1) + ' / ' + str(population.size)
            element_text = self.text_texture.render(element_text, False, (255, 255, 255))
            self.screen.blit(element_text, (2, self.BORDER_VERTICAL + 1 * (self.FONT_SIZE + self.PADDING) + self.PADDING))

            score_text = self.text_texture.render('Actual Score: ' + str(snake_game.score), False, (255, 255, 255))
            self.screen.blit(score_text, (2, self.BORDER_VERTICAL + 2 * (self.FONT_SIZE + self.PADDING) + self.PADDING))
            
            max_score_text = self.text_texture.render('Max Score: ' + str(max_score), False, (255, 255, 255))
            self.screen.blit(max_score_text, (2, self.BORDER_VERTICAL + 3 * (self.FONT_SIZE + self.PADDING) + self.PADDING))

            fitness_text = 'Actual Fitness: ' + str(population.individuals[population.actual_individual].fitness)
            fitness_text = self.text_texture.render(fitness_text, False, (255, 255, 255))
            self.screen.blit(fitness_text, (2, self.BORDER_VERTICAL + 4 * (self.FONT_SIZE + self.PADDING) + self.PADDING))
            
            speed_text = self.text_texture.render('FPS: ' + str(self.fps), False, (255, 255, 255))
            self.screen.blit(speed_text, (2, self.BORDER_VERTICAL + 5 * (self.FONT_SIZE + self.PADDING) + self.PADDING))
 
            if self.generation_max_fitness_last != population.max_fitness:
                fitnessChart(generation, max_generation_fitnesses)
                self.chart_img = pygame.image.load('fitnesses.png')

            self.screen.blit(self.chart_img, (self.BORDER_HORIZONTAL + 50, 0))

        self.generation_max_fitness_last = population.max_fitness

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    self.render = not self.render
                if event.key == K_LEFT:
                    self.fps -= 1
                if event.key == K_RIGHT:
                    self.fps += 1
                if event.key == K_UP:
                    self.fps += 5
                if event.key == K_DOWN:
                    self.fps -= 5

        pygame.display.update()