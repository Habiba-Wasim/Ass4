def main():
    # Get the 3 side lengths of the triangle
    side1: float = float(input("What is the length of side 1? "))
    side2: float = float(input("What is the length of side 2? "))
    side3: float = float(input("What is the length of side 3? "))

    # Calculate the perimeter
    perimeter = side1 + side2 + side3

    # Print the result
    print("The perimeter of the triangle is " + str(perimeter))


# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
