# map, filter, lambda

# ============================================================
#                              map()
# ============================================================
# Пременение функции для каждого элемента в массиве
# Функция в map без ()

def sum_two(x):
    return x + x

number_list = [1, 2, 3, 4, 5, 6, 7]

res = map(sum_two, number_list)
# Либо список, либо цикл
print(list(res))
# for i in res:
#     print(i)

def is_in_string(string):
    if ("а" in string):
        print("В строке есть символ 'а'")
        return True
    else:
        print("В строке нет символа 'а'")
        return False

string_list = ["Привет", "Пока", "Пожалуйста", "До встречи"]

print(list(map(is_in_string, string_list)))

# ============================================================
#                    filter()
# ============================================================
# Работает только, если функция возвращает True или False
# Если return True, результат добавляется в список
# Если return False, результат не добавляется в список

def is_number_odd(number):
    return number % 2 == 1

number_list_1 = [1, 2, 3, 4, 5, 6, 7]
# Либо список, либо цикл for
filter_list = filter(is_number_odd, number_list_1)
print(list(filter_list))

# for i in filter(is_number_odd, number_list_1):
#     print(i)
print(list(filter(is_in_string, string_list)))

# ============================================================
#                    lambda()
# ============================================================
# Анонимные функции. Вызываются всего 1 раз

print(list(map(lambda number: number ** 3, number_list)))

print(list(filter(lambda number: number % 2 == 1, number_list_1)))
print(list(filter(lambda number: number % 2 == 0, number_list_1)))