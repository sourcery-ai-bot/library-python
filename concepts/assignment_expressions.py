"""
Assignment expressions was added to Python in version 3.8. This is the
example given within the docs.
"""

inputs = list()
while (current := input('Type something:')) != 'quit':
    inputs.append(current)
    print(inputs)
