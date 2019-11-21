# This function emulates a Select Case in VBA, or a Switch function in Excel,
# Access or VBA
# It uses a dictionary to store key and value data pairs


def get_month_name(month_num):
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return months.get(month_num, "Invalid month")

# Call function and assign the returned value to the answer variable
answer = get_month_name(12)
print(answer)    # prints 'December'
