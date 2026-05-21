# main.py
import pygame
from config import Width, Height, Row, Column
from maze import Maze
from generator import formMaze
from solver import win
from renderer import draw_maze, drawing_cell

def main():
    pygame.init()
    screen = pygame.display.set_mode((Width, Height))
    pygame.display.set_caption("Team Maze Game")
    
    # Initialize structural grid
    maze = Maze(Row, Column)
    
    # Build the maze visually
    formMaze(maze, screen, draw_maze)
    
    # Solve the maze visually 
    win(maze, screen, (1, 1), (Row, Column), drawing_cell)
    
    # Let users review the completed maze before window shuts down
    running = True
    while running:
        for event in pygame.get_loop() if hasattr(pygame, 'get_loop') else pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
    pygame.quit()

if __name__ == "__main__":
    main()