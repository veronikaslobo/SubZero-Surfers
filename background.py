import pygame 
import math

pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
scroll = 0
targetsize = (SCREEN_WIDTH, SCREEN_HEIGHT)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game name")

blabala = pygame.image.load("images/background.png").convert()
bg = pygame.transform.scale(blabala, targetsize)
bg_width = bg.get_width()
bg_height = bg.get_height()

tiles = math.ceil(SCREEN_HEIGHT / bg_width) + 1

def scroll_bg():
    targetsize = (SCREEN_WIDTH, SCREEN_HEIGHT)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Game name")

    blabala = pygame.image.load("images/background.png").convert()
    bg = pygame.transform.scale(blabala, targetsize)
    bg_width = bg.get_width()
    bg_height = bg.get_height()

    tiles = math.ceil(SCREEN_HEIGHT / bg_width) + 1

    scroll = (scroll + 5) % bg_height

    screen.blit(bg, (0, scroll - bg_height))
    screen.blit(bg, (0, scroll))

    pygame.display.update()
