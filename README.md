# PY-Hashing-Made-Simple
This is a repo for learning how to hash in Python using hashlib. This will include hashing passwords, comparing files for authenticity, and more.

## Python hasher 1 (hashing a file)
Define the file path: This line sets the variable `path` to the file path where the file to be hashed is located.

Open the file in binary mode: Using a `with` statement, this block of code opens the file specified by the `path` variable in binary mode (`"rb"`).

Read the contents of the file: The `read()` method reads the content of the opened file and stores it in the `content` variable.

Initialize hash objects: This section initializes three hash objects (`md5`, `sha256`, and `sha384`) using the `hashlib` module.

Update hash objects with file content: The `update()` method of each hash object is used to update the hash with the content read from the file.

Print the hash results: The hash results are printed to the console, including the name of the hash algorithm and the hexadecimal digest of the hash.

## Python hasher 3 (hashing and comparing)

Imports: The script imports the hashlib module to perform hashing operations.

Welcome Function: The welcome function displays a welcome message to the user.

Get Inputs Function: The get_inputs function prompts the user to enter the file path, hashing algorithm, and original hash, and returns these values.

Read File Function: The read_file function attempts to open and read the content of the file specified by the user. It handles the case where the file is not found.

Hash Content Function: The hash_content function hashes the content of the file based on the specified algorithm. It supports MD5, SHA256, and SHA384 hashing algorithms.

Compare Hashes Function: The compare_hashes function compares the calculated hash with the original hash provided by the user and prints whether they match or not.

Main Function: The main function orchestrates the execution of the program. It calls the welcome message function, gets user inputs, reads the file, calculates the hash, and compares it with the original hash.

Execution Block: This block ensures that the main function is executed when the script is run as the main program.
