import hashlib  # This module is used to create hashes.

# Define the file path.
path = r"C:\Users\Pythetic\Pictures\Bob_ross.jpg"

# Open the file in binary mode.
with open(path, "rb") as open_file:
    # Read the contents of the file.
    content = open_file.read()

    # Initialize hash objects. We can choose from different hash types.
    md5 = hashlib.md5()
    sha256 = hashlib.sha256()
    sha384 = hashlib.sha3_384()

    # Update hash objects with file content. This allows us to hash the file itself.
    md5.update(content)
    sha256.update(content)
    sha384.update(content)

    # Print the hash results. This is done in a nice layout but can also be done with just print(md5.hexdigest()).
    print("Result")
    print("{}: {}".format(md5.name, md5.hexdigest()))
    print("{}: {}".format(sha256.name, sha256.hexdigest()))
    print("{}: {}".format(sha384.name, sha384.hexdigest()))

