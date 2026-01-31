# a funtion that calls iteself from within
#       help to visualize a complex problem into basic steps
#       wich can be solved more easily iteratively ot recursively


#iter
#def walk(steps):
#    for step in range(1, steps + 1):
#       print(f"You take step #{step}")


#recur
#def walk(steps):
#    if steps == 0:
#       return
#    walk(steps - 1)
#    print(f"you take step #{steps}")

#walk(100)



#iter func

#def factorial(x):
#    result = 1
#    if x > 0:
#        for y in range(1, x + 1):
#            result = result * y
#    return result

#print(factorial(10))



# recur func
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)
    
print(factorial(10))