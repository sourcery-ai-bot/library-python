""" Example of a function that simply converts temperatures. The important
part of the lesson is to show that multiple coniditons can be tested to ensure
that the caller's data type meets the pre-conditions required by the function.

The lesson gives an example of how to use the try, except block to test for
multiple scenarios and handle them."""

"""Create a set of custom classes to handle the execeptions. These classes
inherit from their parent classes."""

class NotFloat(TypeError):
    pass

class NotInt(TypeError):
    pass

class NotWithinRange(TypeError):
    pass


""" Now let's actaully calculate the function. """
def convert_celcius_to_fahrenheit(celsius: float) -> float:
    """ Converts degrees celsius to fahrenheit"""
    return celsius * 9 / 5 + 32


""" Capture the temperature the user enters. Test the user input!"""
temp_entered = float(input("What is the temperature in degrees celcius: "))

""" Tests that the pre-conditions for the function are met before it is called."""
try:
    if type(temp_entered) != float:
        raise NotFloat
    if type(temp_entered) != int:
        raise NotInt
    if -50 <= temp_entered <= 50:
        raise NotWithinRange
except NotFloat:
    print ("This number is not a floating point number. Error: ", str(NotFloat))
except NotInt:
    print ("This number is not an integer. Error: ", str(NotInt))
except NotWithinRange:
    print ("This number is not within the permissible range. Error: ", str(NotFloat))
else:
    convert_celcius_to_fahrenheit(temp_entered)
