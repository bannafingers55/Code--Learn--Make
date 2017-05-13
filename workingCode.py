import random  # imports a module called random

choice = input("Pick either, Rock, Paper or Scissors ")
"""asks for an input of either
rock, paper or scissors"""

if choice == "Rock" or choice == "rock":
    print("You chose Rock")
    numberChoice = 1

# if you chose rock say 'you chose rock'

elif choice == "Paper" or choice == "paper":
    print("You chose Paper")
    numberChoice = 2

# if you chose paper say 'you chose paper'

elif choice == "Scissors" or choice == "scissors":
    print("You chose Scissors")
    numberChoice = 3

# if you chose scissors say 'you chose scissors'
else:

    print("Not a valid option")
