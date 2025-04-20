def main():
    # Get the numbers we want to divide
    dividend = int(input("Please enter an integer to be divided: "))
    divisor = int(input("Please enter an integer to divide by: "))

    # Perform integer division and get the remainder
    quotient = dividend // divisor  # Integer division
    remainder = dividend % divisor  # Remainder (modulo)
    
    # Output the result
    print(f"The result of this division is {quotient} with a remainder of {remainder}")


# This line ensures the main function is called if the script is executed
if __name__ == '__main__':
    main()
