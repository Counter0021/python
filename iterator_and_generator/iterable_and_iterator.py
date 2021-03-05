# Iterate - перебирать элементы.

# Iterables object
# Объект, который можно перебирать
number_list = [1, 2, 3, 4, 5]

for num in number_list:
    print(num)

for let in 'my string':
    print(let)

# Iterators - переборщик Iterables object. Метод iter()
number_list_iterator = iter(number_list)
print(type(number_list_iterator))

string_iterator = iter('my string')
print(type(string_iterator))

# Без iter() не работает!!!
# Функция next() или метод .__next__() - переходит к следующему элементу объекта Iterable.
# Перебор всех элементов Iterable

print(number_list_iterator.__next__())
print(number_list_iterator.__next__())
print(number_list_iterator.__next__())
print(number_list_iterator.__next__())
print(next(number_list_iterator))

print(string_iterator.__next__())
print(string_iterator.__next__())
print(string_iterator.__next__())
print(string_iterator.__next__())


# Цикл for в виде iter()
def my_for_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator.__next__())
        except StopIteration:
            print('Iteration is finished')
            break


my_for_loop('Hello!')
my_for_loop([1, 2, 3, 4, 5])
