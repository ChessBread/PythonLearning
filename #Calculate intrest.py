#Calculate interest
what_interest = input("""Do you want compound or simple interest?

1) compound
2) simple

> """).strip().lower()

if what_interest in ("simple", "2"):
    try:
        P = float(input("Enter the principal amount: "))
        R = float(input("Enter the rate of interest: "))
        T = float(input("Enter the time in years: "))
    except ValueError:
        print("Invalid numeric input.")
    else:
        SI = (P * R * T) / 100
        print("The simple interest is:", SI)
elif what_interest in ("compound", "1"):
    try:
        P = float(input("Enter the principal amount: "))
        R = float(input("Enter the rate of interest: "))
        T = float(input("Enter the time in years: "))
        n = int(input("Enter the number of times interest is compounded per year: "))
    except ValueError:
        print("Invalid numeric input.")
    else:
        CI = P * (1 + R / (100 * n))**(n * T) - P
        print("The compound interest is:", CI)
else:
    print("Invalid option selected.")

