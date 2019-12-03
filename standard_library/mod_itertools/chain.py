import itertools

q1 = ['Jan', 'Feb', 'Mar']
q2 = ['Apr', 'May', 'Jun']
q3 = ['Jul', 'Aug', 'Sep']
q4 = ['Oct', 'Nov', 'Dec']

# Create a chain itertools object chaining together the 4 lists - for each quarter of the year
months_of_year = itertools.chain(q1, q2, q3, q4)

for month in months_of_year:
    print(month)
