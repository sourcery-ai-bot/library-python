from typing import Literal

directions = Literal['north', 'south', 'east', 'west']

def move_in_direction(direction: directions) -> None:
    if direction == "north":
        print('Go north')
    elif direction == "south":
        print('Go south')
    elif direction == "east":
        print('Go east')
    elif direction == "west":
        print('Go west')
    else:
        raise ValueError(f"The direction given of {direction!r} is invalid")

move_in_direction('north')
