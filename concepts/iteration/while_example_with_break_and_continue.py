i = 0
while True:
    i = i +1
    if i == 2:
        print("Skipping on 2 due to 'continue' statement")
        continue
    if i == 5:
        print("Breaking on 5 due to 'break' statement")
        break
    print(i)

print("Finished: While loop finished its execution")
