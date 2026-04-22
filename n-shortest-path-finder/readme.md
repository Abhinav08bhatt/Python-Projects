# Maze Solver (personal favorite)

A terminal-based maze solving program that uses Breadth-First Search (BFS) to find the shortest path from the start O to the exit X, while animating the process using the curses module.

## Requirements :

Users must choose a maze layout before the program starts.

The maze must contain:

O as the starting point
X as the goal point
/# as walls
spaces as open paths

- The program must use the BFS algorithm to guarantee the shortest path.
- The solver must explore valid moves in four directions (up, down, left, right).
- The program must visually display the maze and highlight the current path using terminal colors.
- The maze-solving process must be animated with a short delay between steps.
- The program must exit only after displaying the final result and waiting for a key press.