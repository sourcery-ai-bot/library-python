""" The count function continues to count until an explicit instruction or
condition is met within the code. """

import itertools

# Zip the relevant numbers to each of the months within a months list
# Notice the 'start' parameter can be used as an optional argument.
# The counting would otherwise start at 0
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

month_pairings = list(zip(itertools.count(start=1), months))
print(month_pairings)
