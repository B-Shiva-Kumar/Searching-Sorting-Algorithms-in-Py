# User Input data 

data = []

while True:
    name = input("Enter a name: ")
    data.append(name)

    choice = input("Enter another name? (y / n): ")
    if choice.casefold() == 'n':
        break

for name in data:
    print(name)


# OUTPUT:
    
# Shiva
# Mousin
# Ashwin
