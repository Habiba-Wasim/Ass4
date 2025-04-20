def subtract_seven(num):
    # Subtract 7 from the number and return the result
    num = num - 7
    return num

def main():
    # Initialize num with 7
    num = 7
    # Call the subtract_seven function to subtract 7
    num = subtract_seven(num)
    # Print the result, it should be 0
    print("this should be zero: ", num)

# This provided line is required to call the main() function
if __name__ == '__main__':
    main()
