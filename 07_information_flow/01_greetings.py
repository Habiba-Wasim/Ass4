def greet(name):
    # This function takes a name and returns a greeting string
    return "Greetings " + name + "!"

def main():
    # Get the user's name using input
    name = input("What's your name? ")
    # Call the greet function with the user's name and print the result
    print(greet(name))

# This line ensures that the main function is called only when this file is executed directly
if __name__ == '__main__':
    main()
