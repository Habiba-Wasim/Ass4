def main():
    # Ask the user for a number
    curr_value = int(input("Enter a number: "))
    
    # While the current value is less than 100, keep doubling it and printing the result
    while curr_value < 100:
        curr_value = curr_value * 2  # Double the current value
        print(curr_value, end=" ")  # Print the current value on the same line, separated by space

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
