username = input("enter your username : ")

if len(username) > 12:
    print("this is valid")
elif not username.find(" ") == -1:
    print("Username can't contain spaces")
elif not username.isalpha():
    print("Username can't contain numbers")
else:
    print("This is an invalid username")