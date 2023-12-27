# Python Program to Check entered Number for Prime or Composite

# INTRO:

# Prime number:2, 3, 5, 7, 11, 13, 17, 19...
# is a natural number greater than 1, which has exaclty two factors OR divisble by 1 and the number itself.
# example: 2 is divible by 1 & 2 only. Therefore, it is a Prime number.

# Composite number:4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21...
# is a natural number graater than 1, which has more than two factors OR completely divisble by more than two numbers OR which is not a Prime number.
# example: 4 is completely divisible by 1, 2, 4. Therefore, it is a composite number

# NOTE: 1 is niether Prime number nor Composite number (not than 2 factors).


# Program:
def checkNumber():
    while True:
        number = int(input("Enter a natural number (0 to stop): "))
        if number < 0:
            print("Please enter number greater than 1 :")
        elif number == 0:
            break
        elif number == 1:
            print("Please enter number greater than 1: ")
        elif (number == 2) or (number == 3):
            print(number, "is a Prime number")
        else:
            for divisor in range(2, (number//2)+1):
                if (number % divisor) == 0:
                    print(number, "is a Composite number")
                    break
                else:
                    print(number, "is a Prime number")
                    break

# function call
checkNumber()