PETURKSBOUIPO_AGE: int = 16
STANLAU_AGE: int = 25
MAYENGUA_AGE: int = 48

def main():
    # Ask for the user's age
    user_age = int(input("How old are you? "))

    # Check and print voting eligibility for each country
    if user_age >= PETURKSBOUIPO_AGE:
        print("You can vote in Peturksbouipo where the voting age is", PETURKSBOUIPO_AGE, ".")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is", PETURKSBOUIPO_AGE, ".")

    if user_age >= STANLAU_AGE:
        print("You can vote in Stanlau where the voting age is", STANLAU_AGE, ".")
    else:
        print("You cannot vote in Stanlau where the voting age is", STANLAU_AGE, ".")

    if user_age >= MAYENGUA_AGE:
        print("You can vote in Mayengua where the voting age is", MAYENGUA_AGE, ".")
    else:
        print("You cannot vote in Mayengua where the voting age is", MAYENGUA_AGE, ".")

# Run the program
if __name__ == '__main__':
    main()
