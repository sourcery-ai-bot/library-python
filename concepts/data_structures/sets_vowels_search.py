" Uses the intersection method of the set object to find vowels in a given string "

def vowels_search(string: str) -> set:
    """ Returns `True` in case where vowels found
    in addition to the field found themselves """
    vowels = set('aeiou')
    found = vowels.intersection(set(string))
    print(bool(found))
    for vowel in found:
        print(vowel)

sentence_text = 'the cat sat on the mat after dancing in the rain'
vowels_search(str(sentence_text))
