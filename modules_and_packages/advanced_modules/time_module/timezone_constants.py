# Временные зоны
import time

# Время UTC
print(f'UTC time: {time.strftime("%Y/%m/%d %H:%M:%S", time.gmtime())}')
print(f'Local time: {time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())}')

# Смещение локального времени от UTC
# Не правильный результат
print(time.altzone / 60 / 60)
print(time.daylight)

# Правильно
print(time.timezone / 60 / 60)

# Кортеж из двух строк:
# первая - это имя локального часового пояса без перехода на летнее время,
# вторая - имя местного часового пояса летнего времени.
print(time.tzname)

# ======================================================
#                   Лучше использовать
# ======================================================
print(time.localtime().tm_zone)
print(time.localtime().tm_gmtoff)