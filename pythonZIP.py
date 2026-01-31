# zip() combines mltiple iterables (list, tuples, sets, dict)
#       into a single iterator
#       makes managing multiple indices easier


names = ["spongebob", "patrick", "squidward"]

age = [30, 35, 50]

jobs = ["cook", "none", "cashier"]

data = zip(names, age, jobs)



for name, age, jobs in data:
    print(f"{name} is {age} years old, and is a {jobs}")

print(data)