# rock paper scissors
# receive input for player's choice
# generate computer's choice from random
# check the choices to determine the winner

import random

def pcChoice():
    player = input("Enter your choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer = random.choice(options)
    choices = {"player": player,
                "computer": computer
                }
    
    return choices

def checkResult(player, computer):
    if player == computer:
        print("The result is a tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose! Paper wins against rock.")
        elif computer == "scissors":
            print("You win! Rock wins against scissors.")
    elif player == "paper":
        if computer == "rock":
            print("You win! Paper wins against rock.")
        elif computer == "scissors":
            print("You lose! Scissors wins against paper.")
    elif player == "scissors":
        if computer == "rock":
            print("You lose! Rock wins against scissors.")
        elif computer == "paper":
            print("You win! Scissors wins against paper.")

def main():
    choices = pcChoice()
    print("You choose " + choices["player"] + " and computer choose " + choices["computer"] + ".")
    result = checkResult(choices["player"], choices["computer"])

if __name__ == "__main__":
    main()