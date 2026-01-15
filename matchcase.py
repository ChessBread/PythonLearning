# match-case = (switch) an allternative to if-elif-else statements
#               execute some code if a value matches a case
#               benefits = cleaner and more readable code

def is_weekend(day):
    match day:
        case "sunday":
            return True
        case "saturday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False

print(is_weekend("monday"))