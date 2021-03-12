# Промежуток времени

from datetime import timedelta
from datetime import datetime

# year = timedelta(days=365)
# print(year)

# Сейчас
today = datetime.now()
print('Today is', today)

# Дата через сколько-то дней
print('23 days from today will be', (today + timedelta(days=23)))
print('2 days from today will be', (today + timedelta(days=2)))
print('230000 seconds from today will be', (today + timedelta(seconds=230000)))
print('230000000 microseconds from today will be', (today + timedelta(microseconds=230000000)))

# Сколько дней назад было число
last_birthday = datetime(2020, 7, 31)
print('My last birthday was {0} days ago.'.format((today - last_birthday).days))

# Сколько в году секунд
year = timedelta(days=365)
leap_year = timedelta(days=366)
print(f'There are {year.total_seconds()} seconds in a year and {leap_year.total_seconds()} seconds in a leap year')

# Вычислить сколько дней в 7 годах
print(f'There are {(year * 7).days} days in 7 years and {(leap_year * 7).days} days in 7 leap years')
