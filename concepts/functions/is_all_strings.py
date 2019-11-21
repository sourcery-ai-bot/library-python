# This function checks to see whether all of the elements being passed in are string

# Method 1: List Comprehension
def is_all_strings(my_list: list) -> bool:
    return all([type(element) == str for element in my_list])


my_list = ['This', 'That', 'The Other']
print(is_all_strings(my_list))


# Method 2: Generator Expression
def is_all_strings(my_list: list) -> bool:
    return all(type(element) == str for element in my_list)


my_list = ['This', 'That', 'The Other']
print(is_all_strings(my_list))


if __name__ == "__main__":
    pass