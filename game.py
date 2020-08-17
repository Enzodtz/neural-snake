import random

class SnakeGame():

    def __init__(self, steps_to_apple_limit):

        self.snake = [random.randint(0, 59) * 10, random.randint(0, 59) * 10]
        self.apple = [random.randint(0, 59) * 10, random.randint(0, 59) * 10]
        while self.apple in self.snake:
            self.apple = [random.randint(0, 59) * 10, random.randint(0, 59) * 10]
            
        self.snake_direction = 'down'
        self.snake_alive = True
        self.score = 0 
        self.steps = 0
        self.steps_to_apple = 0
        self.steps_to_apple_limit = steps_to_apple_limit

    def gameCicle(self, neural_output):

        self.steps += 1
        self.steps_to_apple += 1

        self.snake_direction = neural_output

        snake_tail = self.snake[-1]

        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i] = [self.snake[i-1][0], self.snake[i-1][1]]

        if self.snake_direction == 'up': 
            self.snake[0][1] +=  -10
        if self.snake_direction == 'left': 
            self.snake[0][0] +=  -10
        if self.snake_direction == 'down': 
            self.snake[0][1] +=  10
        if self.snake_direction == 'right': 
            self.snake[0][0] +=  10

        if self.snake[0] == self.apple: 
            self.snake.append(snake_tail)
            self.score += 1
            self.steps_to_apple = 0
            won = True if self.score >= 247 else False
            while self.apple in self.snake and not won:
                self.apple = [random.randint(0, 59) * 10, random.randint(0, 59) * 10]

        if self.steps_to_apple > self.steps_to_apple_limit: 
            self.snake_alive = False

        if self.snake[0][0] == 600 or self.snake[0][0] == -10 or self.snake[0][1] == -10 or self.snake[0][1] == 600:
            self.snake_alive = False

        for pos in self.snake[2:]:
            if self.snake[0][0] == pos[0] and self.snake[0][1] == pos[1]:
                self.snake_alive = False