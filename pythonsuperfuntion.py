# super() = funtion used in a child class to call methods from a parent class
#         Allows you to exend the functionality of the inherited methods


class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.filled = is_filled



    def describe(self):
        print(f"it is {self.color} and {'filled' if self.filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
    
    def describe(self):
        print(f"it is a circle with an are of {3.14 * self.radius * self.radius} , it is {self.color} and {'filled' if self.filled else 'not filled'}")
        super().describe()

class Square(Shape):
    def __init__(self, color, is_filled, side_length):
        super().__init__(color, is_filled)
        self.side_length = side_length

    def describe(self):
        print(f"it is a square with an area of {self.side_length * self.side_length} , it is {self.color} and {'filled' if self.filled else 'not filled'}")
        super().describe()

class triangle(Shape):
    def __init__(self, color, is_filled, base, height):
        super().__init__(color, is_filled)
        self.base = base
        self.height = height

    def describe(self):
        print(f"it is a triangle with an area of {0.5 * self.base * self.height} , it is {self.color} and {'filled' if self.filled else 'not filled'}")
        super().describe()



circle = Circle("red", True, 5)
square = Square("blue", False, 4)
triangle = triangle("green", True, 6, 8)

circle.describe()
square.describe()
triangle.describe()