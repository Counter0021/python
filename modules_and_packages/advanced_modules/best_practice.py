# Практика с модулями времени
import datetime
import pytz

# Формат строки
# z - сдвиг
iso_format_string = '%Y-%m-%dT%H:%M:%S%z'

# Лучше всего делать в UTC, потом переводить в локальное время
# Получить объект с таймзоной
naive_now = datetime.datetime.now()
print(naive_now)
moscow_timezone = pytz.timezone('Europe/Moscow')
local_datetime = moscow_timezone.localize(naive_now)
print(local_datetime)

# UTC - время
now_utc = datetime.datetime.now(pytz.timezone('UTC'))
print(now_utc.strftime(iso_format_string))

# Время в Стамбуле
now_eu_istanbul = now_utc.astimezone(tz=pytz.timezone('Europe/Istanbul'))
print(now_eu_istanbul.strftime(iso_format_string))

# Время в Москве
now_eu_moscow = now_utc.astimezone(tz=pytz.timezone('Europe/Moscow'))
print(now_eu_moscow.strftime(iso_format_string))

# Все таймзоны
all_timezones = pytz.all_timezones
# for i in all_timezones:
#     print(i)
