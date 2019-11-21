from get_month_name_dictionary import get_month_name

month_name = get_month_name(month_num=9)
print(month_name)


# When defining a function with default values, the parameters with default
# values must be the ones at the end


def about(name, age, likes="Python"):
    sentence = f"Meet {name}! They are {age} years old and they like {likes}"
    return sentence

about(age=23, name="Jack", likes="football")

# Returns the measurements of a circle into a dictionary object
from math import pi

def get_circle_measurements(radius: float) -> float:
    measurements = {
        "radius": radius,
        "diameter": 2 * radius,
        "circumference": round(pi * radius * 2),
        "area": round(pi * radius ** 2)
        }
    return measurements

# Assigns the dictionary values to d
d = get_circle_measurements(5)
print(d)


# Creates a text string providing information about the circle dimensions
circle_dimensions = f"""
(The radius of the circle is {d["radius"]}. The diameter
is {d["diameter"]}. Its circumference is {d["circumference"]} and its area is
{d["area"]}.)
"""
print(circle_dimensions)

""" Packing can be useful to make flexible functions. This is because any
number of arguments can be supplied to the function because the numbers are
unpacked into a tuple. The tuple's elements can then be looped over to return
the desired result of the function. An example of a simple addition of 10
numbers is given below. Packing is done with args using * and unpacking is
done with kwargs using ** args means arguments and kwargs means keyword arguments"""


def add_values(*nums):
    total = 0
    for i in nums:
        total += i
    return(total)

add_values(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def about(name, age, likes):
    sentence = "Meet {name}! They are {age} years old and they like {likes}"
    return sentence

dictionary = {"name": "Wayne", "age": 38, "likes": "football"}
about(**dictionary)
