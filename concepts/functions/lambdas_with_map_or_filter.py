from math import pi

radii = range(1,101)
print(range)

areas = list(map(lambda x: pi * x **2, radii))

print(areas)

values = [10, 20, 30, 40, 50]

below_val = list(filter(lambda x: x < 25, values))

print(below_val)
