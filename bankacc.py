#bank program

def show_balance(balance):
    print(f"Your balance is  ${balance:.2f}")

def deposit():
    amount  = float(input("Eneter an amount to be deposited: "))

    if amount < 0:
        print("That is not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount  = float(input("eneter a amount to withdraw"))

    if amount > balance:
        print("Insufficient funds")
    elif amount < 0:
        print("amount must be greater than 0")
        return 0 
    else:
        return amount
   
def main():
    balance  = 0
    is_running =  True

    while is_running:
        print("Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice =input("enter your choice  (1-4):")

        if choice == "1":
            show_balance(balance)
        elif choice ==  "2":
            balance += deposit()
        elif choice == "3":
            balannce  -= withdraw(balance)
        elif  choice == "4":
            is_running =  False
        else:
            print("that is a invalid choice")

    print("That you, have a nice day")


if __name__ == '__main__':
    main()