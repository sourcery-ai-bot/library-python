"""Lambdas are anonymous functions that can be useful when calculating one
time functions. They should be used sparingly though as they can negatively
imapct the readability of the code"""

# Use a lambda to calculate 2x squared
# Notice the order of operations means that exponentiation is before multiplication
my_function = lambda x: 2 * x ** 2
print(my_function(5))

# Combine first and last names to make a full name
full = lambda first, last: first.strip().title() + " " + last.strip().title()

print(full("    Wayne   ", "LAMBERT"))


# Sort a list of random names by first name and last name
names = ['Jimmy Jo Junior', 'Jack Branning', 'Tony Tiger', 'Fred Estaire',
        'Michael Jackson', 'Jamie Adams']
print(f'Original Names List: {names}')
names.sort()
print(f'Sorted by First Name: {names}')
names.sort(key=lambda name: name.split(" ")[-1].lower())
print(f'Sorted by Last Name: {names}')

# Let's make a quadratic function using a lambda expression
def build_quadratic_function(a, b, c):
    return lambda x: a * x ** 2 + b * x + c

# Where x = 2, the quadratic function resolves to be 13
# Although this is a one liner, it is better to write this using more than one
# line so that it is more readable and easier to maintain
print(build_quadratic_function(3,0,1)(2))
