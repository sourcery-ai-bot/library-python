def power_of_two():
    user_input = input('Please enter a number: ')
    try:
        user_input = float(user_input)
    except ValueError:
        print('your input was invalid')

print(power_of_two())
