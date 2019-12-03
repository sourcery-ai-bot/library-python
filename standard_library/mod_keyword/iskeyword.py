# Uses the keywords module to check whether an item is a Python keyword
from keyword import iskeyword

def contains_keyword(*args):
    for item in args:
        if iskeyword(item):
            return True

# Returns True because 3 of the 4 listed keywords are Python keywords
keywords_list1 = contains_keyword('print', 'def', 'for', 'it')
print(keywords_list1)

# Returns None because none of the keywords are present in the functions' arguments
keywords_list2 = contains_keyword('say', 'hey', 'ney', 'slay')
print(keywords_list2)
