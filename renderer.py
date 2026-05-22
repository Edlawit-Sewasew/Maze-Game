# renderer.py
import pygame
from config impot black, Cell_length

def draw_maze(maze, screen):
    for r in range(1, maze.Row + 1):
        for c in range(1, maze.Column + 1):
            x = (c - 1) * Cell_length
            y = (maze.Row - r) * Cell_length
            
            # draw north wall
            if maze.northWall[r][c]:
                pygame.draw.line(screen, black, (x, y), (x + Cell_length, y))
            # draw east wall
            if maze.eastWall[r][c]:
                pygame.draw.line(screen, black, (x + Cell_length, y), (x + Cell_length, y + Cell_length))
            # draw south wall
            if maze.northWall[r - 1][c]:
                pygame.draw.line(screen, black, (x, y + Cell_length), (x + Cell_length, y + Cell_length))
            # draw west wall
            if maze.eastWall[r][c - 1]:
                pygame.draw.line(screen, black, (x, y), (x, y + Cell_length))

def drawing_cell(maze, screen, position, color):
    r, c = position
    x = (c - 1) * Cell_length + Cell_length // 2
    y = (maze.Row - r) * Cell_length + Cell_length // 2
    pygame.draw.circle(screen, color, (x, y), Cell_length // 4)
