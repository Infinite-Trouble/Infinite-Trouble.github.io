
import random
import pygame
import sys
import time  # Import the time module

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 900, 900
ROWS, COLS = 50, 50
CELL_SIZE = WIDTH // COLS
MOVEMENT_DELAY = 0.01  # Adjust the delay time as needed

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialize the maze grid, player position, and goal position
maze = [[0] * COLS for _ in range(ROWS)]
player_pos = [1, 1]
goal_pos = [ROWS - 2, COLS - 2]

# Initialize Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")

# Function to draw the maze, player, and goal
def draw_game():
    screen.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            if maze[row][col] == 1:
                pygame.draw.rect(screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, (player_pos[1] * CELL_SIZE, player_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, GREEN, (goal_pos[1] * CELL_SIZE, goal_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.flip()

# Recursive Backtracking algorithm with more randomness
def recursive_backtracking(row, col):
    directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
    random.shuffle(directions)

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc

        if 0 <= new_row < ROWS and 0 <= new_col < COLS and maze[new_row][new_col] == 0:
            maze[row + dr // 2][col + dc // 2] = 1  # Carve a path
            maze[new_row][new_col] = 1
            recursive_backtracking(new_row, new_col)

# Run the maze generation algorithm
recursive_backtracking(0, 0)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and player_pos[0] > 0 and maze[player_pos[0] - 1][player_pos[1]] == 1:
        player_pos[0] -= 1
        time.sleep(MOVEMENT_DELAY)  # Introduce delay here
    elif keys[pygame.K_DOWN] and player_pos[0] < ROWS - 1 and maze[player_pos[0] + 1][player_pos[1]] == 1:
        player_pos[0] += 1
        time.sleep(MOVEMENT_DELAY)  # Introduce delay here
    elif keys[pygame.K_LEFT] and player_pos[1] > 0 and maze[player_pos[0]][player_pos[1] - 1] == 1:
        player_pos[1] -= 1
        time.sleep(MOVEMENT_DELAY)  # Introduce delay here
    elif keys[pygame.K_RIGHT] and player_pos[1] < COLS - 1 and maze[player_pos[0]][player_pos[1] + 1] == 1:
        player_pos[1] += 1
        time.sleep(MOVEMENT_DELAY)  # Introduce delay here

    # Check if the player reached the goal
    if player_pos == goal_pos:
        print("Congratulations! You reached the goal!")
        pygame.quit()
        sys.exit()

    # Draw the game
    draw_game()
