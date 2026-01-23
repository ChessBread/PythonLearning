import random


def spin_row(symbols):
    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    print("************")
    print(" | ".join(row))
    print("************")


def get_payout(row, bet):
    # Payout only when all three symbols match
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20
    return 0


def main():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]
    balance = 100

    print("")
    print("Welcome to Python Slots!")
    print("")

    while balance > 0:
        print(f"Current balance: ${balance}")

        # get a valid bet from the player
        while True:
            bet_amount_str = input("Place your bet amount: ")
            if not bet_amount_str.isdigit():
                print("Please enter a valid number.")
                continue
            bet = int(bet_amount_str)
            if bet > balance:
                print("Insufficient funds.")
                continue
            if bet <= 0:
                print("Bet must be greater than zero.")
                continue
            break

        balance -= bet

        print("\nSpinning...")
        row = spin_row(symbols)
        print_row(row)

        payout = get_payout(row, bet)
        balance += payout

        if payout > 0:
            print(f"You won ${payout}!")
        else:
            print("Sorry, you lost this round.")

        if balance <= 0:
            print("You have run out of money!")
            break

        play_again = input("Do you want to spin again? (Y/N): ").strip().upper()
        if play_again != 'Y':
            break

    print("")
    print(f"GAME OVER! Your final balance is ${balance}")
    print("")


if __name__ == "__main__":
    main()