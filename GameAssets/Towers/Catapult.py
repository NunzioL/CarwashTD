import pygame
import sys
import math
from GameAssets.Menu.menu import TowerButton
#from GameAssets.Projectiles.waterBalloon import waterBalloon


class Catapult(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.angle = None
        self.image = pygame.image.load('GameAssets/Towers/Catapult.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.damage = 1

    def shoot_angle(self):
        from math import atan2, degrees, pi
        dx = self.x - self.rect.center[0]
        dy = self.y - self.rect.center[1]
        rads = atan2(-dy, dx)
        rads %= 2 * pi
        degs = degrees(rads)
        print(degs)

    def reload_img(self):
        x, y = self.rect.center
        self.image = pygame.image.load('GameAssets/Towers/Catapult.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def shoot(self):
        cooldown = pygame.time.Clock()
        cooldown.tick(2000)
        for bloon in waterBalloon:
            bloon.draw(self.win)


