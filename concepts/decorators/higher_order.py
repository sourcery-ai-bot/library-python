# We can pass functions as arguments to other functions


def sum(num, function):
    total = 0
    for num in range(1, num + 1):
        total += function(num)
    return total


def square(num):
    return num ** 2


def cube(num):
    return num * 3


print(sum(3, cube))
print(sum(3, square))
