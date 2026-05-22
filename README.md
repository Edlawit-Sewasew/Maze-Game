⚙️ Core Logic Flow
When executed, main.py drives the application through four distinct execution phases:

Plaintext
  [1. Initialization]  ──> Instantiates Pygame window & the global Maze grid data.
          │
          ▼
  [2. Generation]      ──> Executes the visual, real-time maze building animation.
          │
          ▼
  [3. Pathfinding]     ──> Triggers the autonomous solver to find the optimal path.
          │
          ▼
  [4. Execution Loop]  ──> Keeps the final canvas open until the user manually exits.
📦 Imported Dependencies
To maintain a clean separation of concerns, main.py acts as the system "glue" by pulling in components from the other 5 team modules:

config: Imports layout configurations (Width, Height, Row, Column).

maze: Imports the structural grid blueprint (Maze).

generator: Imports the randomized path-carving algorithm (formMaze).

solver: Imports the coordinate navigation system (win).

renderer: Imports the drawing routines (draw_maze, drawing_cell).
