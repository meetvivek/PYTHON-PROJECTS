import random
import os
from art import logo, vs
from data import data

print(logo)

game_on = True
score = 0
B = random.randrange(0, len(data)-1)  
while game_on:
    A = B
    B = random.randrange(0, len(data)-1)  
    while A == B:
        B = random.randrange(0, len(data)-1)  
    
    print(f"Compare A: {data[A]['name']}, {data[A]['description']}, from {data[A]['country']}")
    print(vs)
    print(f"Compare B: {data[B]['name']}, {data[B]['description']}, from {data[B]['country']}")

    user = input("Who has more followers? Type 'A' or 'B': ").upper()

    if (data[A]['follower_count'] > data[B]['follower_count']) and user == "A":
        score += 1
        os.system('cls')
        print(logo)
        print(f"You're right! Current score : {score}")
        
    elif (data[A]['follower_count'] < data[B]['follower_count']) and user == "B":
        score += 1
        os.system('cls')
        print(logo)
        print(f"You're right! Current score : {score}")
        
    else:
        game_on = False
        os.system('cls')
        print(f"Sorry, that's wrong. Final score : {score}")
