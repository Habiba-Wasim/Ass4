# Constant for the speed of light in m/s
C = 299792458  # Speed of light in meters per second

def main():
    # Prompt the user to enter mass in kilograms
    mass_in_kg = float(input("Enter kilos of mass: "))

    # Calculate energy using Einstein's mass-energy equivalence formula: E = m * c^2
    energy_in_joules = mass_in_kg * (C ** 2)

    # Display the results
    print("e = m * C^2...")
    print(f"m = {mass_in_kg} kg")
    print(f"C = {C} m/s")
    print(f"{energy_in_joules} joules of energy!")

# Call the main function if this script is run
if __name__ == '__main__':
    main()
