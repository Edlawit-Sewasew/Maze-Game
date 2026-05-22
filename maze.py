import pygame
import random

Row = 20
Column = 20
Cell_length = 30
Width = Column * Cell_length
Height = Row * Cell_length
Speed = 60

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

class Maze:
    def __init__(self, rows, columns):
        self.Row = rows
        self.Column = columns
        #northWall[r][c] means the upper cell wall
        #Row+1 means that the edge is also included
        #northWall[0][c] is the bottom edge of the whole maze
        self.northWall = []
        for i in range(rows +1):
            self.northWall.append([])
            for j in range(columns +1):
                self.northWall[i].append(1)
        #eastWall[r][c] means the right side of the wall
        #Column +1 means that the edge is also included
        #eastWall[r][0] is the left edge of the whole maze
        self.eastWall = []
        for i in range(rows +1):
            self.eastWall.append([])
            for j in range(columns+1):
                self.eastWall[i].append(1)

        self.visited = []
        for i in range(rows+1):
            self.visited.append([])
            for j in range(columns +1):
                self.visited[i].append(False)
    
    def draw(self, screen):
        for r in range(1, self.Row+1):
            for c in range(1, self.Column+1):
                x= (c-1) * Cell_length
                y = (self.Row - r) * Cell_length
                #draw north wall which is the top of the current cell
                if self.northWall[r][c]:
                    pygame.draw.line(screen, black, (x,y), (x+ Cell_length, y))
                #draw the east wall which is the right side of the current cell
                if self.eastWall[r][c]:
                    pygame.draw.line(screen, black, (x+ Cell_length, y), (x+ Cell_length, y + Cell_length))
                #draw the south wall which is the bottom side of the current cell
                #when r is 1 self.northWall[0][c] makes a line for the bottom of the maze
                if self.northWall[r-1][c]:
                    pygame.draw.line(screen, black, (x,y+Cell_length), (x+Cell_length, y + Cell_length))
                #draw the west wall which is the left side of the current cell
                #when c is 1 self.eastWall[r][0] makes a line for the left side of the maze
                if self.eastWall[r][c-1]:
                    pygame.draw.line(screen, black, (x,y), (x,y+ Cell_length))

def formMaze(maze, screen):
    buffer = [(1,1)]
    maze.visited[1][1] = True
 
    while buffer:
        r ,c = buffer[len(buffer)-1]
        side = []
        if r< maze.Row and maze.visited[r+1][c] == False:
            side.append(('N', r+1, c))
        if r > 1 and maze.visited[r-1][c] == False:
            side.append(('S', r-1, c))
        if c < maze.Column and maze.visited[r][c+1] == False:
            side.append(('E', r, c+1))
        if c>1 and maze.visited[r][c-1]== False:
            side.append(('W', r, c-1))

        if side:
            path, nr, nc = random.choice(side)
            if path == 'N': 
                maze.northWall[r][c] =0
            if path == 'E':
                maze.eastWall[r][c]=0
            if path == 'S':
                maze.northWall[r-1][c]=0
            if path == 'W':
                maze.eastWall[r][c-1]=0

            maze.visited[nr][nc] = True
            buffer.append((nr,nc))

        else:
            buffer.pop()

        screen.fill(white)
        maze.draw(screen)
        pygame.display.flip()
        pygame.time.delay(5)

def win(maze, screen, start, end):
    buffer = [start]
    visited = set([start])
    before = {start: None}

    while buffer:
        now = buffer[len(buffer)-1]
        if now == end:
            break
        r,c= now
        side = []
        if r< maze.Row:
            if maze.northWall[r][c] == 0:
                if(r+1, c) not in visited:
                    side.append((r+1,c))
        
        if r>1:
            if maze.northWall[r-1][c] == 0:
                if (r-1,c) not in visited:
                    side.append((r-1,c))

        if c< maze.Column:
            if maze.eastWall[r][c]==0:
                if(r, c+1) not in visited:
                    side.append((r,c+1))

        if c>1:
            if maze.eastWall[r][c-1]==0:
                if(r, c-1) not in visited:
                    side.append((r,c-1))

        if side:
            sideCell = random.choice(side)
            visited.add(sideCell)
            buffer.append(sideCell)
        else:
            drawing(screen, now, blue)
            buffer.pop()

        for i in range(len(buffer)):
            drawing(screen, buffer[i], red)
        pygame.display.flip()
        pygame.time.delay(40)
def drawing(screen, position, color):
    r,c = position
    x= (c-1) * Cell_length + Cell_length//2
    y= (maze.Row - r) * Cell_length + Cell_length//2
    pygame.draw.circle(screen,color,(x,y), Cell_length//4)

pygame.init()
screen = pygame.display.set_mode((Width, Height))
maze= Maze(Row, Column)
formMaze(maze, screen)
win(maze,screen, (1,1), (Row,Column))
pygame.quit()