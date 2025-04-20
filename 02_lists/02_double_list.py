def main():
    numbers: list[int] = [1, 2, 3, 4]  # Create a list of numbers

    for i in range(len(numbers)):  # Loop through the indices of the list
        elem_at_index = numbers[i]  # Get the element at index i in the numbers list
        numbers[i] = elem_at_index * 2  # Set the element at index i to be doubled

    print(numbers)  # Print the modified list after doubling the elements

if __name__ == '__main__':
    main()  # Call the main function









# Alternative Approach Using List Comprehension:

# def main():
#     numbers: list[int] = [1, 2, 3, 4]  # Create a list of numbers
#     numbers = [num * 2 for num in numbers]  # Double each element using list comprehension
#     print(numbers)  # Print the doubled list

# if __name__ == '__main__':
#     main()  # Call the main function
