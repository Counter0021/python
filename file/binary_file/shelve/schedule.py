# Небезопасно может быть
import shelve

# Расписание по неделе дня
monday = ['Math', 'Eng', 'System programming', 'Python']
tuesday = ['Eng', 'HTML', 'Python', 'PE']
wednesday = ['Physics', 'Eng', 'Python']
thursday = ['Math', 'Math', 'Java']
friday = ['Math', 'Physics', 'C++']

# writeback - обратная запись
with shelve.open('schedules', writeback=True) as schedules:
    schedules['monday'] = monday
    schedules['tuesday'] = tuesday
    schedules['wednesday'] = wednesday
    schedules['thursday'] = thursday
    schedules['friday'] = friday

    # ================================================
    #                   Добавить пердмет
    # Не получается
    # schedules['thursday'].append('Swimming')

    # ================================================
    #               С временным списом
    # temp_list = schedules['thursday']
    # temp_list.append('Swimming')
    # schedules['thursday'] = temp_list

    # При помощи writeback
    # Если большое обновление данных лучше не надо!!!
    schedules['friday'].append('Python')

    for key in schedules:
        print(key, schedules[key])