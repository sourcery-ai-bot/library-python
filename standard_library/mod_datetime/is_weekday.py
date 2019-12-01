import datetime

sample_date = datetime.datetime(2019, 10, 27)

def is_weekday(day):
    return True if day.weekday() <5 else False

print(f"{'is_weekday result ='} {is_weekday(sample_date)}")
