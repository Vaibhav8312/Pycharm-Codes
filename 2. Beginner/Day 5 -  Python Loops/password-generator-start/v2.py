# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

rand_letters = random.sample(letters, nr_letters)
rand_numbers = random.sample(numbers, nr_numbers)
rand_symbols = random.sample(symbols, nr_symbols)
password = rand_letters + rand_numbers + rand_symbols

length = (len(password))

randomized_password = random.sample(password, length)
string = ''.join(randomized_password)

print(string)

########################################################################
# A approach with choice method

pw_letters = ''.join(random.choices(letters, k=nr_letters))
pw_symbols = ''.join(random.choices(symbols, k=nr_symbols))
pw_numbers = ''.join(random.choices(numbers, k=nr_numbers))
easy_password = pw_letters + pw_symbols + pw_numbers
total = nr_letters + nr_symbols + nr_numbers
hard_password = ''.join(random.sample(easy_password, k=total))
print("Your password is: " + hard_password)

#############################################################################
# A approach with shuffle method

rand_letters = random.sample(letters, nr_letters)
rand_symbols = random.sample(numbers, nr_symbols)
rand_numbers = random.sample(symbols, nr_numbers)

rand_string = rand_letters + rand_symbols + rand_numbers
shuffle_string = random.shuffle(rand_string)
rand_string = ''.join(rand_string)

print(rand_string)

