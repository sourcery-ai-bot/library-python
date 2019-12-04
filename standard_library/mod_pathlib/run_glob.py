import pathlib

# Passes the given path to to the pathlib.Path function
example_directory_path = pathlib.Path('./standard_library/')

# Compiles a list of .py files within the 'standard_library' directory
items = example_directory_path.glob('*/*.py')

# Iterate over the generator object to print the respective matching glob items
for item in items:
    print(item)
