import requests

# Получить url
response = requests.get('https://www.google.com')

# Статус - код
print(response)

# Выполнен запрос?
print(response.ok)

# Просмотреть заголовки ответа
print(response.headers)

# Получить весь html
print(response.text)