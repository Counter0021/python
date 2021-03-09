# База данных студентов
import sqlite3

# Установка соединения с базой данных, если она существует, либо создаёт новую, если нет файла.
conn = sqlite3.connect('students_db.db')

# Созадать курсор для выполнения sql запросов
cursor = conn.cursor()

# Создать таблицу
cursor.execute('CREATE TABLE students (name Text, surname Text, age Integer);')

# Сохранить изменения в базе данных
conn.commit()

# Обязательно нужно закрыть!
conn.close()
