from collections import namedtuple

Color = namedtuple('Colour', ['red', 'green', 'blue'])

colour1 = Color(red=55, green=155, blue=255)

print(f"""The red value is {colour1.red}, the green value is {colour1.green}, \
and the blue value is {colour1.blue}""")

Person = namedtuple('Person', ['title', 'first_name', 'last_name', 'gender'])

person1 = Person('Mr', 'Wayne', 'Lambert', 'Male')

print(person1)

title1, first_name1, last_name1, gender1 = person1
print(f"{title1}. {first_name1} {last_name1} is {gender1}")
