""" A series of various functions to practice making Python functions """

def celsius_to_fahrenheit(celcius: float) -> float:
    # Computes the temperature in degrees fahrenheit given the degrees in Celcius
    try:
        if - 50 <= celcius <= 50:
            pass
    except ValueError as out_of_range:
        print("Must be between -50 and 50.")
    
    try:
        if type(celcius) != int or type(celcius) != float:
            pass
    except TypeError as not_int_or_float:
        print("Must be passed as either an integer or a float")
    else:
        return celcius * 9 / 5 + 32


print(celsius_to_fahrenheit(-40))


def fahrenheit_to_celcius(fahrenheit: float) -> float:
    return fahrenheit / 9 * 5 - 32
    
print(fahrenheit_to_celcius(90))
