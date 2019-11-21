""" Converts temperatures from one unit to the another."""


class ValueTooLow(ValueError):
    pass

class ValueTooHigh(ValueError):
    pass

class ValueNotIntOrFloat(TypeError):
    pass


def c_to_f(c) -> float:
    """Converts degrees celcius to fahrenheit"""
    try:
        if type(c) != int and type(c) !=float:
            raise ValueNotIntOrFloat(c)
        if c < - 50:
            raise ValueTooLow(c)
        if c > 50:
            raise ValueTooHigh(c)
    except ValueTooLow:
        print("The value is less than -50")
    except ValueTooHigh:
        print("The value is greater than 50.")
    except ValueNotIntOrFloat:
        print("The value is not a floating point or an integer.")
    else:
        return c / 5 * 9 + 32


print(c_to_f(45.0))
