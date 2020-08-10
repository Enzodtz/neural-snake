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

        if sensor_position[0] == 60 or sensor_position[1] == 0: 
            break
    wall_sensor[1] = sensor * sqrt2

    sensor = 0
    sensor_position = snake_head.copy()
    while True:
        sensor += 1
        sensor_position[0] += 1
        sensor_position[1] += 1 

        if sensor_position[0] == 60 or sensor_position[1] == 60: 
            break
    wall_sensor[3] = sensor * sqrt2    

    sensor = 0
    sensor_position = snake_head.copy()
    while True:
        sensor += 1
        sensor_position[0] -= 1
        sensor_position[1] += 1 

        if sensor_position[0] == 0 or sensor_position[1] == 60: 
            break
    wall_sensor[5] = sensor * sqrt2

    sensor = 0
    sensor_position = snake_head.copy()
    while True:
        sensor += 1
        sensor_position[0] -= 1
        sensor_position[1] -= 1 

        if sensor_position[0] == 0 or sensor_position[1] == 0: 
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
            if apple[1] > apple[1]:
                apple_sensor[5] = 1
            else: 
                apple_sensor[7] = 1

    return apple_sensor

def getInput(snake_game):

    print('\033c')

    names = ['90', '45', '0', '315', '270', '225', '180', '135']

    input_layer = wallSensors(snake_game)

    print('Wall Sensors')
    for i in range(len(input_layer)):
        print(names[i], input_layer[i])

    input_layer = appleSensors(snake_game)

    print('Apple Sensors')
    for i in range(len(input_layer)):
        print(names[i], input_layer[i])

    #input_layer = []

    #input_layer += wallSensors(snake_game)
    
    #input_layer += appleSensors(snake_game)

    #input_layer += tailSensors(snake_game)

    return input_layer