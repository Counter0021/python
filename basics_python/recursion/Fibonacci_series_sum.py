# Сумма первых 10 чисел ряда Фибоначчи
def summDigit(a):
    if (a == []):
        return 0
    else:
        return a[0] + summDigit(a[1:])


a = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(summDigit(a))