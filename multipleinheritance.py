# multiple inheritance = inherit from more than one parent class
#               C(A, B)

# multilevel inheritance = inherit from a parent which inherits from another parent
#               c(B) <-- B(A) <-- A

class Animal:

    def __init__(self, name):
        self.name = name



    def eat(self):
        print(f"this {self.name} is eating")


    def sleep(self):
        print(f"this {self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print("this animal is fleeing")

class Predator(Animal):
    def hunt(self):
        print("this animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("bugs")
hawk = Hawk("Tony")
fish = Fish("Fishy")


fish.eat()