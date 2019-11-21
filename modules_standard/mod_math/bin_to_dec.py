def hex_to_num(num):
    return hex(num)[2:].upper()


def get_hex_nums(up_to_num):
    for i in range(1, up_to_num):
        hex_num = hex_to_num(i)
        print(hex_num)


hex_nums = [get_hex_nums(100) for i in range(100)]
print(hex_nums)
