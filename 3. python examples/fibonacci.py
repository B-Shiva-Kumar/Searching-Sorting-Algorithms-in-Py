# fibanacci serires in Python

def fibonacci(n):

    fibonacciArray = [0, 1]

    if n < 0:
        return "Invalid Input"
    elif n < len(fibonacciArray):
        return fibonacciArray
    else:
        for i in range(2, n):
            fibonacciArray.append(fibonacciArray[i-1] + fibonacciArray[i-2])

        print(f"Sum of Fibanacci Series of {n} is ", sum(fibonacciArray))
        return fibonacciArray

print(fibonacci(10))