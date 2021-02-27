# Возвращает отсортированный двумерный список
def getSortedArray(myList):
    l = []

    # Преобразуем в одномерный список
    for i in range(len(myList)):
        for j in range(len(myList[i])):
            l.append(myList[i][j])

    # Сортировка вставками
    #for i in range(1, len(l)):
    #    n = l[i]
    #    j = i - 1
    #    while (j >= 0 and l[j] > n):
    #        l[j + 1] = l[j]
    #        j -= 1
    #    l[j + 1] = n

    # Используем встроенную сортировку
    l = sorted(l)

    # Преобразуем обратно в двумерный последовательно
    for i in range(len(myList)):
        for j in range(len(myList[i])):
            myList[i][j] = l[i * len(myList) + j]

    return myList

a = [[16, 6, 10, 7],
     [5, 12, 13, 14],
     [3, 9, 15, 11],
     [1, 4, 8, 2]]

print(f"Исходный список:\n{a}")
a = getSortedArray(a)
print(f"Отсортированный список:\n{a}")