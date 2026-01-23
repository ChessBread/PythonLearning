# object = a bundle of related atributes(variable) and methods (funtions)
#       ex. phone cup book
#       you need a "class" to create many objects

#class = (blueprints) used to desighn the structure and layout of an object

from classes import Car

car1 = Car("Mustang", "2024", "Red", False)
car2 = Car("Corvetter", "2025", "Blue", True)


print(car1.model)
print(car1.year)
print(car2.color)
print(car2.for_sale)


car2.drive()