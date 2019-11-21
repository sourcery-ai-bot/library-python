# Function that squares each of the values in the list passed
def square_numbers(nums: list):
    for num in nums:
        yield (num ** 2)


my_nums = square_numbers([1, 2, 3, 4, 5])

# Prints generator object
print(my_nums)

# This is the same as the previous function however is a generator expression
my_nums = (num ** 2 for num in [1, 2, 3, 4, 5])

# Prints list of my_nums by casting the generator object to a list
print(list(my_nums))

# my_nums is a generator object where the generator has been exhausted
print(type(my_nums))

# Nothing prints the terminal as the my_nums generator has been exhausted
for num in my_nums:
    print(num)
