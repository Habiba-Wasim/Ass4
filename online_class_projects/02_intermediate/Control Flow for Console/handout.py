import random

# Total rounds
NUM_ROUNDS = 5

def main():
    score = 0
    
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    # Loop for multiple rounds
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        
        # Generate random numbers for the user and the computer
        computer_number = random.randint(1, 100)
        user_number = random.randint(1, 100)
        
        print(f"Your number is {user_number}")
        
        # Get user input for the guess
        guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
        
        # Check if the guess is correct
        if guess == "higher" and user_number > computer_number:
            print("You were right!")
            score += 1
        elif guess == "lower" and user_number < computer_number:
            print("You were right!")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        
        print(f"Your score is now {score}\n")
    
    print("Thanks for playing!")
    
    # Print ending message based on score
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

# Entry point of the program
if __name__ == "__main__":
    main()
