#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

try: 
  nr_letters = int(input("How many letters would you like in your password?\n"))
  nr_symbols = int(input(f"How many symbols would you like?\n"))
  nr_numbers = int(input(f"How many numbers would you like?\n"))
except ValueError:
  print("Invalid input. Please enter a valid number.")
else:
  # Random password for letters
  password = ""
  
  for letter in range(nr_letters):
    password += random.choice(letters)
  
  
  # Random password for symbols
  for symbol in range(nr_symbols):
    password += random.choice(symbols)
  
  # Random password for numbers 
  for number in range(nr_numbers):
    password += random.choice(numbers)
  
  #Hard Level - Order of characters randomised:
  #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
  password = list(password)
  shuffle_result = random.shuffle(password)
  final_result = "".join(password)
  
  print(f"your generated password is: {final_result}")
