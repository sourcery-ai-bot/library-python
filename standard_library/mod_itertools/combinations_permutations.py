import itertools
from random import randint as r

letters = ("A", "B", "C", "D", "E")

# Returns 120 permutations since 5 letters means there are 5! permutations
print(len(list(itertools.permutations(letters))))

# Choose 6 lottery numbers at random
for i in range(1, 7):
    num = [r(1, 59)]
    if num in num:
        num = r(1, 59)
    print(num)


""" Combinations are where the order does matter and permutations are where
the order does not matter. This therefore means that there will be more
permutations than there are combinations. """

my_combinations = list(itertools.combinations(letters, 5))
print(my_combinations)

my_permutations = list(itertools.permutations(letters, 5))
print(my_permutations)
