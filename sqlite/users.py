# SQL Injection - инъекция кода, которая может разрушить базу данных. Техника WebHacking
import sqlite3

# Установка соединения с базой данных, если она существует, либо создаёт новую, если нет файла.
conn = sqlite3.connect('users_db.db')

# Создать курсор для выполнения sql запросов
cursor = conn.cursor()

# Создать таблицу
# create_query = 'CREATE TABLE users (name Text, password Text);'

# Запрос создать таблицу
# cursor.execute(create_query)

# Пользователи
users = [

    ('_Counter021_', 'fffffffafafafafa'),
    ('Krost', 'faafafafafafa'),
    ('Counter', 'faaafgghsr12q')

]

# Добавить пользователей
# insert_query = 'INSERT into users values (?, ?);'
# cursor.executemany(insert_query, users)

# Принимаем от пользователя
user_name = input('Input your username: ')
user_password = input('Input your password: ')

# Выбор по соответствию
# Не правильно, можно взломать базу данных
# select_query = f'select * from users where name is "{user_name}" and password is "{user_password}"'
# cursor.execute(select_query)

select_query = 'select * from users where name is ? and password = ?'
cursor.execute(select_query, (user_name, user_password))

data = cursor.fetchone()
if data:
    print('You are logged in!')
else:
    print('Please try again')

# Сохранить изменения в базе данных
conn.commit()

# Обязательно нужно закрыть!
conn.close()

# Возлом базы
# " or 1=1--

# -- комментарий в SQl

# В строке после ввода
# f'select * from users where name is "Counter" and password is "" or 1=1--"'
