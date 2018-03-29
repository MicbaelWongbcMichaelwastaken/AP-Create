import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock=pygame.time.Clock()
done = False


#class Background:
    #screen = pygame.image.load('spacebackground.png').convert()

class Player():
    def __init__(self):
        self.image = pygame.image.load('shipsprite.png')
        self.x = 400
        self.y = 600
    def player_keys(self):
        key = pygame.key.get_pressed()
        dist = 5
        if key[pygame.K_RIGHT]:  # right key
            self.x += dist  # move right
        elif key[pygame.K_LEFT]:  # left key
            self.x -= dist  # move left
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

class Lasers():
    def __init__(self):
        self.image = pygame.image.load('beam.png')
        self.x = Player()
        sef.y = Player()





Player = Player()


while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        screen.fill((0, 0, 0))
        Player.draw(screen)
        Player.player_keys()
        clock.tick(60)

        pygame.display.update()


