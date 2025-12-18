# format specifiers = {:flags} format a value based on what
# flags are inserted


# .(number)f = round to that many decimals
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center alighn
# :+ = use a plus sihn to indicate positive avlue
# := = place sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator

price1 = 3.14159 
price2 = -987.65
price3 = 12.34

price4 = -12530.91273

print(f"price 1 is {price1:.2f}")
print(f"price 2 is {price2:10}")
print(f"price 3 is {price3:<10}")
print(f"price 4 is {price4:+,.2f}")