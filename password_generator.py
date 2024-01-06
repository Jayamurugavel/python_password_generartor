# Random Password Generator

# Ask the user if they want to generate a password
# If the user does not, exit program
# If the user does, ask for password length
# Generate password for the user
# Print password for the user

# Import libraries
import string
import random

# List of characters in the password to be generated
characters = list(string.ascii_letters + string.digits + "!@#$%*")

# Function to generate password
def generate_password():
    password_length = int(input("How long this password should be?"))

    # Shuffle characters
    random.shuffle(characters)

    # Create empty list to input the random characters there
    password = []

    # Loop to take random characters to build pw according to pw length
    for x in range(password_length):
        password.append(random.choice(characters))

    # Shuffle it again
    random.shuffle(password)
    password = "".join(password)

    # Print final password to the user
    print(password)

option = input("Do you want to generate a password? (YES/NO)")

option_1 = "yes"
option_2 = "no"

# Lower to make user input case insensitive
if option.lower() == option_1.lower():
    generate_password()
elif option.lower() == option_2.lower():
    print("Ok, program ended.")
    quit()
else:
    print("Invalid option, please type YES or NO.")
    quit()
