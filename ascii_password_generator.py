import random
import string

def generate_password(chars, length):
  # Use random.sample to randomly choose `length` characters from `chars`
  password = ''.join(random.sample(chars, length))
  return password

# Get the string of characters to use for the password
chars = input("Enter the characters to use for the password (or press enter to use all printable ASCII characters): ")

# If no characters are entered, use all printable ASCII characters
if not chars:
  chars = string.printable[:94]

# Get the length of the password
length = int(input("Enter the length of the password: "))

# Generate the password
password = generate_password(chars, length)
print(password)
