import logging
from math import sqrt, pow

filename = 'modules_standard/mod_math/quadratic_equation_calcs.log'

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(
    filename=filename,
    level=logging.DEBUG,
    format=LOG_FORMAT,
    filemode='w'
)
logger = logging.getLogger()


def quadratic_formuala(a: float, b: float, c: float) -> float:
    """ Returns the solutions to the equation ax^2 + bx + c = 0 using the
    arguments of a, b, and c as the co-efficients. """

    logger.info(f'Quadratic Formula with arguments of {a}, {b}, {c}')

    # Compute the discriminant
    logger.debug("# Compute the discriminant")
    disc = pow(b, 2) - 4 * a * c
    logger.debug(disc)

    # Compute the two roots
    logger.debug("# Compute the two roots")
    pos_root = (-b + sqrt(disc)) / (2 * a)
    neg_root = (-b - sqrt(disc)) / (2 * a)

    # Return the roots
    logger.debug("# Return the roots")
    return (pos_root, neg_root)

roots = quadratic_formuala(1, 0, -4)
logging.debug(roots)

print(roots)
