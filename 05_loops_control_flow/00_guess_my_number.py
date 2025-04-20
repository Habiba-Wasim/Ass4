import random

def main():
    # Generate a random number between 1 and 99 (inclusive)
    secret_number = random.randint(1, 99)
    
    print("I am thinking of a number between 1 and 99...")

    # Prompt user for their first guess
    guess = int(input("Enter a guess: "))
    
    # Loop until the user guesses correctly
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        
        print()  # Just a clean spacing line
        guess = int(input("Enter a new guess: "))
    
    # Congratulate the user
    print(f"Congrats! The number was: {secret_number}")

# Required Python boilerplate to run the main function
if __name__ == '__main__':
    main()
