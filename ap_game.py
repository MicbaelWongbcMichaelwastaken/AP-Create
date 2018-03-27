import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 800))
player_sprite = pygame.image.load('shipsprite.png')
clock=pygame.time.Clock()
done = False

#class Background:
    #screen = pygame.image.load('spacebackground.png').convert()

class Player:
    screen.blit((player_sprite),(400,600))
    def moveRight(self, pixels):
        self.rect.x += pixels

Player = pygame.sprite.Group()


while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            Player.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            Player.moveRight(5)


        clock.tick(60)

        pygame.display.update()


