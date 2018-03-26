import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 800))
player_sprite = pygame.image.load('shipsprite.png')
done = False

#class Background:
    #screen = pygame.image.load('spacebackground.png').convert()

class Player:
    screen.blit((player_sprite),(20,20))

Player = pygame.sprite.Group()


while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        pygame.display.update()


