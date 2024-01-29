# HCF or GCF:
# The full form of HCF is Highest Common Factor. HCF of two numbers is the highest factor that can divide the two numbers, evenly.


def findHCF(num1, num2):

    if num1 > num2:
        smaller = num2
    else:
        smaller = num1
    
    for i in range(1, smaller+1):
        if ((num1%i) == 0) and ((num2%i) == 0):
            factor = i
    print(factor)
    
    # return factor

# function call
findHCF(10, 20)