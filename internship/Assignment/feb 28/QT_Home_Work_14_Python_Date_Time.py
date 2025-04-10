# 1
from datetime import datetime

def current_datetime():
    return datetime.now()

print(current_datetime())


# 2
from datetime import datetime

def str_to_datetime(date_string):
    return datetime.strptime(date_string, "%b %d %Y %I:%M%p")

print(str_to_datetime("Feb 25 2020 4:20PM"))


# 3
from datetime import datetime, timedelta

def subtract_week(given_date):
    return given_date - timedelta(days=7)

print(subtract_week(datetime(2020, 2, 25)))


# 4
from datetime import datetime

def format_date(given_date):
    return given_date.strftime("%A %d %B %Y")

print(format_date(datetime(2020, 2, 25)))


# 5
from datetime import datetime

def day_of_week(given_date):
    return given_date.strftime("%A")

print(day_of_week(datetime(2020, 7, 26)))


# 6
from datetime import datetime, timedelta

def add_week_and_hours(given_date):
    return given_date + timedelta(days=7, hours=12)

print(add_week_and_hours(datetime(2020, 3, 22, 10, 0, 0)))


# 7
import time

print(int(time.time() * 1000))


# 8
from datetime import datetime

def datetime_to_str(given_date):
    return given_date.strftime("%Y-%m-%d %H:%M:%S")

print(datetime_to_str(datetime(2020, 2, 25)))


# 9
from datetime import datetime
from dateutil.relativedelta import relativedelta

def add_four_months(given_date):
    return given_date + relativedelta(months=4)

print(add_four_months(datetime(2020, 2, 25).date()))


# 10
from datetime import datetime

def days_between_dates(date_1, date_2):
    return (date_2 - date_1).days

print(days_between_dates(datetime(2020, 2, 25), datetime(2020, 9, 17)))
