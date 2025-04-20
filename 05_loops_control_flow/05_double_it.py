def main():
    # Prompt the user to enter a number
    curr_value = int(input("Enter a number: "))
    
    # Keep doubling the number while it's less than 100
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value, end=" ")

# Boilerplate to run main
if __name__ == '__main__':
    main()
