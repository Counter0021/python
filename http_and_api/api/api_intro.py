# Api - интерфейс для работы с данными других сайтов(приложениями)
# Легальный способ брать данные с других сайтов для расположения на своём сайте
# json - формат передачи данных(похожи на словарь)
# Основной сайт https://earthquake.usgs.gov/fdsnws/event/1/
# Указываем метод(query?(запрос данных) https://earthquake.usgs.gov/fdsnws/event/1/query?
# Параметры
# Пары ключ и значение, разделённые знаком &
# format=geojson& - данный в формате (json)
# starttime=2014-01-01&
# endtime=2014-01-02

# Модуль запроса в интернет
import requests

# Ссылка на сайт
# С параметрами в url
# url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2019-01-01&endtime=2019-02-01&latitude=51.51&longitude=-0.13&maxradiuskm=2000"
# С параметрами не в url, params={}
url = "https://earthquake.usgs.gov/fdsnws/event/1/query?"

# Получить url
# headers={} - принимать данные (в нашем случае json)
response = requests.get(url, headers={'Accept': 'application/json'}, params={
    'format': 'geojson',
    'starttime': '2019-01-01',
    'endtime': '2019-05-01',
    'latitude': '51.51',
    'longitude': '-0.13',
    'maxradiuskm': '2000'
})

# Лучше через json()
# print(response.text)    # тип - str
# print(response.json())  # тип - dict

# Объект с данными json, можно обращаться по ключам
data = response.json()

print(data['features'][1]['properties']['place'])
