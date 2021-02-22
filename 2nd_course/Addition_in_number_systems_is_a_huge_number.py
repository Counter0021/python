import random

# Суммирование 2 списков
def summLong(a, b, base):
    # Создаём копию списка "a" в переменную
    # acopy для того, чтобы
    # не изменить оригинал
    acopy = a.copy()

    # Создаём список "c", в котором будет результат
    c = []

    # До последнего элемента:
    # чтобы не было выхода за
    # границы списка в случае
    # переноса 1 в предпоследнем разряде
    for i in range(len(acopy) - 1):
        summa = acopy[i] + b[i]
        if (summa >= base):
            acopy[i + 1] += 1
            summa -= base
        c.append(summa)
    return c

# Выводим список на экран
def printData(a):
    # p - маркер номера позиции, в которой
    # в списке находится "не ноль"
    # Задаём индекс последнего элемента
    p = len(a) - 1

    # Пока первый с конца элемент = 0, уменьшаем p
    while (a[p] == 0 and p >= 0):
        p -= 1

    # Если нет значений, кроме нуля
    if (p == -1):
        print(0)
    else:
        # Перебераем значения и выводим их на экран
        for i in range(p, -1, -1):
            print(a[i], end="")
        print()

# Работаем в десятичной
base = 10

# Длина чисел
n = 1000

# Заполняем списки рандомно от 0 до
# base (в системе счисления не может быть
# знака больше или равного основанию)
a = [random.randint(0, base - 1) for i in range(n)]
b = [random.randint(0, base - 1) for i in range(n)]

# Запасные ячейки, чтобы
# при сложении не выйти за границы списка
for i in range(2):
    a.append(0)
    b.append(0)

# Считаем в список "c" сумму
c = summLong(a, b, base)

print("Первое число:")
printData(a)
print("\nВторое число:")
printData(b)
print("\nСумма:")
printData(c)