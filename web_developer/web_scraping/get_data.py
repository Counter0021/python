# Получить данные
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
            <li class="green bold">JavaScript</li>
            <li class="green" id="python-li">Python</li>
        </ol>

    </body>
    </html>

"""

# Класс BeautifulSoup
# Параметры:
# Строка с html кодом, 'html.parser' - распозновать именно html
parsed_html = BeautifulSoup(html_string, 'html.parser')

# print(parsed_html.select("li"))
html_element = parsed_html.select("li")[3]

# Получить текст из html элемента
print(html_element.get_text())

html_element_list = parsed_html.select("li")
for i in html_element_list:
    print(i.get_text())

# Получить текст из html класса
class_element_list = parsed_html.select(".green")
for i in class_element_list:
    print(i.get_text())

# Название элемента
for i in class_element_list:
    print(i.name)

# Атрибуты элемента
html_element_arg = parsed_html.select("li")
for i in html_element_arg:
    print(i.attrs)

# Обращение только к классу
html_el_list = parsed_html.select("li")[3]
print(html_el_list.attrs['class'])
print(html_el_list['class'])

# Обращение только к id
print(html_el_list.attrs['id'])
print(html_el_list['id'])