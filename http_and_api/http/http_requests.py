# Http запрос

import requests

# Ссылка на сайт
url = "https://www.google.com"
# Получить url
response = requests.get(url)
# Вывести на экран url и статус-код
print(f'Request to {url}. Status code is {response.status_code}.')
