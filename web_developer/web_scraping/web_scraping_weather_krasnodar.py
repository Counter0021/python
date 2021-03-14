# Получаем контент с веб сайта
# Воруем погоду
# Сайт - https://weather.rambler.ru/v-krasnodare/
import requests
from bs4 import BeautifulSoup

url = 'https://weather.rambler.ru/v-krasnodare/'
response = requests.get(url)

html_data = BeautifulSoup(response.text, 'html.parser')

city = html_data.find(class_='_33PN').get_text()
day_of_week = html_data.find(class_='_3hDK').get_text()
weather = html_data.find(class_='Hixd').get_text()
temp = html_data.find(class_='_1HBR').get_text()
temp_app = html_data.find(class_='UJ_C').get_text()
wind = html_data.find(class_='wind').get_text()
pressure = html_data.find(class_='pressure').get_text()
moon = html_data.find(class_='moonPhase').get_text()

print(city)
print(day_of_week)
print(weather)
print('Температура', temp)
print(temp_app)
print(wind)
print(pressure)
print(moon)