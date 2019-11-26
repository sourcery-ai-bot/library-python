import os
from zipfile import ZipFile

DIR_LOC = os.path.dirname(os.path.realpath(__file__))

# Creates a directory called 'extracted_files' with its contents
with ZipFile(f"{DIR_LOC}{'/premier_league.zip'}", 'r') as zf:
    zf.extractall(f"{DIR_LOC}{'/extracted_files'}")
