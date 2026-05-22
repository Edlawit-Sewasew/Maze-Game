# maze.py
class Maze:
    def __init__(self, rows, columns):
        self.Row = rows
        self.Column = columns
        
        # northWall[r][c] means the upper cell wall
        self.northWall = []
        for i in range(rows + 1):
            self.northWall.append([])
            for j in range(columns + 1):
                self.northWall[i].append(1)
                
        # eastWall[r][c] means the right side of the wall
        self.eastWall = []
        for i in range(rows + 1):
            self.eastWall.append([])
            for j in range(columns + 1):
                self.eastWall[i].append(1)

        self.visited = []
        for i in range(rows + 1):
            self.visited.append([])
            for j in range(columns + 1):
                self.visited[i].append(False)