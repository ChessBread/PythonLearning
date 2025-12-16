#Variable = a container for a value (string, integer, float, boolean)
# A variable behaves as if it was the value that it contains

#strings
name = "John"
food = "pizza"
email = "alden@fake.co.za"

#integer
age = 25
distance = 100
float_height = 175.5

print(f"Hello, my name is {name}. I am {age} years old and I love eating {food}. You can contact me at {email}. I live {distance} kilometers away from here. My height is {float_height} centimeters.")




#boolean
is_male = True
is_female = False
is_tall = False
is_short = False

if is_male and is_tall:
    print("You are a tall and a male.")
elif is_female and is_short:
    print("You are a short female.")
elif is_male and is_short:
    print("You are a short male>")
elif is_female and is_tall:
    print("You are a tall Female.")
else:
    print("I dont know")
