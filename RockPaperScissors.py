# Simple rock paper scissors lizard spock game
import random

OPTIONS = {"r": "rock", "p": "paper", "s": "scissors","l": "lizard","k": "spock"}

def play(choice, comp):
    if choice == comp:
        pass

    elif choice == "r":
        if comp in ("s", "l"):
            return True
        else: 
            return False
    elif choice == "p":
        if comp in ("r", "k"):
            return True
        else:
            return False
    elif choice == "s":
        if comp in ("p", "l"):
            return True
        else:
            return False
    elif choice == "l":
        if comp in ("k", "p"):
            return True
        else:
            return False
    else:
        if comp in ("s", "r"):
            return True
        else:
            return False

while True:
    choice = input("Rock (R), Paper (P), Scissors (S), Lizard (L), Spock (K) or e(x)it: ").lower()
    while choice not in OPTIONS and choice != "x":
        choice = input("Not valid input. Rock (R), Paper (P), Scissors (S), Lizard (L), Spock (K) or e(x)it: ")
    if choice == "x":
        break

    comp = random.choice(list(OPTIONS))

    game = play(choice,comp)
    if game is None:
        print(f"Its a tie, you both chose {OPTIONS[choice].capitalize()}")
    elif game == False:
        print(f"You lost! {OPTIONS[comp].capitalize()} beats {OPTIONS[choice].capitalize()}")
    else:
        print(f"You won! {OPTIONS[choice].capitalize()} beats {OPTIONS[comp].capitalize()}")
