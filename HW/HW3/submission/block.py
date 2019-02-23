#File Name:   block.py
#Purpose:     Block class that inherits from drawable.py.
#Author:      Austin Ramberg
#User id:     afr38
#Date:        February 22, 2019

import pygame
from drawable import Drawable

class Block(Drawable):
    def __init__(self, position, visible, sideLength, color = (0,0,0), lineWidth = 0):
        super().__init__(position, visible)
        self.__lineWidth = lineWidth
        self.__color = color
        self.__sideLength = sideLength

    # getters
    def getLineWidth(self):
        return self.__lineWidth

    def getColor(self):
        return self.__color

    def getSideLength(self):
        return self.__sideLength

    # setters
    def setLineWidth(self, lw):
        self.__lineWidth = lw

    def setColor(self, c):
        self.__color = c

    def setSideLength(self, s):
        self.__sideLength = s

    # override
    def draw(self, surface):
        if self.getVisible():
            pygame.draw.rect(surface, self.getColor(), self.get_rect(), self.getLineWidth())

    #override
    def get_rect(self):
        pos = self.getPosition()
        return pygame.Rect([pos[0], pos[1], self.getSideLength(), self.getSideLength()])

