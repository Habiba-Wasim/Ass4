MAX_LENGTH: int = 3  # Required by the autograder

def shorten(lst):
    """
    Removes items from the end of the list until it is MAX_LENGTH items long.
    Prints each item it removes.
    """
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()  # Remove the last element
        print(last_elem)       # Print the removed element


# There is no need to edit code beyond this point

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    shorten(lst)

if __name__ == '__main__':
    main()
