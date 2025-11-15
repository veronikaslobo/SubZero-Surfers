import pygame
from player import Player

class Obstacle:
    def __init__(self, image, x, y,speed):
        self.image = image
        self.rect = image.get_rect(topleft=(x,y))    # track image place by putting it on a rect object
        self.speed = speed
        self.active = True             # Whether the obstacle is active in the game


def check_for_collision(player, obstacle):
