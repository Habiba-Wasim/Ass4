def get_last_element(lst):
    """
    Prints the last element of the provided list.
    """
    # Option 1: using length - 1
    print(lst[len(lst) - 1])

    # Option 2 (also works, cleaner)
    # print(lst[-1])

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
    get_last_element(lst)

# Required to run the program
if __name__ == '__main__':
    main()
