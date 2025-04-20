def main():
    # Dictionary containing fruit prices
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }
    
    total_cost = 0
    
    # Ask the user how many of each fruit they want
    for fruit in fruits:
        price = fruits[fruit]
        amount = int(input(f"How many ({fruit}) do you want?: "))
        total_cost += price * amount
    
    # Display the total rounded to 2 decimal places
    print(f"Your total is ${round(total_cost, 2)}")

# Standard Python boilerplate
if __name__ == '__main__':
    main()
