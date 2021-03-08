# Чтение CSV файлов. CSV dictReader.
# Данные ввиде словаря
# Ключ - значение
import csv

with open('cars.csv', 'r') as file:
    # Итератор
    csv_reader = csv.DictReader(file)
    for car in csv_reader:
        # print(car)
        print(f"{car['Make']} {car['Model']} costs {car['Price']}")

# Разделение при помощи ";"
# delimiter=';'
with open('cars1.csv', 'r') as file:
    # Итератор
    csv_reader = csv.DictReader(file, delimiter=';')
    for car in csv_reader:
        # print(car)
        print(f"{car['Make']} {car['Model']} is {car['Length']} m")

# Разделение при помощи "|"
# delimiter='|'
with open('cars2.csv', 'r') as file:
    # Итератор
    csv_reader = csv.DictReader(file, delimiter='|')
    for car in csv_reader:
        # print(car)
        print(f"{car['Make']} {car['Model']} is {car['Length']} m")