"""Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out
a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:
- Rock beats scissors
- Scissors beats paper
- Paper beats rock"""

import sys

print("Welcome to a game of Rock, Paper, Scissors. If at any point you'd like to quit, simply type 'quit'.")
options = ["rock", "paper", "scissors"]
user1 = input("What's your name, Player 1?\n")
user2 = input("What's your name, Player 2?\n")


def rps(input_user1, input_user2):
    if (input_user1 == "rock" and input_user2 == "scissors") or (input_user1 == "scissors" and input_user2 == "paper") or (input_user1 == "paper" and input_user2 == "rock"):
        return input_user1
    elif (input_user2 == "rock" and input_user1 == "scissors") or (input_user2 == "scissors" and input_user1 == "paper") or (input_user2 == "paper" and input_user1 == "rock"):
        return input_user2


def exit_check(user_input):
    if user_input == "quit":
        print("Thanks for playing!")
        sys.exit()


game_on = "yes"

while game_on != "no":
    user1_choice = input("What's your choice, " + user1 + "? \n").lower()
    # .lower() method turns all characters into lowercase regardless of user's spelling
    exit_check(user1_choice)

    user2_choice = input("What's your choice, " + user2 + "? \n").lower()
    exit_check(user1_choice)

    if user1_choice == user2_choice:
        print("It's a tie.")
    else:
        result = rps(user1_choice, user2_choice)
        if user1_choice == result:
            print("You won, " + user1 + "!")
        else:
            print("You won, " + user2 + "!")
    game_on = input("Do you want to play another game? yes/no \n")

# fix this:
"""What's your choice, z? 
quit
You won, z!"""

# for future reference, when attempting a different flavour of the game
"""import random
print("Welcome to a game of 'Rock, Paper, Scissors' against a bot")
user1 = input("Name your choice (rock, paper, scissors)")
choiceList = ["rock", "paper", "scissors"]
bot = random.choice(choiceList)"""


