# Project 3 : Guess The Number By (User)
# Instructor: Habiba

import random
print("Guess the number between 1 to 100!")

# Generate random number
number = random.randint(1, 100)

while True:
    guess = int(input("Enter your guess number:"))
    if guess < number:
        print("To Low Number!")
    elif guess > number:
        print("To High Number!")
    else:
        print("Congratulations! You Got It Right!")
        break    