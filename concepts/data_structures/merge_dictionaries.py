# How to merge two dictionaries in Python 3.5+

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'c': 5, 'd': 6}

merged_dict = {**dict1, **dict2, **dict3}

print(merged_dict)
