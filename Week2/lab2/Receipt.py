class Receipt:
    
    def __init__ (self, taxRate, purchases):
        self.__tax_rate = taxRate
        self.__purchases = purchases
        
    def addItem(self, item):
        self.__purchases.append(item)
        
    def __str__(self):
        for purchase in self.__purchases:
            print("{:_<25}".format(purchase.__name) + str(purchase.__price))

#if __name__ == "__main__" :
#    l = list()
#    myReceipt = Receipt(0.3, l)
#    myReceipt.addItem('Hotdog')
#    myReceipt.__str__() 