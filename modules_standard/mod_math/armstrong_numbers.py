# Checks for Armstrong numbers in certain intervals

lower = 100
upper = 2000

for num in range(lower, upper + 1):
    # Order of number
    order = len(str(num))

    # Initialise sum
    sum = 0

    # Find the sum of the cube of each digit
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10


    if num == sum:
        print(num)
