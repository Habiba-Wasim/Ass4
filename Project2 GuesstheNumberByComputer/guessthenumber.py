# Project 2 : Guess The Number By Computer
# 1 to 100 numbers.

import random
def guess_the_number():
    """Project 2 : Guess The Number By Computer."""
    number = random.randint(1, 100)
    guesses_left = 7
    # Welcome message
    print("Welcome to Guess The Number Game!")
    print("I am thinking a number between 1 and 100.")
    
    # Loop generated
    while guesses_left > 0:
        print(f"\nYou have {guesses_left} guesses left. ")
        try:
            guess = int(input("Take a guess to another number: "))
        except ValueError:
            print("Invalid input:  Please enter a number. ")
            continue
        
        
     # Guess the secret number 
        if guess < number:
         print("Too low number. Tell another!")
        elif guess > number:
         print("Too high number. Tell another!")
        
        else:
         print(f"Congratulations! You got the correct number in {7 - guesses_left + 1} tries.")
         return
        
        guesses_left -= 1
     # Jb sb guess finished hojain gy
    print(f"\nYou run out of guess. The number was {number}.")
        
guess_the_number() 
