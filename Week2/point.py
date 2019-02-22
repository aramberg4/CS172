##File Name:  point.py
#Purpose:     Class to represent a point located at coordinatex x, y
#Author:      Adelaida Medlock
#Date:        January 14, 2019

import math

class Point:
    '''
    def __init__ (self):   #default values for x and y = 0
        self.__x = 0
        self.__y = 0
    
    def __init__ (self, x, y): #values for x and y must be provided
        self.__x = x
        self.__y = y
    '''
    # static attribute
    __count = 0  # to count how many points we have created so far
    
    # initialization method 
    def __init__ (self, x = 0, y = 0): #default arguments technique
        self.__x = x
        self.__y = y
        Point.__count += 1  #updating the Point count
    
    # getters
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def print(self):
        return '(' + str(self.__x) + ', ' + str(self.__y) + ')'
    
    # setters
    def setPoint(self, x, y):
        self.__x = x
        self.__y = y
    
    def reset(self):
        self.setPoint(0, 0)
        
    # other methods
    def distance(self, p):
        return math.sqrt( (self.getX() - p.getX()) ** 2 + (self.getY() - p.getY()) ** 2)
    
    # static method
    @staticmethod
    def printPointCount():
        return Point.__count


#the following code will excecute only if this file is not being used as a module
if __name__ == "__main__" :
    # create some point objects
    p1 = Point()
    p2 = Point(10, 10)
    p3 = Point(5, 20)
    
    # print the points
    print('We have created', Point.printPointCount(), 'points:')
    print('p1 =', p1.print())
    print('p2 =', p2.print())
    print('p3 =', p3.print())
    
    # calculatet the distance between p1 and p2
    dist = p1.distance(p2)
    print('The distance between p1 and p2 is', dist)

        
