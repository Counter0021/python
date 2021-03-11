# Какой день недели?
from datetime import date

today = date.today()
day = int(input('Please enter a day: ') or today.day)
month = int(input('Please enter a month: ') or today.month)
year = int(input('Please enter a year: ') or today.year)

week_days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                  'Friday', 'Saturday', 'Sunday']

today_user = date(year, month, day)
week_day = today_user.isoweekday()
print('Today is the day of the week:', week_days_list[week_day - 1])
