#shopping cart

item = input("Enter the item you want to add to the shopping cart: ")
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: "))


total = price * quantity

print(f"You have baught {quantity} x {item}/s")
print(f"Your total is: ${round(total, 2)}")