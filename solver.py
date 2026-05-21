# solver.py
import random
import pygame
from config import red, blue

def win(maze, screen, start, end, draw_cell_callback):
    buffer = [start]
    visited = set([start])

    while buffer:
        now = buffer[-1]
        if now == end:
            break
        r, c = now
        side = []
        if r < maze.Row and maze.northWall[r][c] == 0 and (r + 1, c) not in visited:
            side.append((r + 1, c))
        if r > 1 and maze.northWall[r - 1][c] == 0 and (r - 1, c) not in visited:
            side.append((r - 1, c))
        if c < maze.Column and maze.eastWall[r][c] == 0 and (r, c + 1) not in visited:
            side.append((r, c + 1))
        if c > 1 and maze.eastWall[r][c - 1] == 0 and (r, c - 1) not in visited:
            side.append((r, c - 1))

        if side:
            sideCell = random.choice(side)
            visited.add(sideCell)
            buffer.append(sideCell)
        else:
            draw_cell_callback(maze, screen, now, blue)
            buffer.pop()

        for cell in buffer:
            draw_cell_callback(maze, screen, cell, red)
            
        pygame.display.flip()
        pygame.time.delay(40)