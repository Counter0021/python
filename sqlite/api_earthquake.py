# Землетрясения
import requests
import sqlite3


def save_data(data_list):
    # Установка соединения с базой данных, если она существует, либо создаёт новую, если нет файла.
    conn = sqlite3.connect("earthquakes_db.db")
    # Создать курсор для выполнения sql запросов
    cursor = conn.cursor()
    # Создать таблицу
    # cursor.execute("CREATE TABLE earthquakes (place TEXT, magnitude REAL)")
    # Добавить данные
    cursor.executemany("INSERT INTO earthquakes VALUES (?, ?)", data_list)

    # Сохранить изменения в базе данных
    conn.commit()

    # Обязательно нужно закрыть!
    conn.close()


def print_data():
    # Установка соединения с базой данных, если она существует, либо создаёт новую, если нет файла.
    conn = sqlite3.connect("earthquakes_db.db")
    # Создать курсор для выполнения sql запросов
    cursor = conn.cursor()
    select_query = 'select * from earthquakes;'
    cursor.execute(select_query)

    # Извлекаем данные из базы данных
    data_list_db = cursor.fetchall()
    count = 0
    for i, j in data_list_db:
        count += 1
        print(f"{count}. Place: {i}. Magnitude: {j}")

    # Сохранить изменения в базе данных
    conn.commit()

    # Обязательно нужно закрыть!
    conn.close()


url = "https://earthquake.usgs.gov/fdsnws/event/1/query?"

starttime = input('Enter the start time: ')
endtime = input('Enter the end time: ')
latitude = input('Enter the latitude: ')
longitude = input('Enter the longitude: ')
maxradiuskm = input('Enter the max radius in km: ')
minmagnitude = input('Enter the min magnitude: ')

response = requests.get(url, headers={'Accept': 'application/json'}, params={
    'format': 'geojson',
    'starttime': starttime or '2019-01-01',
    'endtime': endtime or '2019-02-01',
    'latitude': latitude or '51.51',
    'longitude': longitude or '-0.13',
    'maxradiuskm': maxradiuskm or '2000',
    'minmagnitude': minmagnitude or '2'
})

data = response.json()

# Список для записи в db
data_list = []

# Цикл записи в db
for i in range(len(data['features'])):
    data_list.append([])
    place = data['features'][i]['properties']['place']
    magnitude = data['features'][i]['properties']['mag']
    data_list[i].append(place)
    data_list[i].append(magnitude)

question = input('Enter YES if you want to store the data in the database, or leave it blank if you don\'t: ').upper()
if question == "YES":
    save_data(data_list)
print_data()
