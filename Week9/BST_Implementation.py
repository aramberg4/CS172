#Program:     BST_Implementation.py
#Purpose:     Basic implementation of a Binary Searth Tree (BST)
#Author:      Adelaida Medlock
#Date:        March 4, 2019

# Node class -- this is the basic element of a BST
class Node():
    def __init__(self, value):
        self.__value = value
        self.__right = None
        self.__left = None

    def setLeft(self, l):
        self.__left = l
            
    def setRight(self, r):
        self.__right = r
    
    def getLeft(self):
        return self.__left
    
    def getRight(self):
        return self.__right
    
    def getValue(self):
        return self.__value


# BST class - basic implementation of a Binary Search Tree
class BST():
    def __init__(self):
        self.__root = None
    
    
    def insert(self, value):
        # create new node with value
        node = Node(value)
        
        # if BST is empty, the new node is the root
        if self.__root == None:
            self.__root = node
            return
        
        # if BST is not empty, find the proper place for the new node
        current = self.__root
        while True:
            # new node is going to be on the left of current node
            if value <= current.getValue():
                if current.getLeft() == None:  # we have a leaf, insert new node
                    current.setLeft(node)
                    return
                else:
                    current = current.getLeft()
             
             # new node is going to be on the right of current node
            else:
                if current.getRight() == None: # we have a leaf, insert new node
                    current.setRight(node)
                    return
                else:
                    current = current.getRight()


    def search(self, value):
        # empty BST - the value is not there
        if self.__root == None:
            return "Value not found"
        
        # BST is not empty. Traverse and see if value is there
        current = self.__root
        while current != None:  # keep going as long as we haven't reached the last node
            if current.getValue() == value:
                return "Found!"
            elif value < current.getValue():  # search to the left
                current = current.getLeft()
            else:
                current = current.getRight()  # search to the right


# Testing BST implementation
if __name__ == "__main__":
    values = [2, 3, 4, 1, 5, 2]
    
    tree = BST() #empty new BST
    
    # insert values in the list into the4 BST, one at the time
    for value in values:
        print('Inserting: ', value)
        tree.insert(value)
    print()
    
    # searching for a value in the BST
    value = int(input('Enter value to search: '))
    print(tree.search(value))
   
        
        
        
