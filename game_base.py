import pygame
import random
import player
import threading
import sys
import math
from button import Button
from obstacle_definition import Obstacle, spawn_obstacle, obs_imgs, LANES

pygame.init()
clock = pygame.time.Clock()

# CONSTANTS
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 50, 50
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
GAME_SPEED = 5

# COLORS
WHITE  = (255, 255, 255)
BLACK  = (0, 0, 0)
BLUE   = (189, 228, 255)
PURPLE = (207, 169, 245)
YELLOW = (254, 234, 160)

# initialize environment
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game name")

# menu background
menu_bg = pygame.image.load("images/babyblue.png")

# game background (scrolling)
BG_IMAGE = pygame.image.load("images/background.png").convert()
BG_IMAGE = pygame.transform.scale(BG_IMAGE, (SCREEN_WIDTH, SCREEN_HEIGHT))
BG_HEIGHT = BG_IMAGE.get_height()

scroll = 0  # vertical offset

# initialize environment
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def scroll_bg():
    global scroll

    scroll = (scroll + 5) % BG_HEIGHT

    # draw two copies to create continuous vertical scroll
    screen.blit(BG_IMAGE, (0, scroll - BG_HEIGHT))
    screen.blit(BG_IMAGE, (0, scroll))

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("images/font.ttf", size)

def play():
    spawn_timer = 0
    obstacles = []
    running = True

    while running:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        clock.tick(FPS)

        # handle events first
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # draw background
        scroll_bg()

        # generate obstacles
        spawn_timer += 1
        if spawn_timer > 100:
            obstacles.append(spawn_obstacle())
            spawn_timer = 0

        # draw obstacles
        for obs in obstacles:
            obs.update()
            obs.draw(screen)

        obstacles = [obs for obs in obstacles if obs.rect.top <= SCREEN_HEIGHT]

        pygame.display.flip()

def menu():
    while True:
        screen.blit(menu_bg, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=pygame.image.load(r"images/Play Rect.png"), x_pos=640, y_pos=250, text_input="PLAY")
        QUIT_BUTTON = Button(image=pygame.image.load(r"images/Quit Rect.png"), x_pos=640, y_pos=550, text_input="QUIT")

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

#running the game
menu()

pygame.quit()