import random

# Probability of returning True in done function
DONE_LIKELIHOOD = 0.3  # 30% chance to stop

def chaotic_counting():
    """ Counts from 1 to 10, but stops early if done() returns True. """
    for i in range(10):
        curr_num = i + 1
        if done():  # Check if we should stop early
            return  # Ends the function and returns control to main()
        print(curr_num)

def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()  # Call the chaotic counting function
    print("I'm done")  # Prints when chaotic_counting() finishes

if __name__ == "__main__":
    main()
