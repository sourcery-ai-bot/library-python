""" Returns a list of all folders and files within the current working directory """

from os import listdir, curdir
from os.path import join, isfile

def walk(dirname):
    for name in listdir(dirname):
        path = join(dirname, name)

        if isfile(path):
            print(path)
        else:
            walk(path)

print(walk(curdir))
