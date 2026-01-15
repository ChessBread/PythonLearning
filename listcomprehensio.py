# list comprehension=  A concise way to create list in pyyhon
#           compact and easier to read 
#           [expressio for value in iterable if condition]

grades = [85, 42, 79, 90, 56,  61, 30]
passing_grades = [grade for grade in grades if grade  >=  60]



print(passing_grades)