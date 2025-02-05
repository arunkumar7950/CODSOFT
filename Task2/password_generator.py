import random
import string

def generate_password():
    length = input("Enter the desired password length (above 8): ")
    if length.isdigit():
        length = int(length)
        if length >= 8:
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            print("Your generated password is:", password)
        else:
            print("Password length must be at least 8.")
    else:
        print("Please enter a valid number for the password length.")

generate_password()
