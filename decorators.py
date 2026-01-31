# a function that extends the behavoir of another function
#           w/o modifying the base function
#           pass the base funtion as an argument to the decorator

#           @add_sprinkles
#           get_ice_cream("vanilla")




def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("you add sprinkles")
        func(*args, **kwargs)
    return wrapper


def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("you add fudge")
        func(*args, **kwargs)
    return wrapper


@add_sprinkles
@add_fudge
def get_ice_cream(flavour):
    print(f"here is your {flavour} ice cream")



get_ice_cream("chocolate")