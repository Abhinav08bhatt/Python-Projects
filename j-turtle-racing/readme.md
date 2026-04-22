# Turtle Racing Game

A simple and interactive Python script that simulates a race between multiple turtles using the built-in `turtle` graphics module. Users choose how many turtles will compete, and each turtle advances by a random distance until one reaches the finish line.

# Features

- Lets the user choose between **2 and 10 racers**.
- Displays a graphical race window sized at 700×600 pixels.
- Randomly shuffles and assigns colors to the racing turtles.
- Moves each turtle forward by a random distance on every loop iteration.
- Declares the winning turtle’s color once the finish line is reached.

# How It Works

1. The user is prompted to enter the number of racers.
2. The program initializes the turtle screen and creates turtles at evenly spaced positions along the starting line.
3. Each turtle advances randomly, simulating a race.
4. The first turtle to reach the top boundary wins.
5. The winning color is printed to the console.

# Requirements

- Python 3.x  
- Standard library modules: `turtle`, `random`, `time`
