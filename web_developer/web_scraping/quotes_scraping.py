# Получаем контент с веб сайта
# Воруем цитаты
# сайт - https://quotes.toscrape.com/
import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)

html_data = BeautifulSoup(response.text, 'html.parser')
# Цитаты
quotes = html_data.find_all(class_='quote')
# Получаем текст с цитат
for quote in quotes:
    print(quote.find(class_='text').get_text())
    # Автор
    print('Author quote:', quote.find(class_='author').get_text())
    # Получить конетн(теги), на сайте там не текст
    print(quote.find(class_='keywords')['content'])
    print()