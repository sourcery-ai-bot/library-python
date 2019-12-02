# Positional args became effective from Python 3.8

def greet(name, /, greeting='Hi'):
    return f'{greeting} {name}'

print(greet('Wayne'))
print(greet(['Wayne', 'Tony', 'Tom']))
