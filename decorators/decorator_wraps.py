# Сохранять методанные функции

from functools import wraps
# Чтобы данные документации из исходной функции не терялись при использовании декоратора
# @wraps()

# __name__ - имя
# __doc__ - документация
# Декоратор описания функции
def print_function_dara(function):
    """

    This is decorator function
    :param function:
    :return:
    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f'You are using {function.__name__}')
        print(f'Function documentation {function.__doc__}')
        return function(*args, **kwargs)
    return wrapper


@print_function_dara
def squares_sum(a, b):
    """

    :param a: first number
    :param b: second number
    :return: a^2 + b^2
    """
    return a ** 2 + b ** 2


# print(squares_sum(2, 3))
print(squares_sum.__doc__)
print(squares_sum.__name__)
help(squares_sum)
