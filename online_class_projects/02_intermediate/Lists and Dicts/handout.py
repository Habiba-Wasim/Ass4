def access_element(lst, index):
    """Function to access and return the element at the specified index."""
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return "Index out of range!"

def modify_element(lst, index, new_value):
    """Function to modify the element at the specified index."""
    if 0 <= index < len(lst):
        lst[index] = new_value
        return lst
    else:
        return "Index out of range!"

def slice_list(lst, start, end):
    """Function to slice the list from start to end index (exclusive)."""
    if 0 <= start < len(lst) and 0 <= end <= len(lst):
        return lst[start:end]
    else:
        return "Invalid range!"

def game():
    # Initial list with numbers and strings
    game_list = [5, "apple", 10, "banana", 3.14]
    
    print("Welcome to the Index Game!")
    print("Here is the current list:", game_list)
    
    while True:
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Quit the game")
        
        choice = input("Enter the operation number (1-4): ")
        
        if choice == "1":
            index = int(input("Enter the index to access: "))
            result = access_element(game_list, index)
            print(f"Element at index {index}: {result}")
        
        elif choice == "2":
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            result = modify_element(game_list, index, new_value)
            print("Updated list:", result)
        
        elif choice == "3":
            start = int(input("Enter the start index: "))
            end = int(input("Enter the end index: "))
            result = slice_list(game_list, start, end)
            print(f"Sliced list from {start} to {end}: {result}")
        
        elif choice == "4":
            print("Thank you for playing! Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the game
if __name__ == "__main__":
    game()
