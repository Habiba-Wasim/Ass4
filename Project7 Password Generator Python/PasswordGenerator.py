# Project 7 : Password Generator Python

import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits +  string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password 

 #user inputs
length = int(input("Enter the length of your desired password:"))
 
password = generate_password(length)
print("Your Desried Generated Passsword:" ,password)