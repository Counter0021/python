# Запись в CSV файл - DictWriter()
# В форме словаря
import csv

# Запись в CSV файл - DictWriter()
with open('students1.csv', 'w') as file:
    headers_list = ['Name', 'Surname', 'Age']
    csv_writer = csv.DictWriter(file, fieldnames=headers_list)
    # Запись заголовков. Без параметров
    csv_writer.writeheader()
    # Ввиде словаря
    csv_writer.writerow({
        'Name': 'Arkady',
        'Surname': 'Counter',
        'Age': '25'})
    csv_writer.writerow({
        'Name': 'Daniil',
        'Age': 20,
        'Surname': 'Krost'})


# Выбор данных и запись их в форме словаря
with open('cars.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    csv_reader.__next__()
    with open('make_model.csv', 'w') as file:
        headers_list = ['Make', 'Model']
        csv_writer = csv.DictWriter(file, fieldnames=headers_list)
        csv_writer.writeheader()
        for car in csv_reader:
            csv_writer.writerow({
                'Make': car['Make'],
                'Model': car['Model']
            })