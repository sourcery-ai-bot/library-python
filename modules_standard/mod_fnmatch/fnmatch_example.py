import fnmatch
import os

# List only files which meet the pattern of *.git*
[print(item) for item in os.listdir('.')]

# List only items which meet the pattern of *.git*
[print(item) for item in os.listdir('.') if fnmatch.fnmatch(item, '*.git*')]
