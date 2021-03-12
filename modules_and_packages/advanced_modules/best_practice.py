# Практика с модулями времени
import datetime
import pytz

# Формат строки
# z - сдвиг
iso_format_string = '%Y-%m-%dT%H:%M:%S%z'

now_utc = datetime.datetime.now(pytz.timezone('UTC'))
print(now_utc.strftime(iso_format_string))