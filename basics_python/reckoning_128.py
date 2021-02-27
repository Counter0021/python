import random

# Суммирование длинных чисел
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
            print(alphabet[a[i]], end="")
        print()

# Перевод число из системы с
# основанием osnovanie в десятичную
def getData(a, osnovanie):
    d = 0
    lenght = len(a)
    for i in range(lenght):
        d += a[i] * osnovanie ** i
    return d

# Функция перевода из 10-чной
# в систему счисления X
def toBase(x, base):
    # Список с возвращаемым результатом
    ret = []

    # Пока x не "исчерпает себя"
    while (x > 0):
        # Добавляем остаток от деления в возвращаемый список
        ret.append(x % base)

        # Уменьшаем x
        x //= base

    # Добавляем 2 дополнительный
    # разряда в конец списка для
    # ого, чтобы при суммировании не
    # было ошибок и возвращаем список
    ret.append(0)
    ret.append(0)
    return ret

# ================================
#         Основное тело
# ================================

# 128 символов
alphabet = "0123456789"
alphabet += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet += "abcdefghijklmnopqrstuvwxyz"
alphabet += "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
alphabet += "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

printData(toBase(75, 2))
printData(toBase(176, 16))

n = 5
base = 100

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
print(f"В десятичной: {getData(a, base)}")

print("\nВторое число:")
printData(b)
print(f"В десятичной: {getData(b, base)}")

print("\nСумма:")
printData(c)
print(f"В десятичной: {getData(c, base)}")