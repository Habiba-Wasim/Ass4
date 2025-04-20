def add_many_numbers(numbers) -> int:
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """
    total_so_far: int = 0  # Initialize the total sum
    for number in numbers:  # Iterate through each number in the list
        total_so_far += number  # Add each number to the total sum
    return total_so_far  # Return the total sum

def main():
    # Example list of numbers
    numbers: list[int] = [1, 2, 3, 4, 5]
    sum_of_numbers: int = add_many_numbers(numbers)  # Call function to sum the numbers
    print(sum_of_numbers)  # Print out the sum

if __name__ == '__main__':
    main()  # Call main function
