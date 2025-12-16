# conditional expression = a one line shortcut for the if-else statement(ternary operator)
# print or assign one of two values based on a condition
# x if condition else y



num = 5
a = 6
b= 7
age = 25
temp = 20
User_role = "admin"

#print("positive" if num > 0 else "negative")

#result = "even" if num % 2 == 0 else "odd"


#max = a if a > b else b
#min = a if a < b else b
#status = "adult" if age >= 18 else "minor"
#weather = "warm" if temp >= 15 else "cold"
access_level = "admin" if User_role == "admin" else "user"

print(access_level)