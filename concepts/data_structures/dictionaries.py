students = {
        "Alice": ["ID001", 21, "A"],
        "Bob": ["ID002", 22, "B"],
        "Claire": ["ID003", 23, "C"],
        "Dan": ["ID004", 24, "D"],
        "Emma": ["ID005", 25, "E"],
}

# An example of using slicers to get the item from the dictionary/list
print(students["Alice"][0])
print(students["Dan"][1:])

# The below uses a dictionary within the students dictionary
students = {
        "Alice": {"ID": "ID001", "Age": 21, "Grade": "A"},
        "Bob": {"ID": "ID002", "Age": 22, "Grade": "B"},
        "Claire": {"ID": "ID003", "Age": 23, "Grade": "C"},
        "Dan": {"ID": "ID004", "Age": 24, "Grade": "D"},
        "Emma": {"ID": "ID005", "Age": 25, "Grade": "E"},
}

# An example of using slicers to get the item from the dictionary/list
print(students["Bob"]["Age"])
