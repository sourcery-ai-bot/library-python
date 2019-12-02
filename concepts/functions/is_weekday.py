import datetime

sample_date = datetime.datetime(2019, 10, 27)

def is_weekday(day):
    return True if day.weekday() <5 else False

print(f"{'The 27th of October, 2019 is a Sunday, therefore'} {is_weekday(sample_date)}")
