import pygame
import os
from .enemy import Enemy

images = []
for x in range(20):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    images.append(pygame.transform.scale(
        pygame.image.load(os.path.join("GameAssets", "cars", "tesla_model3.png")),
        (64, 64)))


class Tesla(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "tesla"
        self.money = 1
        self.max_health = 1
        self.health = self.max_health
        self.images = pygame.image.load(os.path.join("GameAssets", "cars", "tesla_model3.png"))
        self.images = [pygame.transform.scale(self.images, (110, 64))]
