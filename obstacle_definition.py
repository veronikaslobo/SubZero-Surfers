import pygame
import random

pygame.init()
# defining images
glacier_img = pygame.image.load("images/glacier1.png")

# obstacle images array
obs_imgs = [glacier_img]
LANES=[50,100,150]
game_speed= 5

class Obstacle:
    def __init__(self, image, x, y,speed):
        self.image = image
        self.rect = image.get_rect(topleft=(x,y))    # track image place by putting it on a rect object
        self.speed = speed #NEED TO DEFINE GAME SPEED
        self.active = True             # Whether the obstacle is active in the game

    def update(self): # moves down (with game speed)
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)  # maps image to rect position


def spawn_obstacle():
    image = random.choice(obs_imgs)
    x = random.choice(LANES) #NEED TO DEFINE X POSITIONS
    y = -image.get_height()
    obstacle = Obstacle(image, x, y, game_speed)
    return obstacle

