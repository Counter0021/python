# База данных студентов
import sqlite3

# Установка соединения с базой данных, если она существует, либо создаёт новую, если нет файла.
conn = sqlite3.connect('students_db.db')

# Созадать курсор для выполнения sql запросов
cursor = conn.cursor()

# Поместить в курсор
# cursor.execute('Запрос')

# ===============================================
#               Создать таблицу
# ===============================================
cursor.execute('CREATE TABLE students (name Text, last_name Text, age Integer);')

# ===============================================
#           Вставка данных(добавить)
# ===============================================
insert_query = 'INSERT INTO students VALUES ("Arkady", "Counter", 25);'
cursor.execute(insert_query)

cursor.execute('INSERT INTO students VALUES ("Arkady", "Counter", 25);')

# ===============================================
#   Вставлять данные взятые из переменных
# ===============================================
name = 'Daniil'
surname = 'Krost'
age = 20

jack = ('Jack', 'Black', 18)

# 1 способ (не очень хороший)
insert_query_values = f'INSERT INTO students VALUES ("{name}", "{surname}", {age});'
cursor.execute(insert_query_values)

# 2 способ (рекомендуется)
# ? - вместо значений
insert_query_values = 'INSERT INTO students VALUES (?, ?, ?);'
cursor.execute(insert_query_values, (name, surname, age))

# Можно сразу tuple передавать
cursor.execute(insert_query_values, jack)

# ===============================================
#           Вставка много данных
# ===============================================
students_list = [
    ('Jane', 'White', 19),
    ('Bob', 'Blue', 38),
    ('Rex', 'Smith', 22)
]

insert_query_students_list = 'INSERT INTO students VALUES (?, ?, ?);'
# С циклом
for student in students_list:
    cursor.execute(insert_query_students_list, student)

# С методом executemany()
cursor.executemany(insert_query_students_list, students_list)

# ===============================================
#                   Чтение
# ===============================================
# Итератор объект
cursor.execute('SELECT * FROM students WHERE name is "Arkady";')

# 1 способ - цикл
for row in cursor:
    print(row)

# Методы - извлечь
# Извлечь одну (первую)
print(cursor.fetchone())

# Извлечь все
print(cursor.fetchall())

# ===============================================
#                  Обновление
# ===============================================
cursor.execute("UPDATE students SET age=21 WHERE name='Daniil';")
cursor.execute("UPDATE students SET last_name='Austen' WHERE name is 'Bob';")

# ===============================================
#                  Удаление
# ===============================================
cursor.execute('DELETE from students where last_name is "Smith";')
cursor.execute('DELETE from students;')

# Чтение
cursor.execute('Select * from students;')
data = cursor.fetchall()
[print(row) for row in data]

# Сохранить изменения в базе данных
conn.commit()

# Обязательно нужно закрыть!
conn.close()
