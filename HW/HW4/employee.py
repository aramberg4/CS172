#File Name:   employee.py
#Purpose:     File contains Employee class.
#Author:      Austin Ramberg
#User id:     afr38
#Date:        March 6, 2019

class Employee:

    # initialization method 
    def __init__(self,
                employeeID,
                payRate,
                hours=0):
        self.__employeeID = employeeID
        self.__payRate = payRate
        self.__hours = hours        
        self.__grossWages = self.__payRate*self.__hours

    # getters
    def getEmployeeID(self):
        return self.__employeeID

    def getHours(self):
        return self.__hours

    def getPayRate(self):
        return self.__payRate

    def getGrossWages(self):
        self.__grossWages = self.__payRate*self.__hours
        return round(self.__grossWages, 2)

        
    # setters
    def setHours(self, h):
        self.__hours = h

    def setPayRate(self, pr):
        self.__payRate = pr 

    # overload __str__ method
    def __str__(self):
        return "Employee ID: " + str(self.getEmployeeID()) + '\n' + "Hourly Rate: " + str(self.getPayRate()) + '\n' + "Hours Worked: " + str(self.getHours()) + '\n' + "Gross Wages: " + str(self.getGrossWages()) + '\n' 

    #overload __eq__ method
    def __eq__(self, other):
        return (self.getEmployeeID() == other.getEmployeeID())


# for testing purposes
if __name__ == "__main__":
    myEmp = Employee(123, 12.75, 20)
    print(myEmp)
    print('Adding 20 hours worked.')
    myEmp.setHours(40)
    print(myEmp)
    print('Increasing wage by $1.')
    myEmp.setPayRate(13.75)
    print(myEmp)

