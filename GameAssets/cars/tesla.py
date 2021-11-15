import pygame
import os
from .enemy import Enemy


class Tesla(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "tesla"
        self.money = 1
        self.max_health = 1
        self.health = self.max_health
        self.images = pygame.image.load(os.path.join("GameAssets", "cars", "tesla_model3.png"))
        self.images = [pygame.transform.scale(self.images, (110, 64))]
