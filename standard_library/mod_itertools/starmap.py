import itertools

# Pairs the base number and the exponent as pairs of tuples
squares_pairs = [(1, 2), (2, 2), (3, 2), (4, 2), (5, 2)]

# Creates a starmap iterator where the pow function is mapped to the square_pairs
squares_iterator = itertools.starmap(pow, squares_pairs)

# Casts the starmap iterator to a list
squares_list = list(squares_iterator)
print(squares_list)
