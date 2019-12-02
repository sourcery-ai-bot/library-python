# Custom intersection function
# In practice, this problem is best solved using the intersection method
# within Python's sets
def intersection(list1, list2):
    return [value for value in list1 if value in list2]

in_both_lists_list = intersection([1, 2, 3], [2, 3, 4])
print(f"{in_both_lists_list = }")
