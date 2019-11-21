import re

sentence = 'start a sentence and then bring it to an end'

start_pattern = re.compile(r'^start')
end_pattern = re.compile(r'end$')

start_matches = start_pattern.finditer(sentence)
end_matches = end_pattern.finditer(sentence)

for match in start_matches:
    print(match)

for match in end_matches:
    print(match)
