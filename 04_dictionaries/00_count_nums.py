def get_user_numbers():
    """
    Create an empty list.
    Ask the user to input numbers and store them in a list. 
    Once they enter a blank line, break out of the loop and return the list.
    """
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")
        
        # If the user enters a blank line, break out of the loop
        if user_input == "":
            break
        
        # Convert the input to an integer and add it to the list
        num = int(user_input)
        user_numbers.append(num)
    
    return user_numbers

def count_nums(num_lst):
    """
    Count how many times each number appears in the list using a dictionary.
    """
    num_dict = {}
    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    return num_dict

def print_counts(num_dict):
    """
    Print the number of times each number appears.
    """
    for num in num_dict:
        print(str(num) + " appears " + str(num_dict[num]) + " times.")

def main():
    """
    Main function to tie everything together.
    """
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)

# Boilerplate to run main
if __name__ == '__main__':
    main()
