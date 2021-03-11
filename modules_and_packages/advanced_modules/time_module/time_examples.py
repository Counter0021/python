# Модуль тайм
import time

# Определение эпохи
print(time.gmtime(0))

# Текущая дата
print(time.gmtime())

# Локальное (местное время)
local_time = time.localtime()
print(local_time)

# Время в секундах прошедших с начала эпохи
print(time.time())

# Конвертирует время выраженное в секундах с начала эпохи в строковой формат,
# представляющий из себя локальное время
print(time.ctime())

# Задержка потока кода на количество секунд
print('Text before delay')
time.sleep(3.2)
print('Text after 3.2 seconds')

# Количество секунд с начала эпохи с учётом локального времени
print(time.mktime(local_time))

# Возвращает str отображение времени с начала эпохи с учётом локального времени
print(time.asctime(local_time))

# Конвертирует время в строку, как указано в аргументе формат. Формат - строка
# %X - время
# %x - дата
print(time.strftime('%x %X', local_time))
print(time.strftime('%m/%d/%Y, %H:%M:%S', local_time))

# Распознаёт строку, которая представляет время и возвращает объект struct_time
time_string = '21 December, 2021'

struct_time = time.strptime(time_string, '%d %B, %Y')
print(struct_time)
