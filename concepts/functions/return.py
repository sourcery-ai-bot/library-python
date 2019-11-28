def generate_evens1():
    result = []
    for number in range(2, 50, 2):
        result.append(number)
    return result

list_evens = generate_evens1()
print(f'Generate Evens 1 Function: {list_evens}')


# The function itself can also be written as a list comprehension.
def generate_evens2():
    result = [x for x in range(2, 50, 2)]
    return result

list_evens = generate_evens2()
print(list_evens)


# Another variant of the function can be written using modulo arithmetic.
def generate_evens3():
    result = []
    for number in range(2, 50, 2):
        if number % 2 == 0:
            result.append(number)
    return result

list_evens = generate_evens3()
print(list_evens)