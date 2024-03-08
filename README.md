# PY-Hashing-Made-Simple
This is a repo for learning how to hash in Python using hashlib. This will include hashing passwords, comparing files for authenticity, and more.

## Python hasher 1 (hashing a file)
Define the file path: This line sets the variable `path` to the file path where the file to be hashed is located.
Open the file in binary mode: Using a `with` statement, this block of code opens the file specified by the `path` variable in binary mode (`"rb"`).
Read the contents of the file: The `read()` method reads the content of the opened file and stores it in the `content` variable.
Initialize hash objects: This section initializes three hash objects (`md5`, `sha256`, and `sha384`) using the `hashlib` module.
Update hash objects with file content: The `update()` method of each hash object is used to update the hash with the content read from the file.
Print the hash results: The hash results are printed to the console, including the name of the hash algorithm and the hexadecimal digest of the hash.
