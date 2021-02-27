# Вызов всех lambda функций
a = int(input("Введите значение 1: "))
b = int(input("Введите значение 2: "))
ret = []
lam = [(lambda i, j: i + j), (lambda i, j: i - j), (lambda i, j: i / j), (lambda i, j: i * j)]
for i in range(len(lam)):
    x = lam[i](a, b)
    ret.append(x)
print(ret)