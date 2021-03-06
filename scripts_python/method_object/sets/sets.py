a = {1, 2, 3, 4, 5, 1}
print(a)
b = [1, 2, 3]
# Создать множество
b = set(b)
print(b)
c = set("abc")
print(c)
l = [1, 2, 4, 1, 1, 1]
d = set(l)
print(d)
# ************************** Методы множеств **************************
# Добавить элемент в множество .add()
d.add(3)
print("Элемент добавлен: ", d)
# Удалить элемент случайный .pop()
d.pop()
print("Элемент удалён:", d)
# Удалить определённый элемент, если элемента нет, будет ошибка.
# Не возвращает значения никакого .remove()
d.remove(3)
print(d)
# Удалить определённый элемент, не будет ошибки, если этого элемента нет .discard()
d.discard(4)
print(d)
# Очистка множества
d.clear()
print(f"Множество очищено {d}")
# ************************** Знаки множеств **************************
# Множество {}
f = {(1, 2), (3, 4), (2, 0), (0, 1)}
g = {(0, 0), (0, 1), (2, 0), (0, 2), (1, 1)}
# Объединение множеств |
h = f | g
print(h)
# Пересечение множеств &
k = f & g
print(k)
# Разность множеств -
l = f - g
print(l)
m = g - f
print(m)
# Симметрическая разность ^
n = f ^ g
print(n)
# ************************** Аналоги **************************
print(f.union(g))
print(f.intersection(g))
print(f.difference(g))
print(f.symmetric_difference(g))

# Проверка на вхождение элемента
e = (0, 0) in f
print(e)
i = (0, 0) in g
print(i)
