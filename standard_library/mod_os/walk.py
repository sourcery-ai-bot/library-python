import os

routepath = os.getcwd()

# Displays the list of directory paths, directory names and files within the 'routepath'
for dirpath, dirnames, filenames in os.walk(routepath):
    print('Current Path: ', dirpath)
    print('Directories: ', dirnames)
    print('Files:', filenames)
