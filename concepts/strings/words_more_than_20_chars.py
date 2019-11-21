""" Retrieve all words with more than 20 characters from the words.txt file. """

big_words = []
with open('concepts/strings/words.txt', 'r') as file:
    for line in file:
        if len(line.strip()) >= 20:
            big_words.append(line)
print(big_words)
