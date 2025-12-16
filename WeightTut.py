unit = input("Enter KG or Lbs: ")
Weight = float(input("Enter weight: "))

if unit.upper() == "KG":
    converted = Weight / 0.45
    print(f"Weight in Lbs: {converted}")
elif unit.upper() == "LBS":
    converted = Weight * 0.45
    print(f"Weight in KG: {converted}")
else:
    print("Invalid unit")