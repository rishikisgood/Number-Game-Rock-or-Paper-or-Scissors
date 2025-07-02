import random

while True:
    user_action=input("Enter a choicr(ROCK, PAPER OR SCISSORS):")
    possible_actions=["ROCK", "PAPER", "SCISSORS"]
    computer_actions= random.choice(possible_actions)
    print(f"\nYou chose{user_action}, computer chose {computer_actions}.\n")
    if computer_actions == computer_actions:
        print(f"Both players selected {user_action}. It is a tie!")
    elif user_action =="ROCK":
        if computer_actions == "SCISSORS":
            print("Rock Smashes the Scissors! You Win!!!")
        else:
            print("Paper Covers the Rock! You lose!!!")
    elif user_action =="PAPER":
        if computer_actions == "ROCK":
            print("Paper covers Rock! You Win!!!")
        else:
            print("Scissors Cuts the paper! You lose!!!")
    elif user_action =="SCISSORS":
        if computer_actions == "PAPER":
            print("Scissors cuts Paper! You Win!!!")
        else:
            print("Rock Smashes the Scissors! You lose!!!")
    play_again=input("Play again? (y/n) ")
    if play_again != "y":
        break