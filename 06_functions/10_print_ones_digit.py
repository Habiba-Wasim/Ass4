def print_ones_digit(num):
    # The ones digit can be found by using the modulo operator
    print("The ones digit is", num % 10)

def main():
    # Prompt the user for input
    num = int(input("Enter a number: "))
    
    # Call the print_ones_digit function with the user's input
    print_ones_digit(num)

# Ensure the script runs correctly when executed
if __name__ == '__main__':
    main()
