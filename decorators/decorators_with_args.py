# Декораторы с аргументами

from functools import wraps


# Декоратор, проверка 1 аргумента функции
# Нужно создать ещё 1 дополнительный слой. Ещё 1 внутренняя функция, которая будет принимать функцию аргументом,
# так как внешний слой принимает только значение
def check_if_first_arg_is(value):
    # Внутренний декоратор
    def inner_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args and args[0] != value:
                raise ValueError(f'First argument has to be {value}')
            return func(*args, **kwargs)

        return wrapper

    return inner_dec


# Печать цвета радуги
@check_if_first_arg_is('red')
def print_rainbow_color(*args):
    print(args)


@check_if_first_arg_is(7)
def multiply_7(a, b):
    return a * b


print_rainbow_color('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet')
print(multiply_7(7, 45))

# Декоратор: приводим к нужному типу аргументы

# zip() - создаёт из 2 последовательностей Iterable новую последовательность, в которой
# к каждому из элементов 1 последовательности будет сопоставлен каждый элемент из 2 последовательности
def enforce(*types):
    def inner_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            new_args = []
            for a, t in zip(args, types):
                new_args.append(t(a))
            return func(*new_args, **kwargs)

        return wrapper

    return inner_dec


# Распечатать текст несколько раз
@enforce(str, int)
def print_text_n_times(text, n):
    for i in range(n):
        print(text)


print_text_n_times('Arkady', 2)
print_text_n_times('Arkady', '3')


# *args - ('Arkady', '3')
# *types - (str, int)
# При помощи zip(args, types) - ('Arkady', str) ('3', int)

@enforce(float, float)
def divide(a, b):
    return a / b


print(divide(4, 2))
print(divide('4', '2'))
