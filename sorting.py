# sorting .sort() or sorted()
# list [], tuples(), dictionaries {"":""}, objects

# ----- lists ------

#fruits = ["banana", "orange", "apple", "coconut"]

#fruits.sort(reverse = True)


# ---- tuples -----

#fruits  = ("banana", "orange", "apple", "coconut")

#fruits = tuple(sorted(fruits))
#fruits = tuple(sorted(fruits, reverse = True))


# ------ Dictionaries ------


#fruits = {"banana" : 105,
            "orange" : 73,
            "apple" : 72,
            "coconut" : 354}


#fruits = dict(sorted(fruits.items()))
#fruits = dict(sorted(fruits.items(), key = lambda item: item[0], reverse = True))
#fruits = dict(sorted(fruits.items, key = lambda item: item[1]))
#fruits = dict(sorted(fruits.items, key = lambda item: item[1], reverse = True))

# ----- objects -----

class Fruit:
        def __init__(self, name, calories):
                self.name = name
                self.calories = calories

        def __repr__(self):
                return f"{self.name}: {self.calories}"
        

fruits = [Fruit("banana, 105",
            Fruit("apple, 72"), 
            Fruit("orange, 73"),
            Fruit("Coconut, 354"))]

fruits = sorted(fruits, key = lambda fruit : fruit.name)
fruits = sorted(fruits, key = lambda fruit : fruit.name, reverse = True)
fruits = sorted(fruits, key = lambda fruit : fruit.calories)
fruits = sorted(fruits, key = lambda fruit : fruit.calories, reverse = True)

print(fruits)
