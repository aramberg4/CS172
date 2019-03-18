#File Name:   node.py
#Purpose:     File contains Node class.
#Authors:     Austin Ramberg, Adelaida A. Medlock
#User id: 	  afr38
#Date:        March 6, 2019
#Note:        The following code was adapted from LinkListDemo.py 
#             by Adelaida A. Medlock. I do not claim sole authorship.

class Node():
    def __init__(self, emp, next = None):
        self.__employee = emp
        self.__next = next
    
    # getters
    def getEmployee(self):
        return self.__employee
    
    def getNext(self):
        return self.__next
    
    #setters
    def setEmployee(self,emp):
        self.__employee = emp

    def setNext(self,n):
        self.__next = n

    #overloaded operators
    def __str__(self):
        return str(self.__employee) + " whose next node is " + str(self.__next)