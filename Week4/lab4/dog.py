#File Name:  dog.py
#Purpose:    The Dog class represents a dog, which is a kind of mammal
#Author:     Adelaida A. Medlock
#Date:       January 28, 2019

from mammals import Mammal

class Dog(Mammal):
    
    def __init__(self, age = 0, breed = ''):
        super().__init__('dog', age)
        self.__breed = breed   #additional attribute
    
    def getBreed(self):
        return self.__breed
    
    def setBreed(self, breed):
        self.breed = breed
 
    # additional behavior
    def playCatch(self) :
        print('Running and catching the stick. Good doggie!')
    
    # override makeSound
    def makeSound(self):
        print('Woof! Woof!')
        
    # override __repr__
    def __repr__(self):
        myStr = super().__repr__() +  ', ' + self.__breed
        return myStr
    
