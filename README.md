# neural-snake

An AI project developed to play the snake game.

<h1>The game</h1>

Snake Game is a popular game, and the goal of it, is to take the most apples as you can. 

The architeture of it is a simple 50x50 board (or any dimension) where you start with a small snake with size 1, and in a random place an apple will be generated. Each apple you take will increase your snake lenght by one, and will generate other apple outside of your snake. If you take 249 apples, then the game ends.

<h1>The neural network</h1>

The neural network starts with 24 inputs, then we got more 12 hidden neurons, and a 3 neuron output.

<h3>Input Layer</h3>

The input layer is based in the snake head, imagine that there's a circle on it, and you draw 8 equidistant lines, then, each line will be able to see:

* The distance to the wall (float)
* The distance to its tail (float)
* If there is any apple (binary)

But, when the snake rotates, our circle needs to rotate too, so the lines that you drew before needs to rotate every time that you change the snake direction, each line will rotate 90 degrees.

And then, we flat this 8x3 matrix into a 24x1 array, and use this as our inputs.

<h3>Hidden Layer</h3>

Here, we don't have much to explain, basically we are using 12 neurons on it, but it can be changed by the genetic algorithm.

<h3>Output Layer</h3>

In the output layer, we have 3 outputs, and you may wonder why we have 3 outputs if the game has 4 possible directions. To explain this, we need to remember that the sensors were rotated with the snake head movements, then the outputs needs to be relative to the snake's head, so we got the following outputs: 

* Turn left
* Keep going
* Turn right

For example, if the snake is going right and the output is to turn left, then the direction will be up.

We could made this using 4 outputs and don't rotating the sensor, but I prefered doing this way because we make the network more simple.
