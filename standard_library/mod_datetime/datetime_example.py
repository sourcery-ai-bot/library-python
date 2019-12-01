from datetime import datetime, timedelta, timezone, date

today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1)

print(f"{today = }")
print(f"{tomorrow = }")
print(f"{timedelta = }")
print(f"{timezone = }")

# Formatting of date/time (strftime is the String Format Time)
print(f"{'strftime formatted string ='} {today.strftime('%d-%m-%y %H:%M:%S.%f')[:-3]}")

# Prints Christmas Day date for 2019
print(f"{'date example ='} {date(2019, 12, 25)}")
