def contains_colour(colour, *args):
    if colour in args:
        return True
    return False

print(contains_colour("blue", "blue", "purple", "red", "green", "yellow", "pink"))

def favourite_colours(**kwargs):
    for person, colour in kwargs.items():
        print(f"{person.capitalize()}'s favourite colour is {colour}")

favourite_colours(
    wayne="royal blue", carrie="yellow", barrie="sky blue", rachael="purple"
)
