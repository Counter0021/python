# Обработка исключений
print('Some code')
try:
    print(len(23))
    print(a)
except NameError:
    print('NameError has happen')
except TypeError:
    print('TypeError has happen')

print('Code after error')

# Пример
user_dict = {'name': 'Arkady', 'surname': 'Counter', 'age': 25}

# По ключам значения
print(user_dict['name'])
print(user_dict['car'])

# .get()
print(user_dict.get('name'))
print(user_dict.get('car'))


def get_dict_values(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        return None


print(get_dict_values(user_dict, 'age'))
print(get_dict_values(user_dict, 'car'))
