from random import choice


# # Функции высшего порядка
# # Функции, которые принимают или возвращают другие функции
#
# # ======================================================
# # Принимает функцию параметром
# # ======================================================

# # Возведение в квадрат
# def square(x):
#     return x ** 2
#
#
# # Возведение в куб
# def cube(x):
#     return x ** 3
#
#
# # Умножение числа на значение из функции
# def product(n, func):
#     result = 1
#     for i in range(1, n):
#         result *= func(i)
#     return result
#
#
# # Передаём объект
# print(product(4, square))
# print(product(3, cube))
#
#
# # Передача встроенной функции python
# def python_func(a, b, func):
#     result = func([a, b])
#     return result
#
#
# print(python_func(5, 10, sum))
#
# # ======================================================
# #             Вложенная функция
# # ======================================================
# # Окрашевание предмета
# def colorize(thing):
#     # Получить цвет
#     def get_color():
#         colors = ('red', 'green', 'blue')
#         # Функция choice() из import random
#         color = choice(colors)
#         return color
#
#     result = f'{get_color()} {thing}'
#     return result
#
#
# print(colorize('apple'))

# # ======================================================
# #                   Возвращаем функцию
# # ======================================================
# # Сделать цвет
# def make_color():
#     # Получить цвет
#     def get_color():
#         colors = ('red', 'green', 'blue')
#         # Функция choice() из import random
#         color = choice(colors)
#         return color
#
#     return get_color
#
#
# my_color = make_color()
# print(my_color())
#
# # Аналог, но плохо читабельный
# print(make_color()())
# print(make_color()())


# Можно получать доступ из внутренней функции к параметру внешней функции
def colorize_arg_in_get_colors(thing):
    # Получить цвет
    def get_colors():
        colors = ('red', 'green', 'blue')
        # Функция choice() из import random
        color = choice(colors)
        return color + ' ' + thing

    return get_colors


print(colorize_arg_in_get_colors('Table')())
color_dog = colorize_arg_in_get_colors('dog')
print(color_dog())
