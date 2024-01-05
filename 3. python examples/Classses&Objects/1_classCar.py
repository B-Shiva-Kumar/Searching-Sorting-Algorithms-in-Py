class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_make(self):
        return self.make
    
    def get_model(self):
        return self.model
    
    def get_year(self):
        return self.year
    
    def get_all(self):
        return self.make, self.model, self.year


# create and access 
myCar = Car("Benz", "Benz EX-1", 2024)
print(myCar.get_all())