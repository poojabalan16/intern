import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User input for password length
length = int(input("Enter password length: "))

# Generate and display the password
password = generate_password(length)
print(f"Generated Password: {password}")
