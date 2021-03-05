# Генератор - выражение

def get_number_from_range():
    for i in range(10):
        yield i


counter = get_number_from_range()
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
for i in counter:
    print(i)

# Выражения - генераторы записываются в ()
# При итерации получаем 1 число из диапазона
counter_1 = (i for i in range(10))
print(counter_1.__next__())
print(counter_1.__next__())
print(counter_1.__next__())
print(counter_1.__next__())
print(counter_1.__next__())

# При [] генерируется список
# print([i for i in range(10)])
