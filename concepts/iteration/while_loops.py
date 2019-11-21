# While Loops
i = 1
while i <= 10:
    print(i)
    i += 1

# Baby simulator

answer = input("Why is the grass green?: ").strip().lower()

while answer != "just because":
    answer = input("why?: ").strip().lower()