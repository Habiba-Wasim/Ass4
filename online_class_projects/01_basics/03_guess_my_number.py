import random

def main():
    print("I am thinking of a number between 1 and 99...")
    
    # Generate the secret number at random!
    secret_number = random.randint(1, 99)
    
    # Initialize the number of attempts
    attempts = 0
    
    # Get user's guess
    guess = int(input("Enter a guess: "))
    
    # Loop until the user guesses the correct number
    while guess != secret_number:
        attempts += 1
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        
        # Ask for a new guess if incorrect
        guess = int(input("Enter a new guess: "))
    
    # Print success message when correct guess is made
    attempts += 1
    print(f"Congrats! The number was: {secret_number}")
    print(f"It took you {attempts} attempts to guess the number.")
    
if __name__ == '__main__':
    main()
