import random
import string

def gen_pass(length,numbers=True,special_chr=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters

    if numbers:
        characters += digits
    if special_chr:
        characters += special

    password = ""
    
    password_made = False
    has_number = False
    has_special = False

    while not password_made or len(password) < length:
        new_char = random.choice(characters)
        password += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        
        password_made = True
        if numbers:
            password_made = has_number
        if special_chr:
            password_made = password_made and has_special

    return password

l = int(input("Enter the length of the password : "))
d = input("Do you want numbers in your password [y/n] : ").lower()
s = input("Do you want special character in your password [y/n] : ").lower()

    
password = gen_pass(l,d,s)

print(password)