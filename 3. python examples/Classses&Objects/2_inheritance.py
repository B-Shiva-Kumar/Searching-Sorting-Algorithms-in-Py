# Parent Class:
class Vehicle(object):

    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color

    def fullTank(self):
        self.fullTank = 100
        return self.fullTank

    def emptyTank(self):
        self.emptyTank = 0
        return self.emptyTank


# Child class 1
class Car(Vehicle):
    def __init__(self, price, gas, color, speed):
        super().__init__(price, gas, color)             # inheritance from parent class
        self.speed = speed
    
    def horn(self):
        return "BEEP BEEP!"


# Child class 2
class Truck(Vehicle):
    def __init__(self, price, gas, color, tires):
        super().__init__(price, gas, color)             # inheritance from parent class
        self.tires = tires

    def horn(self):
        return "HONK HONK!"



# create & access
benz = Car(12000, "Petrol", "black", "100km/h")
print(benz.horn())

mahindraTuck = Truck(100000, "Diesel", "White", "75-80 km/hr")
print(mahindraTuck.horn())

# OUTPUT:

# BEEP BEEP!
# HONK HONK!