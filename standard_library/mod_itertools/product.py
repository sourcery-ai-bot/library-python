import itertools
from random import randint as r

letters = ('A', 'B', 'C', 'D', 'E')
print(list(itertools.product(letters, range(1, 5))))
