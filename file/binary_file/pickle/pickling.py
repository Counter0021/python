import pickle
# ===========================================
#               Объекты для записи
# ===========================================
honda = (
    'civic',
    'grey',
    '2009',
    (
        (1, 'James Brown'),
        (2, 'Jack White'),
        (3, 'Arkady Counter')
    )
)

models = ['civic', 'accord', 'pilot']
owners = ['James Brown', 'Jack White', 'Arkady Counter']

# ===========================================
#       Запись в двоичном виде
# ===========================================
with open('honda.pickle', 'wb') as honda_file:
    # pickle.dump - запись в файл в 2-коде
    pickle.dump(honda, honda_file)
    pickle.dump(models, honda_file)
    pickle.dump(owners, honda_file)
    pickle.dump(99595, honda_file)

# ===========================================
#       Извлечение из двоичного файла
#   В том порядке, в котором они записаны
# ===========================================
with open('honda.pickle', 'rb') as honda_file:
    # Извлечение данных pickle.load()
    honda_from_file = pickle.load(honda_file)
    model_from_file = pickle.load(honda_file)
    owners_from_file = pickle.load(honda_file)
    number = pickle.load(honda_file)


print(honda_from_file)
print(model_from_file)
print(owners_from_file)
print(number)
