import pygame
import os
import sys

class TowerButton:
    def __init__(self):
        self.catapult = pygame.image.load(os.path.join("GameAssets", "Towers", "Catapult.png"))
        self.catapult = pygame.transform.scale(self.catapult, (100, 100))
        self.x = 800
        self.y = 100
        self.rect = self.catapult.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.clicked = False

    # draw function
    def draw(self, win):
        win.blit(self.catapult, (self.x, self.y))

    # function for when you click on a button
    def click(self):
        pos = pygame.mouse.get_pos()
        # if clicked is false
        # and mouse is clicked within the rectangle containing the catapult image
        # set clicked equal to true
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                print('CLICKED')
        # if clicked is true
        # and mouse is clicked outside the rectangle containing the catapult image
        # set clicked equal to false
        if not self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == True:
                self.clicked = False
                print('UNCLICKED')

#clicked back to false if elsewhere is clicked

#if button is clicked and