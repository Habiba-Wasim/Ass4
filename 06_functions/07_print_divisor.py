def print_divisors(num: int):
    """
    Prints all divisors of the number `num`.
    """
    print(f"Here are the divisors of {num}")
    # Loop through all numbers from 1 to num inclusive
    for i in range(1, num + 1):
        if num % i == 0:  # Check if i is a divisor of num
            print(i)

def main():
    num = int(input("Enter a number: "))  # Get user input
    print_divisors(num)  # Call the print_divisors function with the input number

if __name__ == '__main__':
    main()
