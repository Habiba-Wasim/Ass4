import math  # Import the math library to use the sqrt function

def main():
    # Get the two perpendicular side lengths from the user and cast them to floats
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))

    # Calculate the hypotenuse (BC) using the Pythagorean theorem
    bc = math.sqrt(ab**2 + ac**2)
    
    # Output the result
    print(f"The length of BC (the hypotenuse) is: {bc}")

# This line ensures the main function is called if the script is executed
if __name__ == '__main__':
    main()
