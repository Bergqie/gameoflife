#Author: Matthew Bergquist
#Date: 01/13/2024
#Description: This program is a simulation of Conway's Game of Life. The rules are as follows:
#1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
#2. Any live cell with two or three live neighbors lives on to the next generation.
#3. Any live cell with more than three live neighbors dies, as if by overpopulation.
#4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The graph is initalized with random values and then updated based on the rules above. The graph is drawn using pygame.


import pygame
import numpy as np
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600 # Width and height of the screen
CELL_SIZE = 10 # Size of each cell
GRID_WIDTH, GRID_HEIGHT = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE # Width and height of the grid
WHITE, BLACK = (255, 255, 255), (0, 0, 0) # Colors
FPS = 10 # Frames per second

# Initialize the grid with random values
def initialize_grid():
    return np.random.choice([0, 1], size=(GRID_WIDTH, GRID_HEIGHT)) # 0 = dead, 1 = alive

# Function to update the grid based on the Game of Life rules
def update_grid(grid):
    new_grid = grid.copy() # Copy the grid to avoid changing the original grid

    for i in range(1, GRID_WIDTH - 1): # Ignore the edges of the grid
        for j in range(1, GRID_HEIGHT - 1): # Ignore the edges of the grid
            neighbors = grid[i - 1:i + 2, j - 1:j + 2].sum() - grid[i, j] # Sum the number of neighbors
            if grid[i, j] == 1 and (neighbors < 2 or neighbors > 3): # If the cell is alive and has less than 2 or more than 3 neighbors, it dies
                new_grid[i, j] = 0 # Dead
            elif grid[i, j] == 0 and neighbors == 3: # If the cell is dead and has exactly 3 neighbors, it becomes alive
                new_grid[i, j] = 1 # Alive

    return new_grid # Return the new grid

# Function to draw the grid
def draw_grid(screen, grid):
    screen.fill(WHITE) # Fill the screen with white
    for i in range(GRID_WIDTH): # Loop through the grid
        for j in range(GRID_HEIGHT): # Loop through the grid
            if grid[i, j] == 1: # If the cell is alive, draw a black rectangle
                pygame.draw.rect(screen, BLACK, (i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE)) # Draw a rectangle

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Set the screen size
    pygame.display.set_caption("Conway's Game of Life") # Set the caption

    clock = pygame.time.Clock() # Create a clock object
 
    grid = initialize_grid() # Initialize the grid

    running = True # Boolean to keep track of whether the program is running or not
    while running: # Main loop
        for event in pygame.event.get(): # Loop through the events
            if event.type == pygame.QUIT: # If the user clicks the X button, quit the program
                running = False # Set running to False
                sys.exit() # Exit the program

        grid = update_grid(grid) # Update the grid

        draw_grid(screen, grid) # Draw the grid
        pygame.display.flip() # Update the display

        clock.tick(FPS) # Tick the clock

    pygame.quit() # Quit pygame

if __name__ == "__main__":
    main() # Call the main function
