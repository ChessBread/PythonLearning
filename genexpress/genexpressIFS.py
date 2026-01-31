number = int(input("ENter a number to square : "))


even_squares  = (x**2 for x in range(1, number + 1) if x % 2 ==  0 )


for square in even_squares:
    print(even_squares)