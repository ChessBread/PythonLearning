import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num , highest_num)
guesses = 0
is_running = True

print("Python guessing game")

print(f"Select a number betwees {lowest_num} and {highest_num} : ")


while is_running:
    guess = input("enter your guess : ")
    
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if guess < lowest_num or guess > highest_num:
            print("that num is out of range")
            print(f"please select a number between {lowest_num} and {highest_num} : ")
        elif guess < answer:
            print("too low")
        elif guess > answer:
            print("Too high")
        else:
            print("Correct")
            print(f"This took guesses : {guesses}")
    else:
        print("this is an invalid guess")
        print(f"please select a number between {lowest_num} and {highest_num} : ")
