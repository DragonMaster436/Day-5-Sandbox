# fruits = ["apple", "Peach", "Pear"]
# for test in fruits:
#     print(test)

# max_number = 0
# fruits = [1, 2, 3]
# for test in fruits:
#     if test > max_number:
#         max_number = test

# print(max_number)
# total = 0
# the 3 is the step 
# for i in range(1, 101, 3):
#     print(i)
#     total += i
    
# print(total)

import random

# Lists of letters, numbers, and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Create lists for each character type
wanted_numbers = random.sample(numbers, nr_numbers)
wanted_symbols = random.sample(symbols, nr_symbols)
wanted_letters = random.sample(letters, nr_letters)

# Concatenate the character lists
joined_total = wanted_letters + wanted_numbers + wanted_symbols

# Shuffle the characters to randomize their order
random.shuffle(joined_total)

# Convert the shuffled list into a string
password = "".join(joined_total)
print(password)
