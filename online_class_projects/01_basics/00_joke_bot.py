PROMPT = "What do you want? "
JOKE = "Here is a joke for you! Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
SORRY = "Sorry I only tell jokes."

def main():
    # Ask the user what they want
    user_input = input(PROMPT).strip()  # Take user input and remove extra spaces

    # Check if the input is 'Joke'
    if user_input == "Joke":
        print(JOKE)  # Print the joke if the input is 'Joke'
    else:
        print(SORRY)  # Print the sorry message for anything else

# This ensures the main function is executed when the script runs
if __name__ == '__main__':
    main()
