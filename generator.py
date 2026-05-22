# generator.py
import random
import pygame
from config import white

def formMaze(maze, screen, draw_callback):
    buffer = [(1, 1)]
    maze.visited[1][1] = True
 
    while buffer:
        r, c = buffer[len(buffer) - 1]
        side = []
        if r < maze.Row and not maze.visited[r + 1][c]:
            side.append(('N', r + 1, c))
        if r > 1 and not maze.visited[r - 1][c]:
            side.append(('S', r - 1, c))
        if c < maze.Column and not maze.visited[r][c + 1]:
            side.append(('E', r, c + 1))
        if c > 1 and not maze.visited[r][c - 1]:
            side.append(('W', r, c - 1))

        if side:
            path, nr, nc = random.choice(side)
            if path == 'N': 
                maze.northWall[r][c] = 0
            if path == 'E':
                maze.eastWall[r][c] = 0
            if path == 'S':
                maze.northWall[r - 1][c] = 0
            if path == 'W':
                maze.eastWall[r][c - 1] = 0

            maze.visited[nr][nc] = True
            buffer.append((nr, nc))
        else:
            buffer.pop()

        screen.fill(white)
        draw_callback(maze, screen)
        pygame.display.flip()
        pygame.time.delay(5)