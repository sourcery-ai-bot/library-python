# Emulates a Select Case in VBA; or a Switch function in Excel, Access or VBA

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

# Call function and assign the returned value to the 'month_name' variable
month_name = get_month_name(12)
print(f"{month_name = }")  # Prints 'December'
