import hashlib  # Importing the hashlib module for hashing operations

# Welcome message for the user
def welcome():
    print("Welcome to the hash checker!\n")
    print(""" 
                 _         ___ _               _             
  /\  /\__ _ ___| |__     / __\ |__   ___  ___| | _____ _ __ 
 / /_/ / _` / __| '_ \   / /  | '_ \ / _ \/ __| |/ / _ \ '__|
/ __  / (_| \__ \ | | | / /___| | | |  __/ (__|   <  __/ |   
\/ /_/ \__,_|___/_| |_| \____/|_| |_|\___|\___|_|\_\___|_|   
                                                          
    """)

# Function to get user inputs: file path, hashing algorithm, and original hash
def get_inputs():
    path = input("Please enter the file path: ")
    hash_type = input("Please specify the hashing algorithm (MD5, SHA256, or SHA384): ")
    original_hash = input("Please enter the original hash: ")
    return path, hash_type.upper(), original_hash

# Function to open and read file content
def read_file(path): 
    try:
        with open(path, "rb") as file:  # Opening the file in binary mode
            content = file.read()  # Reading the content of the file
            return content  # Returning the content of the file
    except FileNotFoundError:
        print("Error: File not found.")  # Handling the case where the file is not found
        return None

# Function to hash the content based on the specified algorithm
def hash_content(hash_type, content):
    if hash_type == "MD5":  # Checking if the hash type is MD5
        return hashlib.md5(content).hexdigest()  # Hashing the content using MD5 algorithm
    elif hash_type == "SHA256":
        return hashlib.sha256(content).hexdigest()
    elif hash_type == "SHA384":
        return hashlib.sha384(content).hexdigest()
    else:
        print("Error: Invalid hash type specified.")  # Handling the case of an invalid hash type
        return None

# Function to compare the calculated hash with the original hash
def compare_hashes(calculated_hash, original_hash):    
    if calculated_hash == original_hash:
        print("Hashes match. This is the legitimate file.")
    else:
        print("Hashes do not match.")

# Main function to execute the program
def main():
    welcome()  # Displaying the welcome message
    path, hash_type, original_hash = get_inputs()  # Getting user inputs
    content = read_file(path)  # Reading the file content
    if content:  # Checking if the content is not None
        calculated_hash = hash_content(hash_type, content)  # Hashing the content
        if calculated_hash:  # Checking if the calculated hash is not None
            compare_hashes(calculated_hash, original_hash)  # Comparing the hashes

if __name__ == "__main__":
    main()  # Executing the main function if the script is run directly

