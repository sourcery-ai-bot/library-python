import re

pattern = r"(.+) \1"

match = re.match(pattern, "word word")
if match:
    print("Match 1")

match = re.match(pattern, "?! ?!")
if match:
    print("Match 2")

match = re.match(pattern, "abc cde")
if match:
    print("Match 3")

# Extract an email address from a string
pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
str = "If you would like more detail, please contact john.doe@gmail.com for assistance"

match = re.search(pattern, str)
if match:
    print(match.group())  # Prints john.doe@gmail.com


sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'abc')

matches = pattern.finditer(str)

for match in matches:
    print(match)
