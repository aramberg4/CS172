#File Name:   testPoint.py
#Purpose:     Test the point class
#Author:      Adelaida Medlock
#Date:        January 14, 2019

from point import Point

def main():
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