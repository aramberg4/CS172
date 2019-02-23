#File Name:   text.py
#Purpose:     Text class that inherits from drawable.py.
#Author:      Austin Ramberg
#User id:     afr38
#Date:        February 22, 2019

import pygame
from drawable import Drawable

class Text(Drawable):
    def __init__(self, position, visible, msg, size, color = (0,0,0)):
        super().__init__(position, visible)
        self.__msg = msg
        self.__color = color
        self.__size = size

    # getters
    def getMsg(self):
        return self.__msg

    def getColor(self):
        return self.__color

    def getSize(self):
        return self.__size

    # setters
    def setMsg(self, m):
        self.__msg = m

    def setColor(self, c):
        self.__color = c

    def setSize(self, s):
        self.__size = s

    # override
    def draw(self, surface):
        if self.getVisible():
            pos = self.getPosition()
            font = pygame.font.SysFont(None, self.getSize())
            screenText = font.render(self.getMsg(), True, self.getColor())
            surface.blit(screenText,[pos[0], pos[1]])

    #override
    def get_rect(self):
        pos = self.getPosition()
        return pygame.Rect([pos[0], pos[1], self.getSideLength(), self.getSideLength()])

