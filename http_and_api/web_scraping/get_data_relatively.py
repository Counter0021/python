# Получить данные относительно HTML элементов
from bs4 import BeautifulSoup

# Внутренний HTML элемент является потомком внешенго (<head> и <body> - потомки <html>)
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

# Класс BeautifulSoup - извлечение из html string
# Параметры:
# Строка с html кодом, 'html.parser' - распозновать именно html
parsed_html = BeautifulSoup(html_string, 'html.parser')

# Чтобы обратиться к потомкам body
data = parsed_html.body.contents
print(data)
# Потомки без (\n) .findChildren()
data_children = parsed_html.body.findChildren()
print(data_children)

data_ol = parsed_html.body.contents[7].contents
print(data_ol)

# Обратиться к следующему элементу, после h1 метод .next_sibling
data_next_sibling = parsed_html.body.contents[1].next_sibling.next_sibling
print(data_next_sibling)
# Метод find_next_sibling(), не учитываются переходы на новую строку (\n), можно указывать параметры
data_next_sibling_find = parsed_html.body.contents[3].find_next_sibling()
print(data_next_sibling_find)

# Обратиться к предыдущему элементу, метод .previous_sibling
data_privious_sibling = parsed_html.body.contents[3].previous_sibling.previous_sibling
print(data_privious_sibling)
# Метод find_previous_sibling(), не учитываются переходы на новую строку (\n), можно указывать параметры
data_privious_sibling_find = parsed_html.body.contents[5].find_previous_sibling()
print(data_privious_sibling_find)

# Получить родителя .parent
data_ol_li = parsed_html.find(id='css-li').parent.parent
print(data_ol_li)
data_ol_li_find_parent = parsed_html.find(id='css-li').find_parent()
print(data_ol_li_find_parent)