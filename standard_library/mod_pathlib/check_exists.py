import pathlib

# Scenario 1: argument given to Path is a directory
# Passes the given directory to to the pathlib.Path function
example_directory_path = pathlib.Path('./standard_library/')

# Tests whether the given path is either a directory or file
does_exist = example_directory_path.exists()

# Prints True since the pathway exists as either a directory or a file
# Misspell the directory and False will be printed instead
print(f"{does_exist = }")


# Scenario 2: argument given to Path is a file
# Passes the given filename to to the pathlib.Path function
example_file_path = pathlib.Path('.env')

# Tests whether the given path is either a directory or file
does_exist = example_file_path.exists()

# Prints True since the pathway exists as either a directory or a file
# Misspell the directory and False will be printed instead
print(f"{does_exist = }")
