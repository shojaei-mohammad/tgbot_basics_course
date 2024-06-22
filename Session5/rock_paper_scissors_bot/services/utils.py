import random


def bot_choice():
    return random.choice(["Rock", "Paper", "Scissors"])


def get_winner(user_choice, bot_choice):
    rules = {
        "Rock": "Scissors",
        "Scissors": "Paper",
        "Paper": "Rock",
    }
    if user_choice == bot_choice:
        return "Draw, No one wins"
    elif rules[user_choice] == bot_choice:
        return "You win"
    else:
        return "You lose"
