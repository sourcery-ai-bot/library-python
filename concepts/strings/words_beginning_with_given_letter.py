""" Retrieve all words beginning with the letter passed by the user input """

letter = input('Words beginning with the letter... ')

def return_words(letter: str) ->list:
    words_beginning_with_letter = []
    with open('concepts/strings/words.txt', 'r') as file:
        for line in file:
            if line[0] == letter:
                words_beginning_with_letter.append(line[0:len(line)-2:])
    print(words_beginning_with_letter)

try:
    return_words(letter)
except TypeError as NotLetter:
    if type(letter) != str:
        print(f"The letter {letter} is not a string data type.")
