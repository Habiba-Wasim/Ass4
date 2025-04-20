ADULT_AGE : int = 18  # U.S. age classification for adulthood

def is_adult(age: int):
    # If the age is greater than or equal to ADULT_AGE, return True
    if age >= ADULT_AGE:
        return True
    # Otherwise, return False
    return False

########## No need to edit code beyond this point :) ##########

def main():
    # Get the user's input and convert it to an integer
    age = int(input("How old is this person?: "))
    # Call is_adult() to check if the person is an adult
    print(is_adult(age))  # Output the result of the check

# This ensures the program runs only when executed directly, not when imported as a module
if __name__ == "__main__":
    main()
