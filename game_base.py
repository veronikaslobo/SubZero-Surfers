import pygame
import random
import player
from obstacle_definition import Obstacle, spawn_obstacle, obs_imgs, LANES


# initializing environment
pygame.init()

# CONSTANTS
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 50,50
PLAYER_WIDTH, PLAYER_HEIGHT = 50,50

# COLORS
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (189,228,255)
PURPLE =(207,169,245)
YELLOW =(254,234,160)

# background


# obstacles


# initialize environment
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


#running the game
running = True
while running:
    # clock and timer
    clock.tick(FPS)
    spawn_timer += 1

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill(BLUE)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()