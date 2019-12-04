import pathlib

# Passes the given path to to the pathlib.Path function
example_directory_path = pathlib.Path('./standard_library/')

# Tests whether the given path is a directory
is_directory = example_directory_path.is_dir()

# Prints True since the pathway is a valid directory
# Misspell the directory and False will be printed instead
print(f"{is_directory = }")
