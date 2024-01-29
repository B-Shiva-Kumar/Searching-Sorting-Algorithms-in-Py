########################################################################################################
# Exceptional Handling:

# Exception Handling in Python which can be achieved using the “try-except” statement. 
# Exceptions are the events that are triggered when the program encounters an error during execution. 
# When an error occurs, we can handle these exceptions to avoid the program from getting crashed.

# reference: https://python-by-examples.readthedocs.io/en/latest/exceptional_handling/introduction/
########################################################################################################

# ---

# example without try-except block:
# -
def implementDivision(a, b):
  value = a/b
  print(value)

implementDivision(10, 0) # throws ZeroDivisionError
# -
# ERROR:ZeroDivisionError: division by zero

# ---

# example with `try except` block - ERROR Handling
def implementDivision(a, b):
    try:
        value = a/b
        print(value)
    except ZeroDivisionError:
        print("Number cannot be divided by Zero")
    except FileNotFoundError:
        print("The File cannot be found")
    except:
        print("This is the Generic Error")

implementDivision(10, 0)

# ---

# example: Working with Finally Block in “try-except”
######################################################################################
# Finally, Block contains all the execution statements that must be executed 
# whether the exception occurred or not during the program execution. 
# The statement inside “finally” will execute irrespective of failure or success. 
######################################################################################

def readFileContent():
    fileReader = None
    try:
        fileReader = open("text.json")
        print(fileReader.read())
    except:
        print("Cannot Read the specified File OR no such file")
    finally:
        print("Closing the file reader")
        # fileReader.close()
        # OR different Code

readFileContent()


# ---


# example: Raising Custom Exceptions - `raise Exception()`

def mainFunction(range):
    try:
        if range > 100 or range < 0:
            raise Exception()
        if range < 100 and range > 0:
            range = range / 2
            range = range + 10
            print(f"The output for the execution is : {range}")
    except:
        print(f"Number {range} not under the specified range")

mainFunction(160)
mainFunction(10)

# ---