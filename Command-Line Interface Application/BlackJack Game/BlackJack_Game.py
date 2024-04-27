import os
import random
from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, Computer has Blackjack."
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over, You Lose."
    elif computer_score > 21:
        return "Computer went over, You Win."
    elif user_score > computer_score:
        return "You win."
    else:
        return "You lose."


def play_game():
    os.system('cls')
    print(logo)
    is_game_over = False
    user_card = []
    computer_card = []

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)

        print(f"\tYour card: {user_card}, current score: {user_score}")
        print("\tComputer's first card:", computer_card[0])

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            check = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if check == 'y':
                user_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    # Recalculate computer's score after drawing additional cards
    computer_score = calculate_score(computer_card)

    print(f"\tYour final hand: {user_card} and final score: {user_score}")
    print(f"\tComputer final hand: {computer_card} and final score: {computer_score}")
    print("RESULT: ", compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'Yes' or 'No': ").lower() == "yes":
    play_game()
