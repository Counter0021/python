# Чтение CSV файлов. CSV reader.
import csv

# CSV reader
with open('cars.csv', 'r') as file:
    # Итератор
    csv_reader = csv.reader(file)
    # Чтобы не было заголовка
    next(csv_reader)
    for car in csv_reader:
        # print(car)
        print(f'{car[1]} {car[2]} costs {car[4]}')

# Двумерный список
with open('cars.csv', 'r') as file:
    # Итератор
    csv_reader_1 = csv.reader(file)
    # Чтобы не было заголовка
    next(csv_reader_1)
    data_list = list(csv_reader_1)
    print(data_list)

# Разделение при помощи ";"
# delimiter=';'
with open('cars1.csv', 'r') as file:
    # Итератор
    csv_reader = csv.reader(file, delimiter=';')
    csv_reader.__next__()
    for car in csv_reader:
        # print(car)
        print(f"{car[1]} {car[2]} is {car[3]} m")