# logicaloperators = used on conditional statements
# ande = checks two or more conditions if true
# or = checks if at least one condition is true
# not = True if condition is false, and vice versa


temp = int(input("What is the temperature outside? "))
sunny = True

if temp >= 0 and temp >= 30:
    print("the temp is bad")
elif temp < 0 or temp > 30:
    print("the temp is good")
elif not temp >= 30:
    print("the temp is okay")
elif temp == 30 and sunny == True:
    print("the temp is great")