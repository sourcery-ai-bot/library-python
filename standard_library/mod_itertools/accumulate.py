from itertools import accumulate
import operator

nums = range(1, 101, 1)

results_added = accumulate(nums, operator.add)
print(results_added)

for item in results_added:
    print(item)
