a = {1, 2, 3, 4, 5, 1}
print(a)
b = [1, 2, 3]
b = set(b)
print(b)
c = set("abc")
print(c)
d = set([1, 2, 4])
print(d)
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