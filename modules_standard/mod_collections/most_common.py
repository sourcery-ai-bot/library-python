from collections import Counter

test_str = """The 'most common' method returns an ordered sequence of tuple pairs
that calculate the count of each character appearing within the string and their
relative count."""

# Counts of each of the characters within the test_string
char_counts = Counter(test_str.lower()).most_common(len(test_str))
print(char_counts)
