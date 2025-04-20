def main():
    # Ask the user for a number and convert the input to a float
    num: float = float(input("Type a number to see its square: "))
    
    # Calculate the square (num * num or num ** 2) and print the result
    print(str(num) + " squared is " + str(num ** 2))


# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
