# if = do some code only if a certain condition is met
# else do something else

age = int(input("How old are you? "))

if age >= 18:
    print("You can get a credit card!")
elif age < 0:
    print("That is not a valid age.")
elif age >= 100:
    print("You are quite old to be getting a credit card!")
else:
    print("You must be 18+ to get a credit card.")