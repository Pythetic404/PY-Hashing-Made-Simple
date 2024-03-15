import hashlib

# Function to hash the password
def check_hash(password):
    hashed_password = hashlib.sha256(password.encode())  # Hash the password using SHA256
    hashed_password_f = hashed_password.hexdigest()  # Convert the hashed password to hexadecimal
    return hashed_password_f  # Return the hashed password


# Function to create a new account
def create_account():
    good_password = False
    new_user = input("Please enter a new username: ")  # Prompt for a new username
    if new_user in accounts:  # Check if the username already exists
        while new_user in accounts:
            print("This account already exists. Please try again.")
            new_user = input("Please enter a new username: ")
    while not good_password:
        new_pass = input("Please enter a new password: ")  # Prompt for a new password
        if any(character in special_characters for character in new_pass) and any(
                character.isdigit() for character in new_pass):
            # Check if the password contains at least one special character and one digit
            print("Strong password")
            good_password = True
        else:
            print("Please add both a special character and a digit to your password.")
            good_password = False

    new_pass_hash = check_hash(new_pass)  # Hash the new password
    accounts[new_user] = new_pass_hash  # Add the new username and hashed password to the accounts dictionary
    print("Your account has been successfully created.")
    login()  # Proceed to login


# Function to log in to an existing account
def login():
    username = input("Enter your username: ")  # Prompt for the username
    password = input("Enter your password: ")  # Prompt for the password

    hashed_input = check_hash(password)  # Hash the input password

    if username in accounts:  # Check if the username exists in the accounts dictionary
        if hashed_input == accounts[username]:  # Check if the hashed input password matches the stored hash
            print("Access Granted")
            print(f"Welcome {username}")
            print("Big brother is watching")
            return
    print("Invalid username or password. Please try again.")  # Display error message if login fails
    main()  # Return to main menu


# Function to reset password for an existing account
def reset_password(username):
    new_password = input("Please enter your new password: ")  # Prompt for a new password
    hashed_new_pass = check_hash(new_password)  # Hash the new password
    accounts[username] = hashed_new_pass  # Update the password for the given username
    print("Your password has been successfully reset.")
    print(accounts[username])


accounts = {"pythetic": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"}
special_characters = "!@#$%^&*()-+?_=,<>/"

# Main function to display menu and handle user input
def main():
    print("""
  ___                 _ _   _         _       
 / _ \ _ ___ __ _____| | | | |   __ _| |__ ___
| (_) | '_\ V  V / -_) | | | |__/ _` | '_ (_-<
 \___/|_|  \_/\_/\___|_|_| |____\__,_|_.__/__/
 
                                              """)
    what_to_do = input("""Please select an option:
      1.) Log in
      2.) Create an account \n: """)
    if what_to_do == "1":
        login()
    elif what_to_do == "2":
        create_account()


main()  # Start the program execution
