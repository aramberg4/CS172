#File:     englishLength.py
#Purpose:  Class to represent and English Length given in inches, feet, yards
#Date:     January 23, 2019
#Author:   Adelaida Medlock

class EL:
    # initialization method
    def __init__(self, inches = 0, feet = 0, yards = 0):
        self.__inches = inches % 12
        self.__feet = feet + inches // 12
        self.__yards = yards + self.__feet // 3
        self.__feet = self.__feet % 3
    
    # getters
    def getInches(self):
        return self.__inches

    def getFeet(self):
        return self.__feet

    def getYards(self):
        return self.__yards
    
    def totalInches(self):
        allInches = self.__yards * 36 + self.__feet * 12 + self.__inches
        return allInches
    
    #setters
    def addInches(self, amountToAdd):
        totalInches = self.totalInches() + amountToAdd
        temp = EL(totalInches)
        self.__inches = temp.getInches()
        self.__feet = temp.getFeet()
        self.__yards = temp.getYards()

    # overloading the arithmetic operators
    def __add__(self, other):
        newInches = self.__inches + other.__inches
        newFeet = self.__feet + other.__feet
        newYards = self.__yards + other.__yards
        return EL(newInches, newFeet, newYards)
    
    # overloading comparison operators
    def __lt__(self, other):
        return (self.totalInches() < other.totalInches())
    
    def __eq__(self, other):
        return (self.totalInches() == other.totalInches())

    # overloading the print operator
    def __str__(self):
        mystr = 'An English Length object that is '
        
        if self.__inches == 1:
            mystr += '1 inch, '
        else:
            mystr += str(self.__inches) + ' inches, '
        
        if self.__feet == 1:
            mystr += '1 foot, '            
        else:
            mystr += str(self.__feet) +' feet, and '
            
        if self.__yards == 1:
            mystr += '1 yard long.'
        else:
            mystr += str(self.__yards) + ' yards long'
	
        return mystr
    
    # overloading the subscript operator
    def __getitem__(self,loc):
        if loc == 0:
            return self.__inches
        elif loc == 1:
            return self.__feet
        elif loc == 2:
            return self.__yards
        else:
            raise Exception('Invalid index')