from functools import wraps
from logging import INFO, basicConfig, info
import os
from random import choice
from time import gmtime, sleep, strftime

DIR_LOC = os.path.dirname(os.path.realpath(__file__))

logfile = f"{DIR_LOC}{'/display_info.log'}"

# Set the format
basicConfig(
    filename=logfile,
    level=INFO,
    format="%(message)s"
)

# Get the path of the current file
info(f"Filename: {os.path.realpath(__file__)}")

# Get the current time
info(f"Date/Time: {strftime('%d-%m-%y %H:%M:%S', gmtime())}")
info(f"\n")


def my_logger(original_function):
    basicConfig(
        filename=f"{DIR_LOC}{'/'}{original_function.__name__}.log",
        level=INFO,
        format="%(message)s"
    )

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        info(f"Ran with args: {args}, and kwargs: {kwargs}")
        return original_function(*args, **kwargs)

    return wrapper


def my_timer(original_function):
    from time import time

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = original_function(*args, **kwargs)
        time_taken = time() - start_time
        print(f"{original_function.__name__} ran in: {time_taken} sec")
        return result

    return wrapper


@my_logger
@my_timer
def display_info(name, age):
    sleep(1)
    print(f"display_info ran with arguments (name={name}, age={age})")


names = ['Wayne', 'Carrie', 'Barrie', 'Rachael']
colours = ['Royal Blue', 'Green', 'Purple', 'Sky Blue']


def make_selection(selection):
    result = []
    for num in range(1, 101):
        selection = {
            'id': num,
            'person': choice(names),
            'colour': choice(colours),
        }
        result.append(selection)
    return result

selections = make_selection(100)
info(selections)
