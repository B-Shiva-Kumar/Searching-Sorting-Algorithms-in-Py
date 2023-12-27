# Python Roll the Dice Program

import random

def rollDice(min, max):

    while True:

        print("Rolling Dice...")

        number = random.randint(min, max)
        print(f"Your number : {number}")

        choice = input("Do you want to roll again? (y/n)")
        if choice.casefold() == 'n':
            break


rollDice(1, 6)