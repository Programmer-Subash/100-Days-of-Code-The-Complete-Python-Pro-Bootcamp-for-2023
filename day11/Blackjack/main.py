import random
from art import logo

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_cards = []
computer_cards = []

def draw_random_card(name:str):
    '''name can be user or computer'''
    if name == 'user':
        user_cards.append(random.choice(cards))
    else:
        computer_cards.append(random.choice(cards))

def count_card(cards):
    '''Count the card of the game'''
    total = sum(cards)
    if total > 21 and 11 in cards:
        total -= 10
        cards.remove(11)
        cards.append(1)
    return total


def check_for_winner():
    user_total = count_card(user_cards)
    computer_total = count_card(computer_cards)

    print(f'Your final hand: {user_cards}, final score: {user_total}')
    print(f'Computer\'s final hand: {computer_cards}, final score: {computer_total}')

    if computer_total < 17:
        print('Computer final score is less than 17. You win')
    elif computer_total > 21:
        print('Opponent went over. You win')
    elif 21 - user_total < 21 - computer_total:
        print('You win')
    elif 21 - user_total > 21 - computer_total:
        print('Computer win')
    else:
        print('Draw')

def blackjack():
    print(logo)

    user_cards.clear()
    computer_cards.clear()


    for _ in range(3):
        draw_random_card('computer')
        draw_random_card('user')

    print(f'Your cards: {user_cards}, current score: {count_card(user_cards)}')
    print(f'Computer\'s first card: {computer_cards[0]}')

    winner_declare = False
    want_card = True
    while want_card:
        if input('Type "y" to get another card, type "n" to pass: ') == 'n':
            want_card = False
            break

        draw_random_card('user')
        draw_random_card('computer')

        if count_card(user_cards) > 21:
            print(f'Your final hand: {user_cards}, final score: {count_card(user_cards)}')
            print(f'Computer\'s final hand: {computer_cards}, final score: {count_card(computer_cards)}')
            print('You went over. Computer win')
            want_card = False
            winner_declare = True
            break

        print(f'Your cards: {user_cards}, current score: {count_card(user_cards)}')
        print(f'Computer\'s first card: {computer_cards[0]}')

    if not winner_declare:
        check_for_winner()

    if input('Type "y" to play again otherwise type "n" ') == 'y':
        blackjack()

blackjack()