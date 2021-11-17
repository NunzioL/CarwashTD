import pygame
import sys
import math


class Enemy():

    def __init__(self):
        self.catapult_count = 0
        self.dirty = True
        self.dirt = 5
        self.path = [(5, 385), (129, 385), (129, 173), (291, 173), (291, 450), (505, 450), (505,312), (800,312)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.path_pos = 0
        self.max_dirt = 5
        self.visible = True
       # catapult_count = 0

    def set(self):
        self.catapult_count += 1




    def draw(self, win):
        """
        Draws the enemy with the given image
        :param win: surface
        :return: none
        """

        if self.visible:
            if self.dirt < 3:
                self.img = self.images[0]
            elif self.dirt < 0:
                self.img = self.images[1]
            else:
                self.img = self.images[2]

            if self.x < self.path[self.path_pos][0]:
               self.img = pygame.transform.rotate(self.img, 0)
            elif self.x > self.path[self.path_pos][0]:
               self.img = pygame.transform.rotate(self.img, 180)
            if self.y < self.path[self.path_pos][1]:
               self.img = pygame.transform.rotate(self.img, -90)
            elif self.y > self.path[self.path_pos][1]:
               self.img = pygame.transform.rotate(self.img, 90)

            win.blit(self.img, (self.x - self.img.get_width() / 2, self.y - self.img.get_height() / 2))

            self.draw_health_bar(win)

            #self.wash(0)

            # pygame.draw.line(win, (1, 0, 0), (self.x, self.y), self.path[self.path_pos])

    def draw_health_bar(self, win):
        """
        draw health bar above enemy
        :param win: surface
        :return: None
        """
        length = 50
        move_by = round(length / self.max_dirt)
        health_bar = move_by * self.dirt

        pygame.draw.rect(win, (255, 0, 0), (self.x - 30, self.y - 75, length, 10), 0)
        pygame.draw.rect(win, (0, 255, 0), (self.x - 30, self.y - 75, health_bar, 10), 0)

    def move(self):
        """
        Move enemy
        :return: none
        """
        if self.visible:
            if self.x < self.path[self.path_pos][0]:
                self.x += 1
            elif self.x > self.path[self.path_pos][0]:
                self.x -= 1
            if self.y < self.path[self.path_pos][1]:
                self.y += 1
            elif self.y > self.path[self.path_pos][1]:
                self.y -= 1
            if self.x == self.path[self.path_pos][0] and self.y == self.path[self.path_pos][1]:
                self.path_pos += 1
                if self.path_pos >= len(self.path):
                    self.visible = False

    def wash(self):
        """
        Returns if a car is visible and removes one dirt if it takes damage
        each call
        :return: bool
        """
        if self.catapult_count >= 1:
            self.dirt -= self.catapult_count

        if self.dirt > 0:
            self.visible = True
        else:
            self.visible = False



