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

def getInput(snake_game):

    names = ['90', '45', '0', '315', '270', '225', '180', '135']

    print("\033c")
    print('\033[0;0HName | Wall Sensor | Apple Sensor | Tail Sensor')

    wall_sensor = wallSensors(snake_game)

    apple_sensor = appleSensors(snake_game)

    tail_sensor = tailSensors(snake_game)

    for i in range(8):
        print('\033['+ str(i+2) +';0H'   + names[i])
        print('\033['+ str(i+2) +';6H| %.5f' %(wall_sensor[i]))
        print('\033['+ str(i+2) +';20H|' + str(apple_sensor[i]))
        print('\033['+ str(i+2) +';35H| %.5f' %(tail_sensor[i]))

    #input_layer = []

    #input_layer += wallSensors(snake_game)
    
    #input_layer += appleSensors(snake_game)

    #input_layer += tailSensors(snake_game)

    # return input_layer
    return 1