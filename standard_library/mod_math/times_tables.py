end_with = 20

for i in range(1, end_with + 1):
    print(str(i)+' times table...')
    for j in range(1, end_with + 1):
        print(f"\t{i} " + chr(215) + f" {j}" + " = " + f"{i*j}")
