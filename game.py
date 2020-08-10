import random

class SnakeGame():

    def __init__(self):
        self.snake = [[200, 200], [210, 200], [220, 200]]
        self.apple = [random.randint(0, 59) * 10, random.randint(0, 59) * 10]
        self.snake_direction = 'left'
        self.snake_alive = True
    
    def gameCicle(self, neural_output):

        #self.snake_direction = neural_output

        if self.snake_direction == 'up': 
            self.snake[0][1] +=  -10
        if self.snake_direction == 'left': 
            self.snake[0][0] +=  -10
        if self.snake_direction == 'down': 
            self.snake[0][1] +=  10
        if self.snake_direction == 'right': 
            self.snake[0][0] +=  10

        snake_tail = self.snake[-1]

        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i] = (self.snake[i-1][0], self.snake[i-1][1])

        if self.snake[0] == self.apple: 
            self.snake.append(snake_tail)
            self.apple = [random.randint(0, 59) * 10, random.randint(0, 59) * 10]

        if self.snake[0][0] == 600 or self.snake[0][0] == -10 or self.snake[0][1] == -10 or self.snake[0][1] == 600:
            self.snake_alive = False

        for pos in self.snake[2:]:
            if self.snake[0][0] == pos[0] and self.snake[0][1] == pos[1]:
                self.snake_alive = False