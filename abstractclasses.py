# abstract class: A class that cannot be instantiated on its own: meant to be subclassed
#               often contains one or more abstract methods 
#              abstract classes benifites:
#            1. prevents instantiation of class itself
#            2. requires children to use inherited abstarct methods

from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass



class Car(Vehicle):

    def go(self):
        print("the car is moving")

    def stop(self):
        print("the car has stopped")

class Motorcycle(Vehicle):
    
    def go(self):
        print("the motorcycle is moving")

    def stop(self):
        print("the motorcycle has stopped")

car = Car()
motorcycle = Motorcycle()
car.go()
motorcycle.stop()
