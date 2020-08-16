import math

sqrt2 = math.sqrt(2)

def wallSensors(snake_game):

    wall_sensor = [0, 0, 0, 0, 0, 0, 0, 0]    

    snake_head = [snake_game.snake[0][0]/10, snake_game.snake[0][1]/10]

    wall_sensor[0] = snake_head[1]
    wall_sensor[2] = 60 - snake_head[0]
    wall_sensor[4] = 60 - snake_head[1]
    wall_sensor[6] = snake_head[0]

    sensor = 0
    sensor_position = snake_head.copy()
    while True:
        sensor += 1
        sensor_position[0] += 1
        sensor_position[1] -= 1 

        if sensor_position[0] > 60 or sensor_position[1] < 0: 
            break
    wall_sensor[1] = sensor * sqrt2

    sensor = 0
    sensor_position = snake_head.copy()
    while True:
        sensor += 1
        sensor_position[0] += 1
        sensor_position[1] += 1 

        if sensor_position[0] > 60 or sensor_position[1] > 60: 
            break
    wall_sensor[3] = sensor * sqrt2    

    sensor = 0
    sensor_position = snake_head.copy()
    while True:
        sensor += 1
        sensor_position[0] -= 1
        sensor_position[1] += 1 

        if sensor_position[0] < 0 or sensor_position[1] > 60: 
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

    snake_head = [snake_game.snake[0][0]/10, snake_game.snake[0][1]/10]

    apple = [snake_game.apple[0]/10, snake_game.apple[1]/10]

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

    snake_head = [snake_game.snake[0][0]/10, snake_game.snake[0][1]/10]
    snake = snake_game.snake

    sensor = 0
    sensor_position = snake_head.copy()
    looping = True
    while looping:
        sensor_position[1] -= 1

        for snake_slice in snake[2:]:
            if sensor_position[0] == snake_slice[0]/10 and sensor_position[1] == snake_slice[1]/10:
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
            if sensor_position[0] == snake_slice[0]/10 and sensor_position[1] == snake_slice[1]/10:
                looping = False
            
        if sensor_position[0] > 60: 
            break            
        sensor += 1
    tail_sensor[2] = sensor 

    sensor = 0
    sensor_position = snake_head.copy()
    looping = True
    while looping:
        sensor_position[1] += 1

        for snake_slice in snake[2:]:
            if sensor_position[0] == snake_slice[0]/10 and sensor_position[1] == snake_slice[1]/10:
                looping = False
            
        if sensor_position[1] > 60: 
            break            
        sensor += 1
    tail_sensor[4] = sensor 

    sensor = 0
    sensor_position = snake_head.copy()
    looping = True
    while looping:
        sensor_position[0] -= 1

        for snake_slice in snake[2:]:
            if sensor_position[0] == snake_slice[0]/10 and sensor_position[1] == snake_slice[1]/10:
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
            if sensor_position[0] == snake_slice[0]/10 and sensor_position[1] == snake_slice[1]/10:
                looping = False
            
        if sensor_position[0] > 60 or sensor_position[1] < 0: 
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
            if sensor_position[0] == snake_slice[0]/10 and sensor_position[1] == snake_slice[1]/10:
                looping = False
            
        if sensor_position[0] > 60 or sensor_position[1] > 60: 
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
            if sensor_position[0] == snake_slice[0]/10 and sensor_position[1] == snake_slice[1]/10:
                looping = False
            
        if sensor_position[0] < 0 or sensor_position[1] > 60: 
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
            if sensor_position[0] == snake_slice[0]/10 and sensor_position[1] == snake_slice[1]/10:
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