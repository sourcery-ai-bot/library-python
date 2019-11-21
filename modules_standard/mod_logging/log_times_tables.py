""" Logging can be used as an alternative to printing results out to the console
and is especially useful because the data logged persists after the lifetime of
the code's execution. """

from logging import basicConfig, INFO, info, Formatter
from os import path
from time import sleep, strftime, gmtime
from datetime import datetime

logfile = 'modules_standard/mod_logging/times_tables.log'

# Set the format
basicConfig(
    filename=logfile,
    level=INFO,
    format="%(message)s"
)

end_with = 20

# Get the path of the current file
info(f'Filename: {path.realpath(__file__)}')

# Get the current time
info(f'Date/Time: {strftime("%d-%m-%y %H:%M:%S", gmtime())}')
info(f'\n')

for i in range(1, end_with + 1):
    info(str(i) + " times table...")
    for j in range(1, end_with + 1):
        info(f"\t{i} " + chr(215) + f" {j}" + " = " + f"{i*j}")
