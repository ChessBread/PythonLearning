import math

sideA = float(input("Enter length of side A: "))
sideB = float(input("Enter length of side B: "))

sideB = math.sqrt(sideA**2 + sideB**2)
print("The length of side B is:", sideB)