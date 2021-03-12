# Тайм зоны (временные зоны)
import pytz
import datetime


# Вывод локального и UTC времени
def print_time_in_timezone(tz):
    # Получаем список таймзон
    timezon = pytz.country_timezones.get(tz)
    # Цикл вывода времени из всех таймзон этой страны
    for i in range(len(timezon)):
        # Для упрощения
        timezone_in_country = datetime.datetime.now(tz=pytz.timezone(timezon[i]))
        # Вывод страны, таймзоны и времени
        print(
            f"Time in the {pytz.country_names[tz]} of the in the time zone {timezon[i].replace('/', ' ')} "
            f"now: {timezone_in_country.strftime(iso_format_string)}")
    # Вывод UTC времени
    utc_time = datetime.datetime.utcnow()
    print(f"UTC time is {utc_time.strftime(iso_format_string)}")


# Вывод всех таймзон по странам
def timezones_in_country():
    # Печать всех таймзон и название страны
    for i in pytz.country_names:
        print(f"{i} - {pytz.country_names[i]}, time zones: {pytz.country_timezones.get(i)}")


# Проверка ввода значений
def input_time_zone():
    global timezones_input, playProgram
    # Чтобы обработать ошибку
    try:
        # Ввод 2 букв страны
        timezones_input = input(
            'Please enter two-letters code of the country to choose the time zone or \'q\' to quit: ').upper()
        # Если ввести q, то будет выход из программы
        if timezones_input == 'Q':
            playProgram = False
        # Вывод времени из этой таймзоны
        print_time_in_timezone(timezones_input)
    # Если ошибка
    except TypeError:
        # Если программа работает, избегает вывода сообщения при выходе из программы
        if playProgram:
            print('Please enter an existing time zone name!!!')
            input_time_zone()


# Главный цикл
def main():
    # Вывод всех таймзон по странам
    timezones_in_country()
    # Цикл метода ввода таймзоны
    while playProgram:
        input_time_zone()


# Ввод таймзоны
timezones_input = None
# Программа работает
playProgram = True
# Формат строка
iso_format_string = '%H:%M:%S %d-%m-%Y'

# Запуск программы
if __name__ == '__main__':
    main()
