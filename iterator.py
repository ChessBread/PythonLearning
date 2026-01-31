# an object that returns elements one at a time
# __iter__() returns the iterator  object
# __next__()  returns the next  item

import random


class Dice():

    def __init__(self, rolls):
        self.rolls = rolls
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count <  self.rolls:
            self.count += 1
            return  random.randint(1,6)
        else:
            raise StopIteration
        

dice = [die for die in Dice(3)]


