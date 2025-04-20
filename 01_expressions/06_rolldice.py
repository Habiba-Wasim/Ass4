import random  # Import the random library to generate random numbers

# Number of sides on each die
NUM_SIDES = 6

def main():
    # Roll the dice (simulate two dice rolls)
    die1 = random.randint(1, NUM_SIDES)  # Roll the first die
    die2 = random.randint(1, NUM_SIDES)  # Roll the second die
    
    # Calculate the total of the two dice
    total = die1 + die2
    
    # Output the results
    print(f"Dice have {NUM_SIDES} sides each.")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice: {total}")

# This line ensures the main function is called when the script is run
if __name__ == '__main__':
    main()
