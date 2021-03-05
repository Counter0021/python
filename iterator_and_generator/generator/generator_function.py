# Все генераторы - итераторы
# Не все итераторы - генераторы

# Генераторы можно создать при помощи функций генераторов
# Генераторы можно создать при помощи генераторов выражений

# def my_func(x):
#     return x
#
#
# print(my_func(4))


# Получаем генератор, а не значение
# yield - аналог return(вырабатываем значение)
# При помощи yield - функция становится генератором
# Запоминается предыдущее значение
# Выполняетс до yield, после будет выработано значение, функция останавливается и запоминает место остановки

# Функция - генератор
def count_up_to(x):
    count = 1
    while count <= x:
        yield count
        count += 1


# print(count_up_to(4))
# counter = count_up_to(4)
# print(counter.__next__())
# print(counter.__next__())
# print(next(counter))
# print(next(counter))

counters = count_up_to(10)
counters.__next__()
for i in counters:
    print(i)