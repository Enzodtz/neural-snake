# neural-snake

A neural network project developed to play the snake game.

<h1>The game</h1>

Snake Game is a popular game, and the objective of it, is to take the most apples as you can. 

The architeture of it is a simple 50x50 board (or any dimension) where you start with a small snake with size 3, and in a random place an apple will be generated. Each apple you take will increase your snake lenght by one, and will generate other apple outside of your snake. If you take 247 apples, then the game ends.

<h1>The neural network</h1>

The neural network is a 2 layer perceptron network, with: 

*24 inputs
*1 hidden layer with 16 neurons
*3 outputs

<h3>Input Layer</h3>

The input layer is based in the snake head, imagine that there's a circle on it, and you draw 8 equidistant lines, then, each line will be able to see:

*The distance to the wall (float)
*-The distance to its tail (float)
*If there is any apple (binary)

But, when the snake rotates, our circle needs to rotate too, so the lines that you drew before needs to rotate every time that you change the snake direction, each line will rotate 90 degrees.

And then, we flat this 8x3 matrix into a 24x1 array, and use this as our inputs.

<h3>Hidden Layer</h3>

Here, we don't have much to explain, basically we are using 16 neurons on it, and its activation function is ReLU, you may change it to sigmoid, but this is more computational expensive, and we don't want this in this case.

<h3>Output Layer</h3>

In the output layer, we have 3 outputs, and you may wonder why we have 3 outputs if the game has 4 possible directions. To explain this, we need to remember that the sensors were rotated with the snake head movements, then the outputs needs to be relative to the snake's head, so we got the following outputs: 

*Turn left
*Keep going
*Turn right

For example, if the snake is going right and the output is to turn left, then the direction will be up.

We could made this using 4 outputs and don't rotating the sensor, but I prefered doing this way because we make the network more simple.
