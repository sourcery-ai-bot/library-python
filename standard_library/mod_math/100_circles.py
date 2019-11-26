import os
from logging import basicConfig, DEBUG, getLogger
from math import pi, pow

DIR_LOC = os.path.dirname(os.path.realpath(__file__))
filename = f"{DIR_LOC}{'/100_circles.log'}"

# Delete the exising log file
with open(file=filename, mode='w') as log_file:
    log_file.__del__()


# Create and configure the logger
LOG_FORMAT = "%(levelname)s - %(filename)s - %(lineno)s - %(asctime)s - %(message)s"
basicConfig(filename=filename,
            level=DEBUG,
            format=LOG_FORMAT,
            filemode='w')
logger = getLogger()


def area_of_circle(radius: float) -> float:
    """Computes the area of a circle given its radius as a float"""
    return pi * pow(radius, 2)


def circumference_of_circle(radius: float) -> float:
    """Computes the circumference of a circle given its radius as a float"""
    return 2 * pi * radius


def diameter_of_circle(radius: float) -> float:
    """Computes the diameter of a circle given its radius"""
    return 2 * radius


for circle_num in range(1, 101):
    logger.info(f'Circle No: {circle_num}')

    radius = float(circle_num)
    logger.info(f'Circle radius: {radius} metres')

    diameter = diameter_of_circle(radius)
    logger.info(f'Circle diameter: {diameter} metres')

    area = area_of_circle(radius)
    logger.info(f'Circle area: {area} square metres')

    circumference = circumference_of_circle(radius)
    logger.info(f'Circumference: {circumference} metres')

    logger.info('*' * 45)


print(f"{'Logging output at'} /{filename}")
