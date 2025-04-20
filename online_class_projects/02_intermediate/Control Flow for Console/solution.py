import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    # Keep track of the score
    your_score = 0

    # Play multiple rounds
    for i in range(NUM_ROUNDS):
        print(f"Round {i + 1}")
        
        # Generate random numbers for player and computer
        computer_num = random.randint(1, 100)
        your_num = random.randint(1, 100)
        print(f"Your number is {your_num}")

        # Get user input for the guess
        choice = input("Do you think your number is higher or lower than the computer's?: ").lower()

        # Ensure valid input
        while choice not in ["higher", "lower"]:
            choice = input("Please enter either higher or lower: ").lower()

        # Check if the guess is correct
        if (choice == "higher" and your_num > computer_num) or (choice == "lower" and your_num < computer_num):
            print(f"You were right! The computer's number was {computer_num}")
            your_score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_num}")

        print(f"Your score is now {your_score}\n")

    # End game feedback
    print("Thanks for playing!")
    print(f"Your final score is {your_score}")

    if your_score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif your_score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()
