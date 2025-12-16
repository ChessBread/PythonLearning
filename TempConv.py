unit = input("Enter C or F: ")
Temp = float(input("Enter temperature: "))

if unit.upper() == "C":
    converted = (Temp * 9/5) + 32
    print(f"Temperature in F: {converted}")
elif unit.upper() == "F":
    converted = (Temp - 32) * 5/9
    print(f"Temperature in C: {converted}")
else:
    print("Invalid unit")