# Python Program to Find the Factorial of a Number Tutorial

# n! = n*(n-1)*(n-2)...*2*1.

def findFactorialNumber():
    while True:
        try:
            findFactorial = int(input("Enter the number (0 to STOP): "))
            factorial = 1

            if (findFactorial < 0):
                print("Can't compute the factorials for -ve numbers.")
            elif (findFactorial == 0):
                break
            elif findFactorial < 2:
                print("{}! => {}".format(findFactorial, factorial))
                # factorial = factorial
            else:
                for number in range(findFactorial, 1, -1):
                    factorial = factorial * number
                
                print("{}! = {}".format(findFactorial, factorial))

        except ValueError as err:
            print("Value Error: ", err)
                
        # return factorial
        
# function call
findFactorialNumber()