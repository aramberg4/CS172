#File Name:   main.py
#Purpose:     Simulates a basic payroll system.
#Author:      Austin Ramberg
#User id: 	  afr38
#Date:        March 6, 2019

from employee import Employee
from linkedList import LinkedList
from node import Node

# function to disply the main menu in the loop
def printMenu():
    print('\n')
    print('*** CS 172 Payroll Simulator ***')
    print('a. Add New Employee')
    print('b. Calculate Weekly Wages')
    print('c. Display Payroll')
    print('d. Update Employee Hourly Rate')
    print('e. Remove Employee from Payroll')
    print('f. Exit the program')

def main():
    empList = LinkedList()
    minimumWage = 6

    while True:
        # call printMenu to display menu screen and ask user for thier choice
        printMenu()
        while True:
            try:
                userInput = input('Please enter your choice: ')
                if userInput not in ['a','b','c','d','e','f']:
                    print('Please try again.')
                    continue
                break
            except:
                print('Error: your choice has to be a letter in the options menu. Try again.')
        print('\n')
        if(userInput == 'a'):
            #Add new employee: this option allows you to enter the ID of a new employee and his/her hourly rate
            while True:
                empID = input('Enter the new employee ID:  ')               
                if empList.search(empID):
                    print('Employee ID must be unique. Try again.')
                    continue
                break
            while True:
                try:
                    payRate = float(input('Enter the hourly rate:  '))
                    if payRate < minimumWage:
                        print('Hourly rate must be above $6.00. These people have families. Try again.')
                        continue
                except Exception as e:
                    print("Error: " + str(e))
                    continue
                break
            newEmp = Employee(empID, payRate)
            empList.append(newEmp)
        elif(userInput == 'b'):
            # Calculate Weekly Wages: this option displays each employee ID and asks the user to enter the number of hours worked by each employee
            for i in range(0, len(empList)):
                while True:
                    try:
                        hours = float(input('Enter hours worked for employee ' + empList[i].getEmployeeID() +': '))
                        if hours < 0:
                            print('Hours cannot be negative. Please try again.')
                            continue
                        break
                    except Exception as e:
                        print("Error: " + str(e))
                        continue
                empList[i].setHours(hours)               
        elif(userInput == 'c'):
            # Display Payroll: this option displays each employee’s identification number, hours worked, hourly rate, and gross wages.
            for i in range(0, len(empList)):
                print(empList[i])
        elif(userInput == 'd'):
            # Update Hourly Rate: this option allows the user update the hourly rate of one employee.
            empID = input('Enter the ID of the employee whose hourly rate you wish to change: ')
            while True:
                try:
                    newRate = float(input('Enter the new hourly rate:  '))
                    if newRate < minimumWage:
                        print('Hourly rate must be above $6.00. These people have families. Try again.')
                        continue
                    break
                except Exception as e:
                    print("Error: " + str(e))
                    continue
            found = False
            for i in range(0, len(empList)):
                if empList[i].getEmployeeID() == empID:
                    empList[i].setPayRate(newRate)
                    print('Done.')
                    found = True
                    break
            if not found:
                print('The employee ID entered does not exist in the system. Operation aborted.') 
        elif(userInput == 'e'):
            # Remove Employee for payroll: this option allows the user to remove an employee.
            empID = input('Enter the ID of the employee to remove from payroll: ')
            if empList.search(empID):
                empList.remove(empID)
                print('Done.')
            else:
                print('The employee ID entered does not exist in the system. Operation aborted.')          
        elif(userInput == 'f'):
            # Quit the program
            print('Goodbye!')
            break

if __name__ == "__main__":
    main()