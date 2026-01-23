# duck typing = another way to achive polymorphism besides inheritance
# object must have minimum necessary attributes/methods
# "if it looks like a duck and quacks like a duck, it must be a duck"


class Animal:
    alive = True


class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")


class Car:

    alive = False

    def speak(self):
        print("Beep!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
   animal.speak()
   print(animal.alive)