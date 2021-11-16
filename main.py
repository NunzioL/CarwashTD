import pygame
import math
from GameAssets.cars.tesla import Tesla
from GameAssets.Menu.menu import TowerButton
from GameAssets.Towers.Catapult import Catapult
from GameAssets.cars.enemy import Enemy

class Game:
    def __init__(self):
        self.width = 1000
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = [Tesla()]
        self.buttons = [TowerButton()]
        self.towers = []
        self.lives = 3
        self.money = 1000
        # load the background image
        self.background = pygame.image.load('GameAssets/map.jpg')
        self.background = pygame.transform.scale(self.background, (800, self.height))
        self.clicks = []  # remove
        self.catapults = pygame.sprite.Group()
        self.catapult_cost = 50
        self.FPS = 30
        self.num_catapults = 0

        # Score
        pygame.font.init()
        self.font = pygame.font.SysFont('freesansbold.ttf', 32)

        self.textX = 10
        self.testY = 10

    def show_money(self, x, y):
        money_value = self.font.render("Money : " + str(self.money), True, (255, 255, 255))
        self.win.blit(money_value, (x, y))

    def show_lives(self, x, y):
        lives_value = self.font.render("Lives : " + str(self.lives), True, (255, 255, 255))
        self.win.blit(lives_value, (x, y))

    def show_price(self, x, y):
        price_value = self.font.render("Price : " + str(self.catapult_cost), True, (255, 255, 255))
        self.win.blit(price_value, (x, y))

    def end_game(self, x, y):
        quit = self.font.render("GAME OVER", True, (255, 255, 255))
        self.win.blit(quit, (x, y))

    def shoot_angle(self, catapult, enemy):
        from math import atan2, degrees, pi
        dx = enemy.x - catapult.rect.center[0]
        dy = enemy.y - catapult.rect.center[1]
        rads = atan2(-dy, dx)
        rads %= 2 * pi
        degs = degrees(rads) + 90
        catapult.reload_img()
        catapult.angle = degs
        catapult.image = pygame.transform.rotate(catapult.image, degs)

    # game loop
    def runGame(self):
        global num_catapults
        runGame = True
        clock = pygame.time.Clock()
        while runGame:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runGame = False

                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicks.append(pos)
                   # print(pos)
                    pixel_color = self.win.get_at(pos)
                   # print(self.win.get_at(pos))

                    # towers can only be placed on green surface
                    #if 80 < pixel_color[0] > 100 and 105 < pixel_color[1] > 120 and 15 < pixel_color[2] > 30 and self.money >= self.catapult_cost:
                    if self.money >= self.catapult_cost:
                        # place tower using the coordinates
                        new_catapult = Catapult(pos[0], pos[1])
                        self.catapults.add(new_catapult)
                        self.money -= self.catapult_cost

            # listen for button
            for but in self.buttons:
                but.click()

            # loop through enemies
            to_del = []
            for en in self.enemies:
                en.move()
                if en.x < -5:
                    to_del.append(en)

            # delete all enemies off the screen
            for d in to_del:
                self.enemies.remove(d)

            self.draw()

            #if player is out of lives display game over and exit loop
            if self.lives == 0:
                self.end_game(400, 350)

        pygame.quit()

    def draw(self):
        self.win.fill((0, 0, 0))
        self.win.blit(self.background, (0, 0))


        # draw button
        for but in self.buttons:
            but.draw(self.win)

        # draw enemies
        for en in self.enemies:
            en.draw(self.win)

        if len(self.catapults) >= 1 and len(self.enemies) >= 1:
            for catapult in self.catapults:
                closest_en = None
                closest_dist = None
                for en in self.enemies:
                    dist = math.sqrt(((catapult.rect.center[0] - en.x) ** 2) + ((catapult.rect.center[0] - en.x) ** 2))
                    if closest_dist is None or closest_dist > dist:
                        closest_dist = dist
                        closest_en = en
                self.shoot_angle(catapult, closest_en)


        # draw towers
        self.catapults.draw(self.win)

        self.show_money(10, 10)
        self.show_lives(700, 10)
        self.show_price(810, 80)

        pygame.display.update()





g = Game()
g.runGame()
