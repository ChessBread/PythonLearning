# while loop = execute some code While a condition remains true

food = input("Enter food : ")

while not food == "q":
    print(f"You like {food} ")
    food = input("Another food : ")
else:
    print("Cheese")