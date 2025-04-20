import random

# Number of sides on each die
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total.
    Each die roll is a random integer between 1 and NUM_SIDES.
    """
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    total: int = die1 + die2
    print(f"Roll results: Die 1 = {die1}, Die 2 = {die2}, Total = {total}")

def main():
    die1: int = 10  # This is the local variable inside main, separate from roll_dice() function
    print(f"die1 in main() starts as: {die1}")

    # Simulate rolling the dice 3 times
    roll_dice()
    roll_dice()
    roll_dice()

    # This prints the value of die1 inside main()
    print(f"die1 in main() is still: {die1}")

# This line ensures the main() function is called when the file is run
if __name__ == '__main__':
    main()
