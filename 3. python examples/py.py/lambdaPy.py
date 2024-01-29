# Python Lambda

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# ---
# ex1
x = lambda x: x + 1
print(x(1))
# output -> 2

# ex2
y = lambda a, b: a*b
print(y(10, 10))
# output -> 100

# ex3
kmToMiles = lambda kmValue: kmValue * 0.621371
print(f"{2} KM to Miles Conversion : ", kmToMiles(2))
# output -> 2 KM to Miles Conversion :  1.242742

# ex4
greetName = lambda name: f"Hello, {name}"
print(greetName("Python"))
# output -> Hello, Python