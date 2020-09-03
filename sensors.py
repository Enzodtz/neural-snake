import math

sqrt2 = math.sqrt(2)

def wallSensors(snake_game):

    wall_sensor = [0, 0, 0, 0, 0, 0, 0, 0]    

    snake_head = snake_game.snake[0].copy()

    wall_sensor[0] = snake_head[1]
    wall_sensor[2] = snake_game.GAME_SIZE_X - snake_head[0]
    wall_sensor[4] = snake_game.GAME_SIZE_Y - snake_head[1]
    wall_sensor[6] = snake_head[0]

    sensor = 0
    sensor_position = snake_head.copy()
    while True:
        sensor += 1
        sensor_position[0] += 1
        sensor_position[1] -= 1 

        if sensor_position[0] >= snake_game.GAME_SIZE_X or sensor_position[1] < 0: 
            break
    wall_sensor[1] = sensor * sqrt2

    sensor = 0
    sensor_position = snake_head.copy()
    while True:
        sensor += 1
        sensor_position[0] += 1
        sensor_position[1] += 1 

        if sensor_position[0] >= snake_game.GAME_SIZE_X or sensor_position[1] > snake_game.GAME_SIZE_Y: 
            break
    wall_sensor[3] = sensor * sqrt2    

    sensor = 0
    sensor_position = snake_head.copy()
    while True:
        sensor += 1
        sensor_position[0] -= 1
        sensor_position[1] += 1 

        if sensor_position[0] < 0 or sensor_position[1] >= snake_game.GAME_SIZE_Y: 
            break
    wall_sensor[5] = sensor * sqrt2

    sensor = 0
    sensor_position = snake_head.copy()
    while True:
        sensor += 1
        sensor_position[0] -= 1
        sensor_position[1] -= 1 

        if sensor_position[0] < 0 or sensor_position[1] < 0: 
            break
    wall_sensor[7] = sensor * sqrt2

    return wall_sensor

def appleSensors(snake_game):

    apple_sensor = [0, 0, 0, 0, 0, 0, 0, 0]    

    snake_head = snake_game.snake[0].copy()

    apple = snake_game.apple.copy()

    if apple[0] == snake_head[0]:
        if apple[1] > snake_head[1]:
            apple_sensor[4] = 1
        else: 
            apple_sensor[0] = 1

    elif apple[1] == snake_head[1]:
        if apple[0] > snake_head[0]:
            apple_sensor[2] = 1
        else:
            apple_sensor[6] = 1

    else: 
        if apple[0] > snake_head[0]:
            if apple[1] > snake_head[1]:
               apple_sensor[3] = 1
            else: 
                apple_sensor[1] = 1

        else: 
            if apple[1] > snake_head[1]:
                apple_sensor[5] = 1
            else: 
                apple_sensor[7] = 1

    return apple_sensor

def tailSensors(snake_game):

    tail_sensor = [0, 0, 0, 0, 0, 0, 0, 0]    

    snake_head = snake_game.snake[0].copy()
    snake = snake_game.snake

    sensor = 0
    sensor_position = snake_head.copy()
    looping = True
    while looping:
        sensor_position[1] -= 1

        for snake_slice in snake[2:]:
            if sensor_position[0] == snake_slice[0] and sensor_position[1] == snake_slice[1]:
                looping = False
            
        if sensor_position[1] < 0: 
            break 
        sensor += 1           
    tail_sensor[0] = sensor 

    sensor = 0
    sensor_position = snake_head.copy()
    looping = True
    while looping:
        sensor_position[0] += 1

        for snake_slice in snake[2:]:
            if sensor_position[0] == snake_slice[0] and sensor_position[1] == snake_slice[1]:
                looping = False
            
        if sensor_position[0] >= snake_game.GAME_SIZE_X: 
            break            
        sensor += 1
    tail_sensor[2] = sensor 

    sensor = 0
    sensor_position = snake_head.copy()
    looping = True
    while looping:
        sensor_position[1] += 1

        for snake_slice in snake[2:]:
            if sensor_position[0] == snake_slice[0] and sensor_position[1] == snake_slice[1]:
                looping = False
            
        if sensor_position[1] >= snake_game.GAME_SIZE_Y: 
            break            
        sensor += 1
    tail_sensor[4] = sensor 

    sensor = 0
    sensor_position = snake_head.copy()
    looping = True
    while looping:
        sensor_position[0] -= 1

        for snake_slice in snake[2:]:
            if sensor_position[0] == snake_slice[0] and sensor_position[1] == snake_slice[1]:
                looping = False
            
        if sensor_position[0] < 0: 
            break            
        sensor += 1
    tail_sensor[6] = sensor

    sensor = 0
    sensor_position = snake_head.copy()
    looping = True
    while looping:
        sensor_position[0] += 1
        sensor_position[1] -= 1

        for snake_slice in snake[2:]:
            if sensor_position[0] == snake_slice[0] and sensor_position[1] == snake_slice[1]:
                looping = False
            
        if sensor_position[0] >= snake_game.GAME_SIZE_X or sensor_position[1] < 0: 
            break 
        sensor += 1           
    tail_sensor[1] = sensor * sqrt2

    sensor = 0
    sensor_position = snake_head.copy()
    looping = True
    while looping:
        sensor_position[0] += 1
        sensor_position[1] += 1

        for snake_slice in snake[2:]:
            if sensor_position[0] == snake_slice[0] and sensor_position[1] == snake_slice[1]:
                looping = False
            
        if sensor_position[0] >= snake_game.GAME_SIZE_X or sensor_position[1] >= snake_game.GAME_SIZE_Y: 
            break       
        sensor += 1     
    tail_sensor[3] = sensor * sqrt2

    sensor = 0
    sensor_position = snake_head.copy()
    looping = True
    while looping:
        sensor_position[0] -= 1
        sensor_position[1] += 1

        for snake_slice in snake[2:]:
            if sensor_position[0] == snake_slice[0] and sensor_position[1] == snake_slice[1]:
                looping = False
            
        if sensor_position[0] < 0 or sensor_position[1] >= snake_game.GAME_SIZE_Y: 
            break     
        sensor += 1       
    tail_sensor[5] = sensor * sqrt2

    sensor = 0
    sensor_position = snake_head.copy()
    looping = True
    while looping:
        sensor_position[0] -= 1
        sensor_position[1] -= 1

        for snake_slice in snake[2:]:
            if sensor_position[0] == snake_slice[0] and sensor_position[1] == snake_slice[1]:
                looping = False
            
        if sensor_position[0] < 0 or sensor_position[1] < 0: 
            break    
        sensor += 1        
    tail_sensor[7] = sensor * sqrt2

    return tail_sensor

def sensorFlip(snake_direction, sensor):
    
    flipped_sensor = sensor.copy()

    if snake_direction == 'up':
        pass
    
    elif snake_direction == 'right':
        flipped_sensor[0] = sensor[2]
        flipped_sensor[1] = sensor[3]
        flipped_sensor[2] = sensor[4]
        flipped_sensor[3] = sensor[5]
        flipped_sensor[4] = sensor[6]
        flipped_sensor[5] = sensor[7]
        flipped_sensor[6] = sensor[0]
        flipped_sensor[7] = sensor[1]

    elif snake_direction == 'down':
        flipped_sensor[0] = sensor[4]
        flipped_sensor[1] = sensor[5]
        flipped_sensor[2] = sensor[6]
        flipped_sensor[3] = sensor[7]
        flipped_sensor[4] = sensor[0]
        flipped_sensor[5] = sensor[1]
        flipped_sensor[6] = sensor[2]
        flipped_sensor[7] = sensor[3]

    elif snake_direction == 'left':
        flipped_sensor[0] = sensor[6]
        flipped_sensor[1] = sensor[7]
        flipped_sensor[2] = sensor[0]
        flipped_sensor[3] = sensor[1]
        flipped_sensor[4] = sensor[2]
        flipped_sensor[5] = sensor[3]
        flipped_sensor[6] = sensor[4]
        flipped_sensor[7] = sensor[5]

    return flipped_sensor

def getInput(snake_game):

    snake_direction = snake_game.snake_direction

    input_layer = sensorFlip(snake_direction, wallSensors(snake_game))

    input_layer += sensorFlip(snake_direction, appleSensors(snake_game))

    input_layer += sensorFlip(snake_direction, tailSensors(snake_game))
 
    return input_layer

def processOutput(snake_direction, neural_output):

    neural_output = neural_output.index(max(neural_output))

    if snake_direction == 'up':
        
        if neural_output == 0:
            neural_output = 'left'

        elif neural_output == 1: 
            neural_output = 'up'

        else:
            neural_output = 'right'

    elif snake_direction == 'right':
        
        if neural_output == 0:
            neural_output = 'up'

        elif neural_output == 1: 
            neural_output = 'right'

        else:
            neural_output = 'down'

    elif snake_direction == 'down':
        
        if neural_output == 0:
            neural_output = 'right'

        elif neural_output == 1: 
            neural_output = 'down'

        else:
            neural_output = 'left'

    elif snake_direction == 'left':
        
        if neural_output == 0:
            neural_output = 'down'

        elif neural_output == 1: 
            neural_output = 'left'

        else:
            neural_output = 'up'

    return neural_output