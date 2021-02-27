# Вывод приветсвия
def print_greeting():
    # Документация функции
    # Док - стринг
    """
    print("Helloy!")
    :return: None
    """
    print("Helloy!")

# Функция с параметром
# Дефолтный параметр
def print_greeting_with_name(name="Name"):
    """
    :param name
    :return: No
    """
    print(f"Helloy {name}!")

def summ_of_two_numbers(a=0, b=0):
    """
    :param a:
    :param b:
    :return: a + b
    """
    return a + b

# Просмотр документации функции help()
help(print_greeting)
help(print_greeting_with_name)
help(summ_of_two_numbers)

# Запуск
print_greeting()
print_greeting_with_name("Arkady")
x = summ_of_two_numbers(2, 8)
print(x)