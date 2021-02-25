# Функциональное программирование функция, возвращающая функцию. Генераторы и map.
def f(x):
    return x * 10

def double_performer(f, x):
    return f(f(x))

def f2(x):
    return x ** 2

def f3(x):
    return -x

f1 = f

c = double_performer(f, 5)
print(c)
for f in f1, f2, f3:
    y = double_performer(f, 5)
    print(y)

A = (1, 2, 3, 4, 5)
C = map(f1, A)
for y in C:
    print(y)