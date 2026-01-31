# an event that interrupts the flow of a program
#           (ZeroDivisionError, typeerror, valueerror)
#           1. try, 2. expect, 3. finally


try:
    number = int(input("enter a number: "))

    print(1 / number)
except ZeroDivisionError:
    print("number cant be divided by 0")
except TypeError:
    print("Please enter a number")
except ValueError:
    print("this is an invalid value")
finally:
    print("Do some cleanup")