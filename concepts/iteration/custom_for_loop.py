""" Here is an example of a custom for loop that demonstrates how a loop
    works in Python. It demonstrates the concepts of iterators and iterables. """

def my_for_loop1(iterable, func):
    """ Emulates a for loop accepting an iterable object and a function
        object as its arguments """
    iterator = iter(iterable)
    """ The while True enables the iterator to keep iterating until there
        are iterators to continue to work with. Once the loop goes beyond the
        final iterator, it tries to run the next function, however throws an
        exception and therefore the except statement throws the StopIteration
        exception and the 'break' keyword breaks out of the while loop allowing
        for the error to pass silently. """
    while True:
        try:
            thing = next(iterator)
        except StopIteration:
            break
        else:
            func(thing)

# Demonstrate this by calling the function using several methods

def square(num):
    print(num * num)


# Strings are iterable, therefore the elements of the string can be iterated upon
my_for_loop1("The cat sat on the mat", print)

# A list is naturally iterable, therefore its elements can be iterated upon
my_for_loop1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], square)
