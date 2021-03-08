# Запись в CSV файл - writer()
import csv

# Запись в CSV файл - writer()
with open('students.csv', 'w') as file:
    csv_writer = csv.writer(file)
    # writerow() - запись
    # Ввиде списка
    csv_writer.writerow(['Name', 'Surname', 'Age'])
    csv_writer.writerow(['Arkady', 'Counter', '25'])
    csv_writer.writerow(['Daniil', 'Krost', 20])

# Выбор данных и их запись
# 1 - способ
with open('cars.csv') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    make_model_list = []
    for i in csv_reader:
        make_model_list.append([i[1], i[2]])

with open('cars_make_model.csv', 'w') as file:
    csv_writer = csv.writer(file, delimiter=';')
    for i in make_model_list:
        csv_writer.writerow(i)

# 2 - способ
# Короче
with open('cars.csv') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    with open('cars_make_model_2.csv', 'w') as file:
        csv_writer = csv.writer(file, delimiter=';')
        for i in csv_reader:
            csv_writer.writerow([i[1], i[2]])