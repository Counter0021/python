# Проверка аргументов. Ограничение аргументов для функции
# Отсеивание не нужных значений
from functools import wraps


# Декоратор
# Запрет аргументов **kwargs
def prohibit_kwargs(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError('Keyword arguments are prohibited')
        return function(*args, **kwargs)

    return wrapper


# Декоратор
# Запрет аргументов типа int
def prohibit_int_arguments(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for val in args:
            if type(val) == int:
                raise ValueError('Integer arguments are prohibited')
        for key, val in kwargs.items():
            if type(val) == int:
                raise ValueError('Integer arguments are prohibited')
        return func(*args, **kwargs)

    return wrapper


# @prohibit_kwargs
@prohibit_int_arguments
def print_hello(name):
    print(f'Hello {name}!')


print_hello('Arkady')
print_hello(name=3)
