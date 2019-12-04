import pathlib

# Scenario 1 - path is not a valid file path
# Passes the given path to to the pathlib.Path function
test_file_path = pathlib.Path('./standard_library/')

# Tests whether the given path is a file
is_file = test_file_path.is_file()

# Prints False since the pathway is a not a valid file
print(f"{is_file = }")


# Scenario 2 - path is a valid file path
# This time, pass a valid file path to the pathlib.Path function
test_file_path = pathlib.Path('./standard_library/mod_pathlib/isfile.py')

# Tests whether the given path is a file
is_file = test_file_path.is_file()

# Prints True since the pathway is a valid file
print(f"{is_file = }")
