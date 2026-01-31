#Data Class = A special kind of class that's designed mostly for holding data
#without writing a lot of the boilerplate code for regular classes.
#They automatically generate: _init__, __repr__, __eq_
#(Python 3.7+)

from dataclasses import dataclass
from dataclasses import field

@dataclass (frozen = True)
class Person:
    name: str
    age: int
    password: str = field(repr=False)
    is_alive: bool = True

    def __post__init__(self):
        if self.age  < 0:
            raise ValueError("Age cannot be negative")



person1 = Person("spongebob", 30, "Pineapple1")
person2 = Person("patrick", 35, "password")

print(person1)
print(person2)
print(person1 == person2)