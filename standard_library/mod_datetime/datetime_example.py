from datetime import datetime, timedelta, timezone, date

today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1)

print(today, tomorrow, timedelta, timezone)
# Prints 2018-11-25 17:42:39.445941+00:00 2018-11-26 17:42:39.445941+00:00
# <class 'datetime.timedelta'> <class 'datetime.timezone'>

# Formatting of date/time (strftime is the String Format Time)
print(today.strftime('%d-%m-%y %H:%M:%S.%f')[:-3])
# 25-11-18 17:49:45.456

# Prints Christmas date for 2019
print(date(2019, 12, 25))
