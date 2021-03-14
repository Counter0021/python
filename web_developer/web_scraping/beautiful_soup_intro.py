# Фарсить html код - выбирать элементы по своему желанию
from bs4 import BeautifulSoup

# HTML код
html_string = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
    
        <title>Web Development Page</title>
    
        <style type="text/css">
    
            h1{
                color: white;
                background: red;
            }
    
            li{
                color: red;
            }
    
            #css-li{
                color: blue;
            }
    
            .green{
                color: green;
            }
    
        </style>
    </head>

    <body>
        <h1>Web Development</h1>
        <h1 class="green">Web</h1>
        <h3>Programming Languages</h3>
    
        <ol>
            <li>HTML</li>
            <li id="css-li">CSS</li>
            <li class="green">JavaScript</li>
            <li class="green">Python</li>
        </ol>
    
    </body>
    </html>

"""

# Класс BeautifulSoup
# Параметры:
# Строка с html кодом, 'html.parser' - распозновать именно html
parsed_html = BeautifulSoup(html_string, 'html.parser')
# print(parsed_html)
# print(type(parsed_html))

# Показать только код body
print(parsed_html.body)

# Получить 1 элемент(самый первый)
print(parsed_html.body.h1)
print(parsed_html.body.ol.li)

# Аналог - метод find(строка с элементом)
print(parsed_html.find('li'))

# Все элементы типа
print(parsed_html.find_all('li'))

# Элемент по id
print(parsed_html.find(id="css-li"))
# Элементы по классу
print(parsed_html.find_all(class_="green"))

# Элемент CSS селектора
# Получаем в списке
print(parsed_html.select("#css-li"))
print(parsed_html.select("#css-li")[0])
print(parsed_html.select(".green"))
print(parsed_html.select(".green")[1])
print(parsed_html.select("li"))