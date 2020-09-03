import random

class SnakeGame():

    def __init__(self):

        self.GAME_SIZE_X = 5
        self.GAME_SIZE_Y = 5
        self.STEPS_TO_APPLE_LIMIT = 25

        self.snake = [[random.randint(0, self.GAME_SIZE_X - 1), random.randint(0, self.GAME_SIZE_Y - 1)]]

        self.apple = [random.randint(0, self.GAME_SIZE_X - 1), random.randint(0, self.GAME_SIZE_Y - 1)]
        while self.apple in self.snake:
            self.apple = [random.randint(0, self.GAME_SIZE_X - 1), random.randint(0, self.GAME_SIZE_Y - 1)]
            
        self.snake_direction = 'down'
        self.snake_alive = True
        self.score = 0 
        self.steps = 0
        self.steps_to_apple = 0

    def step(self, move):

        self.steps += 1
        self.steps_to_apple += 1

        self.snake_direction = move

        snake_tail = self.snake[-1]

        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i] = [self.snake[i-1][0], self.snake[i-1][1]]

        if self.snake_direction == 'up': 
            self.snake[0][1] +=  -1
        if self.snake_direction == 'left': 
            self.snake[0][0] +=  -1
        if self.snake_direction == 'down': 
            self.snake[0][1] +=  1
        if self.snake_direction == 'right': 
            self.snake[0][0] +=  1

        if self.snake[0] == self.apple: 
            self.score += 1
            self.snake.append(snake_tail)
            self.steps_to_apple = 0
            snake_alive = False if self.score >= (self.GAME_SIZE_X * self.GAME_SIZE_Y) - 1 else True         
            while self.apple in self.snake and snake_alive:
                self.apple = [random.randint(0, self.GAME_SIZE_X - 1), random.randint(0, self.GAME_SIZE_Y - 1)]

        if self.steps_to_apple > self.STEPS_TO_APPLE_LIMIT: 
            self.snake_alive = False

        if self.snake[0][0] == self.GAME_SIZE_X or self.snake[0][0] == -1 or self.snake[0][1] == -1 or self.snake[0][1] == self.GAME_SIZE_Y:
            self.snake_alive = False

        for pos in self.snake[2:]:
            if self.snake[0][0] == pos[0] and self.snake[0][1] == pos[1]:
                self.snake_alive = False