import pygame
import math
import os


class Enemy:

    def __init__(self):
        self.width = 64
        self.height = 64
        self.animation_count = 0
        self.dirt = 5
        self.velocity = 3
        self.path = [(5, 385), (129, 385), (129, 173), (291, 173), (291, 450), (505, 450), (505,312), (800,312)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.dis = 0
        self.path_pos = 0
        self.move_count = 0
        self.move_dis = 0
        self.flipped = False
        self.max_dirt = 5
        self.speed_increase = 1.2
        self.visible = True

    def draw(self, win):
        """
        Draws the enemy with the given image
        :param win: surface
        :return: none
        """

        if self.visible:
            self.img = self.images[self.animation_count]

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

    def collide(self, x, y):
        """
        Returns if position has hit enemy
        :param x: int
        :param y: int
        :return: bool
        """
        if self.x + self.width >= x >= self.x:
            if self.y + self.height >= y >= self.y:
                return True
        return False

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

        # if self.x == self.path[self.path_pos][7]:

    def wash(self, damage):
        """
        Returns true if a car is clean and removes one dirt
        each call
        :return: bool
        """
        self.dirt -= damage
        if self.dirt <= 0:
            return True
        return False

        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = None
        self.distance = 0
        self.path_position = 0
        self.move_count = 0
        self.move_distance = 0
        self.flipped = False
        self.max_dirt = 0
