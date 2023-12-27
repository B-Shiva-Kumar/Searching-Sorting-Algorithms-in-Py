# Python Program to Print Multiplication Table of a number

def multiplicationTable():

    while True:
            
        number = int(input("Enter the number for multiplication (0 to STOP) : "))
        if (number == 0):
            print("STOPPED")
            break

        for mul in range(1, 11):
            print("{} * {} = {}".format(number, mul, (number*mul)))


multiplicationTable()