# This function emulates a Select Case in VBA, or a Switch function in Excel,
# Access or VBA
# It uses a dictionary to store key and value data pairs


def get_month_name(month_num):
    return {
        1: lambda: "January",
        2: lambda: "February",
        3: lambda: "March",
        4: lambda: "April",
        5: lambda: "May",
        6: lambda: "June",
        7: lambda: "July",
        8: lambda: "August",
        9: lambda: "September",
        10: lambda: "October",
        11: lambda: "November",
        12: lambda: "December"
    }.get(month_num, lambda: None)()

# Call function and assign the returned value to the answer variable
# Prints 'December'
answer = get_month_name(12)
print(answer)    
