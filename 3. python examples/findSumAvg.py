# Python Program to Find Sum and Average of All Numbers entered by the User

numbers = []

while True:
    number = int(input("Enter the number: "))
    numbers.append(number)

    anotherNumber = input("Enter another number? (y / n) : ")
    if anotherNumber.casefold() == 'n':
        
        print("SUM: ", sum(numbers))
        print("AVG: ", (sum(numbers)/len(numbers)))
        break



# ex output:
# SUM:  10
# AVG:  2.0

# Traditional SUM Logic
    
# sumValue = 0
# for eachNum in numbers:
#     sumValue += eachNum
# print("SUM ", sumValue)