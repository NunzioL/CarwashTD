import pygame
import os
from GameAssets.cars.tesla import Tesla


class Game:
    def __init__(self):
        self.width = 1000
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = [Tesla()]
        self.towers = []
        self.lives = 10
        self.money = 100
        # load the background image
        self.background = pygame.image.load(os.path.join("GameAssets", "map.jpg"))
        self.background = pygame.transform.scale(self.background, (800, self.height))
        self.clicks = []  # remove this

    def runGame(self):
        runGame = True
        clock = pygame.time.Clock()
        while runGame:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runGame = False

                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN :
                    self.clicks.append(pos)
                    print(pos)

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

        pygame.quit()

    def draw(self):
        self.win.fill((0, 0, 0))
        self.win.blit(self.background, (0, 0))

        # draw enemies
        for en in self.enemies:
            en.draw(self.win)

        pygame.display.update()


g = Game()
g.runGame()
