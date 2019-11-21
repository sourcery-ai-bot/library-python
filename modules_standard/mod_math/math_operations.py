import math as m
import random as r

print(f"{'The sum of 1, 2, 3, 4 and 5'} is {m.fsum([1, 2, 3, 4, 5])}")

print(f"{'The floor of 10.6'} is {m.floor(10.6)}")

print(f"{'The ceiling of 10.6'} is {m.ceil(10.6)}")

print(f"{'The hypotenuse where 3 and 4 are the other 2 sides'} is {m.hypot(3, 4)}")

print(f"{'2 to the power of 3'} is {m.pow(2, 3)}")

print(f"{'The sine of 90 degrees is'} {m.sin(90)}")

print(f"{'The cosine of 90 degrees is'} {m.cos(90)}")

print(f"{'The tangent of 90 degrees is'} {m.tan(90)}")

print(f"{'The square root of 56 is'} {m.sqrt(56)}")

print(f"{'Returns the absolute value (i.e. 12)'} {m.fabs(-12)}")

print(f"{'Returns the natural logarithm of 10 with respect to base e'} is {m.log(10)}")

print(f"{'Returns the logarithm of 10,000 with respect to base 10'} is {m.log10(10000)}")

print(f"{'Greatest common divisor of 20 and 25'} is {m.gcd(20, 25)}")

print(f"{'5!'} is {m.factorial(5)}")

print(f"{'57.3 radians'} is approximately {m.radians(57.3)} {'degree'}")

print(f"{'90 degrees is'} {m.radians(90)} {'radians'}")

print(f"""
    Returns two outputs:
    1) The fractional element (i.e. the .4); and
    2) the integer element (i.e. the 15)
    Outputs (as a tuple) = {m.modf(15.4)}
    """
)

print(f"{'Returns False if its argument is a number'} {m.isnan(0.0)}")

print(f"{'The argument truncated (i.e. 123)'} of 123.6 is {m.trunc(123.6)}")

"""
This returns `True` because it has 7 decimal places. If it were just 6 here,
this would have returned `False` (i.e. not close)
"""
print(m.isclose(100, 99.9999999))
