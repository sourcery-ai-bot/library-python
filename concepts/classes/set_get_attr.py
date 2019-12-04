# Create a basic class with no functionality
class Car:
    pass

# Create an instance of the Car class
car = Car()

# Define attributes for the car
car_info = {
    'make': 'Audi',
    'model': 'A3',
    'colour': 'black',
}

# Set options on car object to attributes defined in car_info dictionary
for key, value in car_info.items():
    setattr(car, key, value)

# Demonstrate the attributes have been set according to the items of the car_info dictionary
print(f"""The make of the car is {car.make}, the model is {car.model} and the \
colour is {car.colour}.""" )

# Gets the key's value for each item within the car_info dictionary
for key in car_info.keys():
    print(getattr(car, key))
