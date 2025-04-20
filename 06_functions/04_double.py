def double(num: int):
    # Return the result of multiplying num by 2
    return num * 2

def main():
    # Prompt the user to enter a number
    num = int(input("Enter a number: "))
    
    # Call the double function and store the result
    num_times_2 = double(num)
    
    # Print the result
    print("Double that is", num_times_2)

# Call the main function when the script is executed
if __name__ == '__main__':
    main()
