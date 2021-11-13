import pygame
import os
from .enemy import Enemy


class Frontier(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "frontier"
        self.money = 3
        self.max_health = 3
        self.health = self.max_health
        self.images = pygame.image.load(os.path.join("GameAssets", "cars", "nissan_frontier.png"))
        self.images = [pygame.transform.scale(self.images, (110, 64))]
