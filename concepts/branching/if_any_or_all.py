x = [True, True, False]

if any(x):
    print("At least one True")
else:
    print("None are True")


if all(x):
    print("Not one False")
else:
    print("At least one is False")


if any(x) and not all(x):
    print("At least one True and one False")
else:
    print("Either all are True or all are False")
