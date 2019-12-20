""" Uses the intersection method of the set data structure
    to find vowels present in a given string """

def vowels_search(string: str) -> set:
    """ Prints `True` where vowels are found """
    vowels = set('aeiou')
    found = vowels.intersection(set(string))
    print(bool(found))
    
    """ Prints the vowels found within the set intersection """
    for vowel in found:
        print(vowel)

sentence_text = 'the cat sat on the mat after dancing in the rain'
vowels_search(str(sentence_text))
