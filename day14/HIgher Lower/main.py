import os
import random
from game_data import data
from art import logo
from art import vs


#choose random account from data list
def random_account(data):
    """return random account data"""
    return random.choice(data)


#display two account data in a format
def display_account_data(a:dict,b:dict):
    """Display the data of two account which is easy to read"""
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")


#compair who has more follower
def compair_follower(a:dict,b:dict)->str:
    """Compair the two account follower count and return who have more follower"""
    if a["follower_count"] > b["follower_count"]:
        return 'a'
    else:
        return 'b'

#game logic
def higher_lower_game():
    a = random_account(data)
    score = 0
    while True:
        print(logo)
        if score > 0:
            print(f"You're right! Current score: {score}.")

        #a and b must be distinct
        b = random_account(data)
        while b == a:
            b = random_account(data)

        display_account_data(a,b)
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        more_followers = compair_follower(a,b)

        if guess == more_followers:
            score += 1 #increasing score

            #for another game greater follower became a
            if more_followers == 'b':
                a = b
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            break

        os.system('clear')
higher_lower_game()