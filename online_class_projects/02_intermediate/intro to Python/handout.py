# Define the constants for each planet's gravity as a percentage of Earth's gravity
planetary_gravity = {
    "Mercury": 37.6,
    "Venus": 88.9,
    "Mars": 37.8,
    "Jupiter": 236.0,
    "Saturn": 108.1,
    "Uranus": 81.5,
    "Neptune": 114.0
}

def main():
    # Milestone 1: Get the user's weight on Earth
    earth_weight = float(input("Enter a weight on Earth: "))

    # Milestone 2: Get the user's choice of planet
    planet = input("Enter a planet: ")

    # Check if the planet is in the dictionary
    if planet in planetary_gravity:
        # Get the gravity percentage for the selected planet
        gravity_percentage = planetary_gravity[planet]
        
        # Calculate the weight on the selected planet
        planet_weight = (earth_weight * gravity_percentage) / 100
        
        # Print the result rounded to 2 decimal places
        print(f"The equivalent weight on {planet}: {round(planet_weight, 2)}")
    else:
        # Handle invalid planet input
        print("Invalid planet name. Please enter a valid planet from the list.")

# Entry point for the program
if __name__ == "__main__":
    main()
