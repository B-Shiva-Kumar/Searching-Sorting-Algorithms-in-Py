# Find smallest and largest number

print("Example 1")
numbers = [123, 21, 121, 5, 19, 38, 1]
numbers.sort()

minNum = numbers[0]
maxNum = numbers[-1]

print("Minimum number: ", minNum)
print("Maximum number: ", maxNum)

# ______________________________

print("Example 2")

numbersList = [123, 21, 121, 5, 19, 38, 1]
smallest = min(numbersList)
largest = max(numbersList)

print("Smallest number: ", smallest)
print("Largest number: ", largest)



# OUTPUT:

# Example 1
# Minimum number:  1
# Maximum number:  123
# Example 2
# Smallest number:  1
# Largest number:  123