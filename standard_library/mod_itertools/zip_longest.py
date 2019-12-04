import itertools

# Create a numbered list from 1 - 10
longest = range(1, 11)

# Create a series of numbers with 5 elements
data1 = [100, 200, 300, 400, 500]
data2 = [1000, 2000, 3000, 4000, 5000, 6000]

# Zips together the data1 list, data2 list with the 'longest' list (10 elements)
# The backfilling of absent elements is filled with 'None' by default
# As illustrated below, the fillvalue argument can be given to backfill with something else
zipped = itertools.zip_longest(longest, data1, data2, fillvalue='N/A')

# Cast the 'zipped' zip_longest iterator as a list
zipped_list = list(zipped)
print(zipped_list)
