import pytz
import datetime

# Время в Москве и сдвиг от UTC
moscow = 'Europe/Moscow'
tz_moscow = pytz.timezone(moscow)
moscow_time = datetime.datetime.now(tz=tz_moscow)
print(moscow_time)

# Какие тайм зоны есть
for i in pytz.all_timezones:
    print(i)

# Тайм зоны в стране
for i in pytz.country_names:
    print(i, pytz.country_names[i], pytz.country_timezones.get(i))

# Вывод времени и даты
print(datetime.datetime.today())
print(datetime.datetime.now(tz=None))

# UTC время
print(datetime.datetime.utcnow())