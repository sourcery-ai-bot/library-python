i = 0
print('while loop')
while i <= 100:
    if i % 5 == 0:
        print(i)
    i += 1


print('for loop')
for i in range(1, 101):
    if i % 5 == 0:
        print(i)

films = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


for i in films:
    if films[i] % 2 == 0:
        print(i)


films2 = {
    "Die Hard": 1,
    "Vanilla Sky": 2,
    "Top Gun": 3,
    "Shooter": 4,
        }

for f in films2.keys():
    print(f)
