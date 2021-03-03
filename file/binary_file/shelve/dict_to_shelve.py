# Конвертиция словаря в объект shelve
import shelve
# Нужно быть осторожным с запятыми при конвертиции!!!

university = shelve.open('university_file')
university['schedules'] = {
    # Расписание по дням недели
        'monday': ['Math', 'Eng', 'System programming', 'Python'],
        'tuesday': ['Eng', 'HTML', 'Python', 'PE'],
        'wednesday': ['Physics', 'Eng', 'Python'],
        'thursday': ['Math', 'Math', 'Java'],
        'friday': ['Math', 'Physics', 'C++']
}
    # Преподователи
university['tutors'] = {
        'Math': ['Jack White', 'Jim Black'],
        'Python': ['Jason Greed', 'John Smith']
}

# x = university['schedules']
# print(type(x))

print(university['schedules']['monday'])
print(university['tutors']['Python'][1])

university.close()




# Университет
# university = {
#     # Расписание по дням недели
#     'schedules': {
#         'monday': ['Math', 'Eng', 'System programming', 'Python'],
#         'tuesday': ['Eng', 'HTML', 'Python', 'PE'],
#         'wednesday': ['Physics', 'Eng', 'Python'],
#         'thursday': ['Math', 'Math', 'Java'],
#         'friday': ['Math', 'Physics', 'C++']
#     },
#     # Преподователи
#
#     'tutors': {
#         'Math': ['Jack White', 'Jim Black'],
#         'Python': ['Jason Greed', 'John Smith']
#     }
# }
#
# print(university['schedules']['monday'])
# print(university['tutors']['Python'][1])