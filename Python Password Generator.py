import random

# Defining all characters for the variables in use.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level.  This gives you the characters in order of how it is asked.

#First define a placeholder for your password
password = ""

#randomize the letters
for character in range(1, nr_letters + 1):
    random_character = random.choice(letters)
    password = password + random_character 

#randomize the symbols
for character in range(1, nr_symbols + 1):
    random_character = random.choice(symbols)
    password += random_character

#randomize the numbers
for character in range(1, nr_numbers + 1):
    random_character = random.choice(numbers)
    password += random_character

#Code for scrambling the character layout for password
password ="".join(random.sample(password, len(password)))

print(f"Your password is {password}")
