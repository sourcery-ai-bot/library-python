set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set2 = {3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

# Not found in set 1 - like a VLOOKUP
not_in_set1 = set1.difference(set2)
print(not_in_set1)

# Not found in set 2 - like a VLOOKUP
not_in_set2 = set2.difference(set1)
print(not_in_set2)

union_vals = set1.union(set2)
print(union_vals)

intersection_vals = set1.intersection(set2)
print(intersection_vals)

issubset_vals = intersection_vals.issubset(union_vals)
print(issubset_vals)

issuperset_vals = union_vals.issuperset(intersection_vals)
print(issuperset_vals)
