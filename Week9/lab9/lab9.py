import random
import time
import BST
import matplotlib.pyplot as plt

#To get started create a function, populate, that takes as a parameter a positive integer n, populates a list of length n with random integers in the range of [0, n] and returns that list.
def populate(n):
    outList = []
    outTree = BST.BST()

    for x in range(n):
        item = random.randint(0, n)
        outList.append(item)
        outTree.append(item)
    return outList, outTree

#Next create a function that takes as a parameter a list and an integer and returns True if that integer is found in the list and False if it is not.

def searchList(l, n):
    found = False
    for item in l:
        if item == n:
            found = True
    return found

#Finally, in your main script call your function for a value of n to get a list of length n and then go through that list and look for each element in that list within the list and print out that count.  Needless to say if you did everything right you should print out n

def main():
    xVals = []
    yValsList = []
    yValsBST = []
    for n in range(0,10000,1000):
        if n == 0:
            n = 1
        xVals.append(n)
        l, t = populate(n)  # get list and tree
        count_l = 0
        count_t = 0
        timeB4List = time.time()
        for item in l:
            if(searchList(l, item)):
                count_l += 1
        timeAfterList = time.time()
        timeDiffList = timeAfterList - timeB4List
        yValsList.append(timeDiffList)

        timeB4BST = time.time()
        for item in l:
            if t.isin(item):
                count_t += 1
        print('List items', count_l, '. Tree items found:', count_t)
        timeAfterBST = time.time()
        timeDiffBST = timeAfterBST - timeB4BST
        yValsBST.append(timeDiffBST)

    plt.plot(xVals,yValsList,label='list') 
    plt.plot(xVals,yValsBST,label='bst')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
