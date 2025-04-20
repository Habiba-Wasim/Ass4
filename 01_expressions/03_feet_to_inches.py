# Constant for the number of inches in one foot
INCHES_IN_FOOT = 12  # There are 12 inches in one foot

def main():
    # Ask the user for the number of feet and convert the input to a float
    feet = float(input("Enter number of feet: "))
    
    # Convert feet to inches
    inches = feet * INCHES_IN_FOOT
    
    # Print the result
    print(f"That is {inches} inches!")

# Call the main function if this script is run directly
if __name__ == '__main__':
    main()
