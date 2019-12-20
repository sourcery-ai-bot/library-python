""" Below are some highly contrived code examples where outer functions are
    defined to be used as decorators augmenting the functionality of the
    calling function. Of course, in reality, these features are already
    present using certain functions within the standard Python library. """

# This version only accepts one argument
def shout(fn):
    def wrapper(name):
        return fn(name).upper()
    return wrapper

# This version works with any number of args
def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper


def reverse_str(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)[::-1]
    return wrapper


@reverse_str
def greet(name):
    return f"Hi, my name is {name}."


@shout
def order(main, side):
    return f"Hi, I'd like the {main}, with a side of {side}, please."


@shout
def lol():
    return "lol"

print(greet("Wayne"))
print(order(main="burger", side="fries"))
print(lol())
