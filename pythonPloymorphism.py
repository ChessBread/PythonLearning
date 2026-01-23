# polymorphism = greek work that mean to "have many faces or forms"

# poly = many
# morph = forms

# two ways to achive this
# 1. inheritance
# 2. duck typing = object must have neccesary attributes/methods

from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    

class Pizza(Circle):
    def __init__(self, topping, radius):
        self.topping = topping
        super().__init__(radius)


shapes = [Circle(24), Square(2), Triangle(3 , 5), Pizza("pepperoni", 12)]


for shape in shapes:
    print(f"{shape.area()}cm²")
