from calendar import calendar, datetime, day_name, day_abbr, month

print(datetime, '\n', calendar, '\n', day_name, '\n', day_abbr)

# Prints the calendar to the terminal for December 2019
yyyy, mm = 2019, 12
print(month(yyyy, mm))
