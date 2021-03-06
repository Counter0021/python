# Поиск пути в лабиринте
# Рекурсивный метод ПОИСКА ПУТИ
def finPath(a, x, y, number):
    # Маркируем текущую клетку (x, y)
    a[x][y] = number

    # Путь вниз
    if (a[x + 1][y] == 0):
        finPath(a, x + 1, y, number + 1)

    # Путь вправо
    if (a[x][y + 1] == 0):
        finPath(a, x, y + 1, number + 1)

    # Путь влево
    if (a[x][y - 1] == 0):
        finPath(a, x, y - 1, number + 1)

    # Путь вверх
    if (a[x - 1][y] == 0):
        finPath(a, x - 1, y, number + 1)

# Крутой вывод на экран
def printLab(a):
    # Перебираем список
    for i in a:
        for j in i:
            # Если = 0, то выводим ЧЕТЫРЕ ПРОБЕЛА
            # end="" означает отмену переноса строки
            if (j == 0):
                print("    ", end="")
            # Если -1, то выводим 4 звёздочки
            elif (j == -1):
                print("*" * 4, end="")
            else:
                # Если число < 10, то добавляем в начале 0 (01, 02, 03).
                if (j < 10):
                    print(f" 0{j} ", end= "")
                else:
                    print(f" {j} ", end="")
        print()
    print()

# Получаем координаты найденного пути
def getRoad(a, x, y):
    res = []

    res.append([x, y])
    if (a[x + 1][y] == a[x][y] - 1):
        return res + getRoad(a, x + 1, y)
    if (a[x - 1][y] == a[x][y] - 1):
        return res + getRoad(a, x - 1, y)
    if (a[x][y + 1] == a[x][y] - 1):
        return res + getRoad(a, x, y + 1)
    if (a[x][y - 1] == a[x][y] - 1):
        return res + getRoad(a, x, y - 1)

    return res

# Создаём двумерный список с данныйми лабиринта
a = []
a.append([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1])
a.append([-1,  0, -1,  0,  0,  0, -1,  0,  0,  0, -1])
a.append([-1,  0,  0,  0, -1,  0, -1,  0, -1,  0, -1])
a.append([-1,  0, -1,  0, -1,  0,  0,  0, -1,  0, -1])
a.append([-1,  0, -1,  0, -1, -1, -1, -1, -1,  0, -1])
a.append([-1,  0, -1,  0,  0,  0,  0,  0, -1,  0, -1])
a.append([-1,  0, -1, -1, -1, -1, -1, -1, -1,  0, -1])
a.append([-1,  0,  0,  0,  0,  0,  0,  0, -1,  0, -1])
a.append([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1])

# ***********************************
#      Основное тело программы
# ***********************************

# Вывод списка с лабиринтом ввиде лабиринта
print("До обработки:")
printLab(a)

# Ищем путь из точки с координатами 1, 1
finPath(a, 1, 1, 1)

# Выводим список с указывающими путь цифрами в клетках
print("После обработки:")
printLab(a)

road = getRoad(a, 7, 9)
road.reverse()

print("Координаты пути:")
for i in road:
    print(i)