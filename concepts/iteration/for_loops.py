# For Loops

for i in range(1, 201, 1):
    if i % 2 == 0:
        print(i)

# The above can be written as a succinct list comprehension format
even_nums = [i for i in range(1, 101) if i % 2 == 0]
i = 0
odd_nums = [i for i in range(1, 101) if i % 2 != 0]


vowels = 0
consonants = 0

test_string = "we wish you a merry Christmas and a happy new year"

for letter in test_string:
    if letter.lower() in 'aeiou':
        vowels += 1
    elif letter == " ":
        pass
    else:
        consonants += 1

print(str(vowels) + " vowels and " + str(consonants) + " consonants")


students = {
    "male": ["Tom", "Charlie", "Harry", "Frank"],
    "female": ["Sarah", "Huda", "Samantha", "Emily", "Elizabeth"]
            }

for key in students.keys():
    for name in students[key]:
        if "o" in name:
            print(name)
