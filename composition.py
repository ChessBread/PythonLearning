# aggregation = a relationship where on object contains refrerences to other objects
# has-a relationship

# composition = the composed object owns its components, whic cannot exitst independently
# owns-a relationship




class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, model, horsepower, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horsepower)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]

    def display_car(self):
        return f"{self.make} {self.model} {self.engine.horsepower}HP {self.wheels[0].size} in"

car = Car("Toyota", "Camry", 200, 16)


car2 = Car("Honda", "Accord", 190, 17)

print(car.display_car())
print(car2.display_car())