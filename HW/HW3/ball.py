#File Name:   ball.py
#Purpose:     Ball class that inherits from drawable.py.
#Author:      Austin Ramberg
#User id:     afr38
#Date:        February 22, 2019
import pygame
from drawable import Drawable

class Ball(Drawable):
    def __init__(self, position, visible, width = 0, radius =1, color = (0,0,0)):
        super().__init__(position, visible)
        self.__lineWidth = width
        self.__radius = radius
        self.__color = color

    # getters
    def getLineWidth(self):
        return self.__lineWidth

    def getRadius(self):
        return self.__radius

    def getColor(self):
        return self.__color

    # setters
    def setLineWidth(self, w):
        self.__lineWidth = w

    def setRadius(self, r):
        self.__height = r

    def setColor(self, c):
        self.__color = c

    # override
    def draw(self, surface):
        if self.getVisible():
            pygame.draw.circle(surface, self.getColor(), self.getPosition(), self.getRadius(), self.getLineWidth())

    #override
    def get_rect(self):
        pos = self.getPosition()
        return pygame.Rect([pos[0]-self.getRadius(), pos[1]+self.getRadius(), self.getRadius()*2, self.getRadius()*2])

