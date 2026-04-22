import curses
from curses import wrapper
import queue
import time

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

maze_small = [
    ["#", "#", "#", "#", "#"],
    ["#", "O", " ", " ", "#"],
    ["#", " ", "#", " ", "#"],
    ["#", " ", " ", "X", "#"],
    ["#", "#", "#", "#", "#"]
]

maze_big = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "O", " ", " ", " ", "#", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", " ", "#", "#", " ", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", "#", "#", "#", "#", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", "#"],
    ["#", "#", "#", "#", " ", "#", " ", "#", "#", "#", " ", "#"],
    ["#", " ", " ", "#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]

maze_easy = [
    ["#", "#", "#", "#", "#", "#", "#"],
    ["#", "O", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", " ", "X", "#"],
    ["#", "#", "#", "#", "#", "#", "#"]
]

maze_complex = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "O", " ", " ", "#", " ", " ", " ", " ", "#"],
    ["#", "#", "#", " ", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", " ", "#"],
    ["#", " ", "#", "#", "#", " ", "#", " ", "#", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", "#", "#"],
    ["#", "#", "#", " ", "#", "#", "#", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", "#", "#", " ", "#"],
    ["#", " ", "#", "#", "#", " ", " ", " ", "X", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]


def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j * 2, "X", RED)
            else:
                stdscr.addstr(i, j * 2, value, BLUE)


def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
    return None


def find_neighbors(maze, row, col):
    neighbors = []

    if row > 0:
        neighbors.append((row - 1, col))
    if row + 1 < len(maze):
        neighbors.append((row + 1, col))
    if col > 0:
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]):
        neighbors.append((row, col + 1))

    return neighbors


def find_path(maze, stdscr):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)

    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    visited = set()
    visited.add(start_pos)

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.2)
        stdscr.refresh()

        if maze[row][col] == end:
            return path

        for neighbor in find_neighbors(maze, row, col):
            if neighbor in visited:
                continue

            r, c = neighbor
            if maze[r][c] == "#":
                continue

            visited.add(neighbor)
            q.put((neighbor, path + [neighbor]))


selected_maze = maze


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    find_path(selected_maze, stdscr)
    stdscr.getch()


print("Choose a maze:")
print("1. Default Maze")
print("2. Small Maze")
print("3. Big Maze")
print("4. Easy Maze")
print("5. Complex Maze")

choice = input("Enter your choice (1-5): ")

if choice == "1":
    selected_maze = maze
elif choice == "2":
    selected_maze = maze_small
elif choice == "3":
    selected_maze = maze_big
elif choice == "4":
    selected_maze = maze_easy
elif choice == "5":
    selected_maze = maze_complex
else:
    print("Invalid choice! Default maze selected.")
    selected_maze = maze


wrapper(main)