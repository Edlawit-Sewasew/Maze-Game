# Maze Generation and Solving Visualization

This project is a Python maze generation and maze solving visualization program built using the Pygame library.  
The program automatically generates a random maze and visually demonstrates the process of solving it.

---

## Features

- Random maze generation using Depth-First Search (DFS)
- Maze solving visualization
- Real-time animation using Pygame
- Color-coded path visualization
- Interactive graphical window

---

## Technologies Used

- Python
- Pygame

---

## How the Program Works

### Maze Generation
The maze is generated using a depth-first search backtracking algorithm:
1. Start from the first cell
2. Randomly choose an unvisited neighboring cell
3. Remove the wall between cells
4. Continue until all cells are visited

### Maze Solving
The solver searches for a path from the start cell to the destination:
- Red circles represent the current search path
- Blue circles represent dead ends

---

## Installation

### 1. Install Python
Download Python from the official website:

https://www.python.org/downloads/

### 2. Install Pygame

Open terminal or command prompt and run:

```bash
pip install pygame
```

If you experience issues with Python 3.14, use Python 3.12 or install the pre-release version:

```bash
pip install --pre pygame
```

---

## Running the Project

Save the code as:

```bash
maze.py
```

Run the program using:

```bash
python maze.py
```

---

## Project Demo Video

Loom Video Demo:

https://www.loom.com/share/52fcc8e952374b7a95c01fd94d74e78a

---

## Group Members

1. Edlawit Sewasew  
2. Tesnim Mehadi  
3. Hearmon Tesfay  
4. Hailemariam Dagnaw  
5. Hiruy Legesse  
6. Helina Tadesse

---

## Output Visualization

- Black lines → Maze walls
- Red circles → Current exploration path
- Blue circles → Dead-end paths

---

## Future Improvements

- Add keyboard controls
- Add different maze generation algorithms
- Add timer and score system
- Allow user-selected maze sizes
- Add shortest path visualization

---

## License

This project is for educational purposes.