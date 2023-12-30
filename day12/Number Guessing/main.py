import random
from art import logo

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_ATTEMPTS
    else:
        return HARD_ATTEMPTS


def compair(guess,secret_number,attempts):
    '''Return remaining number of attempts'''
    if guess == secret_number:
        print(f"You got it! The answer is {secret_number}.")
        return attempts
    elif guess < secret_number:
        print("Too low.")
        return attempts - 1
    else:
        print("Too high.")
        return attempts - 1


def number_guessing():
    print(logo)
    print("I'm thinking of a number between 1 and 100,")
    secret_number = random.randint(1,100)

    attempts = set_difficulty()

    guess = 0
    while guess != secret_number:
        if attempts == 0:
            print(f"You've run out of guesses, you lose.")
            break
        else:
            print(f"You have {attempts} remaining to guess the number.")

        guess = int(input("Make a guess: "))
        attempts = compair(guess,secret_number,attempts)
        if not guess == secret_number:
            print("Guess again.")



number_guessing()