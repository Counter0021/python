# Метод выводящий список на экран
def printList2D(lst):
    # Формируем внешний цикл до len(lst) - количества строк
    for i in range(len(lst)):
        # Цикл до длины текущей строки (lst[i])
        for j in range(len(lst[i])):
            print(f"{lst[i][j]} ", end="")
        # Переносим строку
        print()


# Строки
n = int(input("Введите количество строк: "))
# Столбцы
m = int(input("Введите количество столбцов: "))

# Создание списка
a = []

# Цикл ввода с клавиатуры
for i in range(n):
    a.append([])
    for j in range(m):
        x = int(input(f"Введите число для [{i}][{j}]: "))
        a[i].append(x)

# printList2D(СПИСОК)
printList2D(a)
