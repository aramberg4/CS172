#File Name:  cat.py
#Purpose:    The Cat class represents a cat, which is a kind of mammal
#Author:     Adelaida A. Medlock
#Date:       January 28, 2019

from mammals import Mammal

class Cat(Mammal):
    
    def __init__(self, age = 0, hair = 'short'):
        super().__init__('cat', age)
        self.__hair = hair   #additional attribute represents long or short hair
    
    def getHair(self):
        return self.__hair
    
    # no setter is needed. why?
 
    # additional behavior
    def catchMouse(self) :
        print('Here goes the hunter! Good kitty!')
    
    # override makeSound
    def makeSound(self):
        print('Meow')
        
    # override __repr__
    def __repr__(self):
        myStr = super().__repr__() +  ', ' + self.__hair + ' hair.'
        return myStr
    
