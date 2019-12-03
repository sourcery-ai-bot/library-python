from itertools import accumulate
import operator

nums = range(1, 101)

# The results from 1 to 100 cumulatively added
results_added = accumulate(nums, operator.add)
print(results_added)

for item in results_added:
    print(item)

# The results from 1 to 100 cumulatively subtracted
results_subtracted= accumulate(nums, operator.sub)
print(results_subtracted)

for item in results_subtracted:
    print(item)
