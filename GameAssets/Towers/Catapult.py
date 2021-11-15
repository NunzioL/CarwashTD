import pygame
from GameAssets.Towers import Tower
import os
import math
from GameAssets.Menu.menu import TowerButton


menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "menu.png")).convert_alpha(), (120, 70))
upgrade_btn = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "upgrade.png")).convert_alpha(), (50, 50))


catapult_imgs1 = []

# load catapult image
"""for x in range(37,43):
    pygame.image.load(os.path.join("GameAssets", "Towers", "Catapult.png")).convert_alpha(),(90,90)))"""



class catapultTowerLong(Tower):
    def __init__(self, x,y):
        super().__init__(x, y)
        self.catapult_imgs = catapult_imgs1[:]
        self.catapult_count = 0
        self.range = 200
        self.original_range = self.range
        self.inRange = False
        self.left = True
        self.damage = 1
        self.original_damage = self.damage
        self.width = self.height = 90
        self.moving = False
        self.name = "catapult"

        # self.menu = TowerButton(self, self.x, self.y, menu_bg, [2000, 5000,"MAX"])
        self.menu.add_btn(upgrade_btn, "Upgrade")


    def draw(self, win):
        """
        draw the arhcer tower and animated catapult
        :param win: surface
        :return: int
        """
        super().draw_radius(win)
        super().draw(win)

        if self.inRange and not self.moving:
            self.catapult_count += 1
            if self.catapult_count >= len(self.catapult_imgs) * 10:
                self.catapult_count = 0
        else:
            self.catapult_count = 0

        catapult = self.catapult_imgs[self.catapult_count // 10]
        if self.left == True:
            add = -25
        else:
            add = -catapult.get_width() + 10
        win.blit(catapult, ((self.x + add), (self.y - catapult.get_height() - 25)))


    def attack(self, enemies):
        """
        attacks an enemy in the enemy list, modifies the list
        :param enemies: list of enemies
        :return: None
        """
        money = 0
        self.inRange = False
        enemy_closest = []
        for enemy in enemies:
            x = enemy.x
            y = enemy.y

            dis = math.sqrt((self.x - enemy.img.get_width()/2 - x)**2 + (self.y -enemy.img.get_height()/2 - y)**2)
            if dis < self.range:
                self.inRange = True
                enemy_closest.append(enemy)

        enemy_closest.sort(key=lambda x: x.path_pos)
        enemy_closest = enemy_closest[::-1]
        if len(enemy_closest) > 0:
            first_enemy = enemy_closest[0]
            if self.catapult_count == 50:
                if first_enemy.hit(self.damage) == True:
                    money = first_enemy.money * 2
                    enemies.remove(first_enemy)

            if first_enemy.x > self.x and not(self.left):
                self.left = True
                for x, img in enumerate(self.catapult_imgs):
                    self.catapult_imgs[x] = pygame.transform.flip(img, True, False)
            elif self.left and first_enemy.x < self.x:
                self.left = False
                for x, img in enumerate(self.catapult_imgs):
                    self.catapult_imgs[x] = pygame.transform.flip(img, True, False)

        return money


catapult_imgs = []

# load catapult images
for x in range(43,49):
    catapult_imgs.append(
        pygame.image.load(os.path.join("GameAssets", "Towers", "Catapult.png"))
    )