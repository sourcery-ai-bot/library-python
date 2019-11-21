""" Retrieve all words which only contain consonants. """

words_with_all_consonants = []
with open('concepts/strings/words.txt', 'r') as file:
    for line in file:
        if not set('aeiou').intersection(line.lower()):
            words_with_all_consonants.append(line[0:len(line)-2:])
print(words_with_all_consonants)
