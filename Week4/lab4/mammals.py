#File Name:  mammals.py
#Purpose:    The Mammal class represents a generic mammal
#Author:     Adelaida A. Medlock
#Date:       January 28, 2019

class Mammal:
    def __init__(self, species = '', age = 0):
        self.__species = species
        self.__age = age

    # getters
    def getSpecies():
        return self.__species
    
    def getAge():
        return self.__age
    
    # setters
    def setSpecies(self, species):
        self.__species = species
    
    def haveBirthday(self):
        self.__age = self.__age + 1   

    # The make_sound method is the mammal's way of making a generic sound
    def makeSound(self):
        print('Grrrrr')
       
    # overloading the print operator
    def __repr__(self):
        myStr = 'A ' + str(self.__age) + '-year old ' + self.__species
        return myStr


