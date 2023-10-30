import random
import string

def generate_password(length=12):
    # Define character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_characters = '!@#$%^&*()_-+=<>?/'

    # Combine character sets
    all_characters = uppercase + lowercase + digits + special_characters

    # Ensure at least one character from each set
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Generate the rest of the password
    password.extend(random.choice(all_characters) for _ in range(length - 4))

    # Shuffle the password characters
    random.shuffle(password)

    return ''.join(password)

# Example: Generate a 16-character password
password = generate_password(16)
print(password)
