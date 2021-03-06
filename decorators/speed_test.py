# Скорость выполнения кода

from time import time
from functools import wraps


# Декоратор тестирования скорости
def speed_test(function):
    # Чтобы документация не терялась
    @wraps(function)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = function(*args, **kwargs)
        end_time = time()
        print(f'Time of code execution {end_time - start_time}')
        return result

    return wrapper


@speed_test
def sum_with_list():
    return sum([i for i in range(10000)])


@speed_test
def sum_with_generator():
    return sum(i for i in range(10000))


@speed_test
def product(ranges):
    res = 1
    for i in range(1, ranges):
        res *= i
    return res


if __name__ == '__main__':
    x = sum_with_list()
    y = sum_with_generator()

    print(f'List amount: {x}')
    print(f'Generator amount: {y}')

    z = product(10000)
    print(f'Product: {z}')
