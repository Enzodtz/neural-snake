import pygame
from pygame.locals import *

class Renderer():
    def __init__(self):

        self.TILE_SIZE = 60
        self.SCREEN_SIZE = (800, 600)

        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        pygame.display.set_caption('neural-snake')

        self.clock = pygame.time.Clock()
        self.delay = 5

        self.snake_skin = pygame.Surface((self.TILE_SIZE, self.TILE_SIZE))
        self.snake_skin.fill((255, 255, 255))

        self.apple_skin = pygame.Surface((self.TILE_SIZE, self.TILE_SIZE))
        self.apple_skin.fill((255, 0, 0))

        self.line_skin = pygame.Surface((2, self.SCREEN_SIZE[1]))
        self.line_skin.fill((255, 255, 255))

        self.text_skin = pygame.font.SysFont('Calibri', 15)

        self.render = True

    def update(self, snake_game):

        if self.render:

            self.clock.tick(self.delay)

            self.screen.fill((0, 0, 0))

            score_text = self.text_skin.render('Score: ' + str(snake_game.score), False, (255, 255, 255))
            self.screen.blit(score_text, (2, 0))

            speed_text = self.text_skin.render('Speed: ' + str(self.delay), False, (255, 255, 255))
            self.screen.blit(speed_text, (2, 66))

            for snake_piece in snake_game.snake:
                snake_piece[0] *= self.TILE_SIZE
                snake_piece[1] *= self.TILE_SIZE
                self.screen.blit(self.snake_skin, snake_piece)

            apple = [snake_game.apple[0] * self.TILE_SIZE, snake_game.apple[1] * self.TILE_SIZE]

            self.screen.blit(self.apple_skin, apple)
            self.screen.blit(self.line_skin, (self.SCREEN_SIZE[0] - 200, 0))

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