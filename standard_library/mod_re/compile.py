import re

sentence = "The cat sat on the mat at the bat's cave."

# Matches cat, sat, mat, and at but NOT bat
pattern_to_match = re.compile(r'[^b]at')

# Create an iterator of match objects
matches = pattern_to_match.finditer(sentence)

# Verify type of matches object
print(type(matches))

# Exhaust matches object by yielding each match
for match in matches:
    print(match)
