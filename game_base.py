import pygame
import random

# intializing environment
pygame.init()

# CONSTANTS
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 50,50
PLAYER_WIDTH, PLAYER_HEIGHT = 50,50
OBSTACLE_SPEED = 5

# COLORS
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (189,228,255)
PURPLE =(207,169,245)
YELLOW =(254,234,160)

# game variables


# obstacle

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.draw.circle(screen,(PURPLE), (250, 250), 75))

pygame.display.flip()