def main():
    for i in range(10, 20):  # Loop through numbers 10 to 19 (inclusive)
        if is_odd(i):  # Check if the number is odd
            print(f"{i} odd")  # Print number and "odd"
        else:
            print(f"{i} even")  # Print number and "even"

def is_odd(value: int):
    """
    Checks to see if a value is odd. If it is, returns True.
    """
    remainder = value % 2  # 0 if value is divisible by 2, 1 if it isn't
    return remainder == 1  # Returns True if the number is odd (remainder = 1)

# This provided line is required at the end of the Python file to call the main() function
if __name__ == '__main__':
    main()
