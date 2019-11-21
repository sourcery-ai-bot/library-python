numbers = dict(first=1, second=2, third=3, fourth=4, fifth=5)

squared_numbers = {key: value ** 2 for key, value in numbers.items()}
cubed_numbers = {key: value ** 3 for key, value in numbers.items()}

print(f'Squared numbers: {squared_numbers}, \nCubed Numbers: {cubed_numbers}')
