from fractions import Fraction

num = Fraction(6, 11)
den = Fraction(4, 5)


def add_frac(x, y):
    added = x + y
    return added

print(add_frac(num, den))


def sub_frac(x, y):
    subtracted = x - y
    return subtracted

print(sub_frac(num, den))


def mult_frac(x, y):
    multiplied = x * y
    return multiplied

print(mult_frac(num, den))


def div_frac(x, y):
    divided = x / y
    return divided

print(div_frac(num, den))
