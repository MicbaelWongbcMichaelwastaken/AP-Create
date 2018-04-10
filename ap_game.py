import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock=pygame.time.Clock()
done = False


RED = (255, 0, 0)

#class Background:
    #screen = pygame.image.load('spacebackground.png').convert()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
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
    def fire(self):
        laser = Lasers(self, self)
        AllSprites.add(laser)
        lasers.add(laser)



class Lasers(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


Player = Player()
lasers = pygame.sprite.Group()
AllSprites = pygame.sprite.Group()
#AllSprites.add(Player)



while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        Player.fire()

        AllSprites.update()
        #hit = pygame.sprite.spritecollide(Player, False)
        #if hit:
            #running = False
        screen.fill((0, 0, 0))
        Player.player_keys()
        clock.tick(60)
        AllSprites.draw(screen)
        pygame.display.update()