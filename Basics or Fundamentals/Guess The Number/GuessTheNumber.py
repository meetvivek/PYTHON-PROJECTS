import random
import os
from art import logo


def difficult(difficulty):
    if difficulty == "hard":
        attempt = 5
    elif difficulty == "easy":
        attempt = 10
    while attempt >= 1:
        print(f"You have {attempt} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == real_number:
            print(f"\tYou got it! The answer was {guess}.")
            exit()
        elif guess > real_number and attempt > 1:
            print("\tToo High.\n\tGuess again.")
        
        elif guess < real_number and attempt > 1:
            print("\tToo Low.\n\tGuess again.")
        attempt -= 1
    else:
        print(f"Sorry You lost, the Number was: {real_number}")

check = 'yes'    
while check == "yes":
    print(logo)
    real_number = random.randrange(1, 100)
    print("Welcome to the Number Guessing Game !")
    input_number = print("I'm thinking of a number between 1 amd 100.")
    difficulty = input("Choose a difficulty Type 'easy' or 'Hard': ").lower()

    difficult(difficulty)

    check = input("Do you want to play the guessing game again. Type 'yes' or 'no': ").lower()
    if check == 'yes':
        os.system('cls')
    else: 
        print("Thank You!")

