import os

# Prints the current working directory
cwd = os.getcwd()
print(cwd)

# Returns a list of files and other directories within the current working directory
print(os.listdir(cwd))

print(os.environ)

print(os.path.basename(''))

print(os.path.exists('test.txt'))

# Returns the absolute path of testfile.txt
print(os.path.abspath('testfile.txt'))

# Checks whether the passed string is a directory
print(os.path.isdir('/user/testfolder/'))        # Prints True
print(os.path.isdir('testfile.txt'))             # Prints False

# Checks whether the passed string is a file
print(os.path.isfile('testfile.txt'))            # Prints True
print(os.path.isfile('/user/testfolder/'))       # Prints False

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)

print(walk(cwd))
