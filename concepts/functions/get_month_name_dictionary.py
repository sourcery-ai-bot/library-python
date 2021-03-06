# Emulates a Select Case in VBA; or a Switch function in Excel, Access or VBA

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

# Call function and assign the returned value to the 'month_name' variable
month_name = get_month_name(12)
print(f"{month_name = }")  # Prints 'December'
