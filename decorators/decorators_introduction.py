# Декораторы - добавляют новую функциональность
def simple_function():
    print('Simple function code')


simple_function()


# Чтобы расширить функцию
# Функция - декоратор
# Определение функции декоратора
def decorators_function(original_function):
    # Обёрточная функция
    def wrap_function():
        print('Some code before the old code')
        original_function()
        print('Some code after the old code')

    return wrap_function


# decorator_func = decorators_function(simple_function)
# decorator_func()


# Получаем код с дополнительной функциональностью(задикорированный код)
# Определение исходной функции
@decorators_function
# Чтобы отключить новую функциональность нужно # @декоратор или убрать его
def simple_function():
    print('Simple function code')


simple_function()


# Декоратор
def make_compliment(func):
    # *args и **kwargs - для универсальности функции
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print(f'Nice to meet you!')
        print('You look great!')

    return wrapper


# Как тебя зовут?
@make_compliment
def ask_name():
    print('What is your name?')


ask_name()


# Скажи имя
@make_compliment
def say_name(name):
    print(f'My name is {name}')


say_name('Arkady')


# Я хочу...
@make_compliment
def order(food, drink):
    print(f'Give me {food} and {drink}')


order(food='chips', drink='cola')
