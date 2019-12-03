""" The count function continues to count until an explicit instruction or
condition is met within the code. """

import itertools

counter = itertools.count(start=1)

# Counts until a thousand.
for num in counter:
    if num > 1_000:
        break
    print(num)
