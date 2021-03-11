from datetime import date

# Текущая дата
today = date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)

# Разница во времени
date_1 = date(2021, 3, 11)
date_2 = date(2020, 3, 11)
diff = date_1 - date_2
print(diff)

# Количество дней до др
print(today)

my_birthday = date(today.year, 7, 31)
# Если прошло
if my_birthday < today:
    my_birthday = my_birthday.replace(year=today.year + 1)
print(my_birthday)

days = my_birthday - today
print(f'You will celebrate your birthday in {days.days} days!')

# Какой день недели?
# week_day = today.weekday()
week_day = today.isoweekday()
print(week_day)