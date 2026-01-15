# args = allows you to pass multiple non key arguments
# kwargs = allows you to pass multiple key arguments (keyword arguments)
#               unpacking opperator = *
#              1. psotional 2. default 3. KEYWORD 4. arbitrary

def shipping_lable(*args, **kwargs):
    for arg in args:
        print(arg, end = " ")
    print()
    
    if "apt" in kwargs:
        print(f"{kwargs.get('street')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('apt', 'N/A')}, {kwargs.get('state')}, {kwargs.get('zip')}")
    
shipping_lable("Dr.", "spongebob", "Squarepants", "III",
               street="123 Ocean Ave",
               pobox = " PO Box #100",
               state = "MI",
               zip = "12345"
               )