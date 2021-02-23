# Перевод кортежа в список
def addNum(tuple, num):
    tuple = list(tuple)
    for i in range(len(tuple)):
        tuple[i] += num
    return tuple

# Кортеж
tuple = (3, 6, 2, 6)

# Список
nextTuple = addNum(tuple, 3)

print(tuple)
print(nextTuple)

# Изменение списка внутри кортежа
nested = (1, "do", ["param", 10, 20])
print(nested)
nested[2][1] = "Да"
nested[2][0] = 0
print(nested)