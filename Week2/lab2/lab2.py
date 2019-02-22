import datetime


class item_class:
    def __init__(self, name, price, isTaxable):
        self.__name = name
        self.__price = price
        self.__taxable = isTaxable

    def __str__(self):
        return "{:_<20}".format(self.__name) + "{:_>20.2f}".format(
            self.__price)

    def getPrice(self):
        return self.__price


    def getTax(self):
        return self.__taxable


class Receipt:
    def __init__(self, taxRate, purchases):
        self.__taxRate = taxRate
        self.__purchases = purchases
        self.__subTotal = 0
        self.__totalTax = 0
        

    def addItem(self, name, price, isTaxable):
        self.__purchases.append(item_class(name, price, isTaxable))

    def getPurchases(self):
        return self.__purchases

    def __str__(self):
        for item in self.__purchases:
            self.__subTotal += item.getPrice()
            if item.getTax():
                self.__totalTax += item.getPrice() * self.__taxRate
                
        return '\n'.join([str(item) for item in self.__purchases]) + '\n' + "{:_<20}".format("Sub Total") + "{:_>20.2f}".format(
            self.__subTotal) + '\n' + "{:_<20}".format("Tax") + "{:_>20.2f}".format(self.__totalTax) + '\n' + "{:_<20}".format("Total") + "{:_>20.2f}".format(self.__totalTax + self.__subTotal)


def main():
    print("Welcome to Receipt Creator")

    receipt = Receipt(0.07, [])

    continue_loop = True
    while continue_loop:
        while True:
            try:
                usr_name = input("Enter Item name: ")
                break
            except:
                print('Not accepted. Try again.')

        while True:
            try:
                usr_price = float(input("Enter Iterm Price: "))
                break
            except:
                print('Not accepted. Try again.')

        while True:
            usr_isTaxable = input("Is the item taxable (yes/no): ")
            if usr_isTaxable not in ["yes", "no"]:
                print('Not accepted. Try again.')
                continue
            if usr_isTaxable == 'yes':
                pass_usr_isTaxable = True
            else:
                pass_usr_isTaxable = False
            break

        receipt.addItem(
            name=usr_name, price=usr_price, isTaxable=pass_usr_isTaxable)

        while True:
            usr_continue = input("Add another item (yes/no): ")
            if usr_continue not in ["yes", "no"]:
                print('Not accepted. Try again.')
                continue
            if usr_continue == 'no':
                continue_loop = False
            break

    # print recepipt

    print("--- Receipt " + str(datetime.datetime.now()) + " ---")
    print(receipt)