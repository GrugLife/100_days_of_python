import random
import string

letters = string.ascii_letters
numbers = string.digits
symbols = "!@#$%^&*()"

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

pw_letters = random.choices(letters, k=nr_letters)
pw_numbers = random.choices(numbers, k=nr_numbers)
pw_symbols = random.choices(symbols, k=nr_symbols)

password = pw_letters + pw_symbols + pw_numbers
random.shuffle(password)
password = "".join(password)
print(f"Your password is: {password}")
