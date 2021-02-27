# *args - аргуметы, бесконечное количество. В функции последовательность представлена в виде кортежа
# **kwargs - аргументы по ключевому слову, бесконечное количество.
# В функции последовательность представлена в виде словаря
def ten_percent(x, y, z):
    return (x * y * z) * 0.1


c = ten_percent(10, 20, 7)
print(c)


# *args
# С бесконечными аргументами
# def ten_percent_with_args(*args):
#     product = 1
#     for i in args:
#         product *= i
#     return product * 0.1
#
# b = ten_percent_with_args(10, 20, 7, 2)
# print(b)
# a = ten_percent_with_args(10, 20, 2)
# print(a)

# Сначала позиционные параметры!!! А потом *args
def ten_percent_with_args(percent, *args):
    product = 1
    for i in args:
        product *= i
    return product / 100 * percent


a = ten_percent_with_args(20, 10, 20, 2, 345)
print(a)

# ============================================================================
print()


# ============================================================================

# **kwargs
# Параметры передаются в форме ключей и значений
# Ключ - обязательно строка(слово)!!!
# Сначала позиционные параметры!!! А потом *kwargs
def helloy_with_kwargs(greeting, **kwargs):
    if ("name" in kwargs):
        print(f"{greeting} {kwargs['name']}!")
    else:
        print(f"{greeting}. Как твоё имя?")


helloy_with_kwargs("Привет", gender="male", age=18, name="Arkady")
helloy_with_kwargs("Привет", gender="male", age=18)


# *args и **kwargs в одной функции
def func_with_args_and_kwargs(*args, **kwargs):
    print(f"Я хочу во-{args[0]} {kwargs['food']}")


func_with_args_and_kwargs("первых", "вторых", drink="воду", food="мясо")