# Вызов своей ошибки по желанию raise
#
# Без указания текста
# raise ValueError()
#
# Указать текст ошибки
# raise ValueError('Invalid value')

def get_rainbow_color(color_num):

    '''
    :param color_num: Color number must be integer type
    and Color number must be in range of integer from 1 to 7
    :return: color
    '''
    color_num_list = [1, 2, 3, 4, 5, 6, 7]
    # Ошибки
    if type(color_num) is not int:
        raise TypeError('Color number must be integer type')

    if color_num not in color_num_list:
        raise ValueError('Color number must be in range of integer from 1 to 7')

    if color_num == 1:
        return 'red'
    elif color_num == 2:
        return 'orange'
    elif color_num == 3:
        return 'yellow'
    elif color_num == 4:
        return 'green'
    elif color_num == 5:
        return 'blue'
    elif color_num == 6:
        return 'indigo'
    elif color_num == 7:
        return 'violet'


color = get_rainbow_color(4)
print(color)

def colorize_text(color_num, text):
    color_num_list = [1, 2, 3, 4, 5, 6, 7]
    # Ошибки
    if type(color_num) is not int:
        raise TypeError('Color number must be integer type')

    if color_num not in color_num_list:
        raise ValueError('Color number must be in range of integer from 1 to 7')

    if type(text) is not str:
        raise TypeError('Text number must be string type')

    if color_num == 1:
        print('red', text)
    elif color_num == 2:
        print('orange', text)
    elif color_num == 3:
        print('yellow', text)
    elif color_num == 4:
        print('green', text)
    elif color_num == 5:
        print('blue', text)
    elif color_num == 6:
        print('indigo', text)
    elif color_num == 7:
        print('violet', text)


colorize_text(4, 'dog')
