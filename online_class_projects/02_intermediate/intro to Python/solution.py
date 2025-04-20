# Constants for Mars gravity
MARS_MULTIPLE = 0.378

def main():
    # Step 1: Get the Earth's weight from the user
    earth_weight_str = input('Enter a weight on Earth: ')

    # Step 2: Convert the input to a float for calculation
    earth_weight = float(earth_weight_str)

    # Step 3: Calculate the weight on Mars
    mars_weight = earth_weight * MARS_MULTIPLE

    # Step 4: Round the result to 2 decimal places
    rounded_mars_weight = round(mars_weight, 2)

    # Step 5: Output the result
    print('The equivalent weight on Mars: ' + str(rounded_mars_weight))

# Ensure the main function runs only when this script is executed directly
if __name__ == '__main__':
    main()
