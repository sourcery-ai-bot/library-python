""" Highest order function to calculate two numbers given an operator """


def calculator(num1, num2, operator):
    return operator(num1, num2)


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiplied_by(num1, num2):
    return num1 * num2


def divided_by(num1, num2):
    return num1 / num2


def raised_to_power_of(num1, num2):
    return num1 ** num2


def quotient(num1, num2):
    return num1 // num2


def modulus(num1, num2):
    return num1 % num2


# Create an array to contain each of the operators
operators = [add, subtract, multiplied_by, divided_by,
    raised_to_power_of, quotient, modulus]

num1 = 100; num2 = 8
for operator in operators:
    answer = calculator(num1, num2, operator)
    print(f'{num1} {operator.__name__} {num2} = {answer}')
