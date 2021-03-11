# Время и дата
from datetime import datetime

today_now = datetime(2021, 3, 11)
print(today_now)
print(today_now.now())

# Возвращает количество секунд с начала эпохи
timestamp = datetime.timestamp(today_now)
print(timestamp)
timestamp_now = datetime.timestamp(today_now.now())
print(timestamp_now)

# Возвращает локальную дату и время
today = datetime.today()
print(today)
print(timestamp)
today_from_timestamp = datetime.fromtimestamp(timestamp)
print(today_from_timestamp)

today_format = today.strftime('%d %B %Y')
print('Today is', today_format)
print('Today is', today.strftime('%A'))

# Перевод в UTC формат
utc_today = today.utcnow()
print(utc_today)

# Только время
print(today.date())
# Только дата
print(today.time())

# Кортеж из года, недели года и дня недели
print(today.isocalendar())
# Формат iso, разделитель
print(today.isoformat())
