def main():
    # Get the year to check from the user
    year = int(input('Please input a year: '))

    # Apply leap year logic
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("That's a leap year!")
            else:
                print("That's not a leap year.")
        else:
            print("That's a leap year!")
    else:
        print("That's not a leap year.")

# Required line to call the main function
if __name__ == '__main__':
    main()
