import pygame
import os
from .enemy import Enemy


class Mustang(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "mustang"
        self.money = 2
        self.max_health = 2
        self.health = self.max_health
        self.images = pygame.image.load(os.path.join("GameAssets", "cars", "ford_mustang.png"))
        self.images = [pygame.transform.scale(self.images, (110, 64))]
