from collections import Counter

str_to_be_letter_counted = 'This is a test string'

elements = Counter(str_to_be_letter_counted.replace(' ', '').lower()).elements()
# elements is an iterator (Chain) object
print(elements)

for element in elements:
    print(element)
