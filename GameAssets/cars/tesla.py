import pygame
import sys
from .enemy import Enemy


class Tesla(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "tesla"
        self.money = 50
        self.max_health = 1
        self.health = self.max_health
        self.image = pygame.image.load('GameAssets/cars/tesla_model3.png')
        self.image = pygame.transform.scale(self.image, (110, 64))
        self.image_clean = pygame.image.load('GameAssets/cars/tesla_model3_clean.png')
        self.image_clean = pygame.transform.scale(self.image_clean, (110, 64))
        self.image_dirty = pygame.image.load('GameAssets/cars/tesla_model3_dirty.png')
        self.image_dirty = pygame.transform.scale(self.image_dirty, (110, 64))
     #  self.images = [self.image]
        self.images = [self.image_dirty, self.image_clean, self.image]
