import math

# Produce a list from 1 to 10 for each of the radii to be processed
radii = [num for num in range(1, 11)]

# Set a function that calculates the area (to 2dp) when given its radius
area_calc = lambda r: round(math.pi * r ** 2, 2)

# Creates an iterator that maps together each of the radii to their respective calculated areas
areas = map(area_calc, radii)

# Casts the 'areas' iterator to a list
areas = list(areas)

print(areas)

""" Continues the example given in lambdas_with_map.py """

import statistics

# Calculate the average of the areas
avg = statistics.mean(areas)
print(f"{'Average:'} {round(avg, 2)}")

# Create a filter iterator that only shows the items above the average
filtered = filter(lambda num: num > avg, areas)

# Casts the 'filtered' iterator to a list
filtered = list(filtered)

print(filtered)
