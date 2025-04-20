# # Topic: Project4

# # Rock, Paper, Scissors Game

# import random

# #game choices
# choices = ["rock", "paper", "scissors"]

# #player choice
# player_choice = input("Enter rock, paper, or scissors:").lower()

# #computer choice
# computer_choice = random.choice(choices)

# #winner decision 
# if player_choice == computer_choice:
#     print(f"dono ka choice {player_choice} tha. Its a tie!")
    
# elif player_choice == "rock" and computer_choice == "scissors":
#     print(f"Player wins! {player_choice} beats {computer_choice}.")
    
# elif player_choice == "paper" and computer_choice == "rock":
#     print(f"Player wins! {player_choice} beats {computer_choice}.")
    
# elif player_choice == "scissors" and computer_choice == "paper":
#     print(f"Player wins! {player_choice} beats {computer_choice}.")        















# Topic: Project4

# Rock, Paper, Scissors Game

import random

# Game choices
choices = ["rock", "paper", "scissors"]

# Player choice
player_choice = input("Enter rock, paper, or scissors: ").lower()

# Validate input
if player_choice not in choices:
    print("Invalid input! Please enter rock, paper, or scissors.")
else:
    # Computer choice
    computer_choice = random.choice(choices)

    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}\n")

    # Winner decision
    if player_choice == computer_choice:
        print(f"Both chose {player_choice}. It's a tie!")
        
    elif player_choice == "rock" and computer_choice == "scissors":
        print("Player wins! Rock beats scissors.")
        
    elif player_choice == "paper" and computer_choice == "rock":
        print("Player wins! Paper beats rock.")
        
    elif player_choice == "scissors" and computer_choice == "paper":
        print("Player wins! Scissors beats paper.")
    
    else:
        print(f"Computer wins! {computer_choice} beats {player_choice}.")
