#File Name:   drawable.py
#Purpose:     Abstract base class for pygame drawable objects.
#Author:      Austin Ramberg
#User id:     afr38
#Date:        February 22, 2019
import pygame
import abc

class Drawable(metaclass = abc.ABCMeta):
	def __init__(self, position, visible):
		self.__position = position
		self.__visible = visible
	
	#getters
	def getPosition(self):
		return self.__position
		
	def getVisible(self):
		return self.__visible

	#setters
	def setPosition(self, newPos):
		self.__position = newPos
	
	def setVisible(self, v):
		self.__visible = v

	#abstract methods	
	@abc.abstractmethod
	def draw(self,surface):
		pass

	@abc.abstractmethod
	def get_rect(self):
		pass