# Получаем контент с веб сайта
# Воруем цитаты
# сайт - https://quotes.toscrape.com/
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://quotes.toscrape.com/'
response = requests.get(url)

html_data = BeautifulSoup(response.text, 'html.parser')
# Цитаты
quotes = html_data.find_all(class_='quote')

# Запись в файл цитат
with open('web_scraping_data.csv', 'w', encoding='utf-8') as file:
    headers_list = ['Quoter', 'Author', 'Tags']
    csv_writer = csv.DictWriter(file, fieldnames=headers_list, delimiter='|')
    csv_writer.writeheader()
    for quote in quotes:
        csv_writer.writerow({
            'Quoter': quote.find(class_='text').get_text(),
            'Author': quote.find(class_='author').get_text(),
            'Tags': quote.find(class_='keywords')['content']
        })