
#Generator Expression = Similar to a list comprehension but uses () instead of []
#Creates a generator (iterator) that yields values one at a time
#No need to define a function or use yield
#Less flexible than a gen func and not reusable
#gen object = (expression for value in iterable if condition)



number = int(input("Enter  a number : "))


counter  = (count for count in range(1, number + 1))

for n in counter:
    print(n)