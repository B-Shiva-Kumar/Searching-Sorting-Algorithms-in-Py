# What is Map in py?
# Map function is used to iterate on a function and its arguments should be iterable
# Example: map (functionname, arguments)

#  example1
### Declare a function
def fun(a,b):
 return a+b

### Call a function
x= map(fun,("orange","grapes"),("banana","Mango"))
print(x)
print(list(x))


# output
# <map object at 0x000001D66A859DB0>
# ['orangebanana', 'grapesMango']


# example2
def addNums(num1, num2):
 return num1 + num2

mapFun = map(addNums, (1, 1, 1), (2, 4, 1))
print(list(mapFun))
