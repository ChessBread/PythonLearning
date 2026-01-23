# inheritance = allows a class to inherit attributes and methods from another class
# code reuseability
# class child(parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def speak(self):
        print("WOOF")

class Cat(Animal):
    pass


dog = Dog("scooby")

cat = Cat("Garfield")


print(dog.name)
dog.eat()
dog.speak()