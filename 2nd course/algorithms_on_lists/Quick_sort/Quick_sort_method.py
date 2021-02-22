# Быстрая сортировка Quick Sort
def qsort(a, startElement, endElement):
    # Если левая граница больше правой,
    # то прерываем метод с помощью return
    if (startElement >= endElement):
        return

    # 1. С помощью среднего арифметического списка a
    average = sum(a[startElement:endElement]) // (endElement - startElement)

    # 2. С помощью центрального элемента списка a
    #average = a[startElement + (endElement - startElement) // 2]

    # Запоминаем позиции
    first = startElement
    last = endElement

    while (first <= last):
        # Находим индекс левого элемента
        # который больше или равен опорному числу
        while (a[first] < average):
            first += 1

        # Находим индекс правого элемента,
        # который меньше или равен опорному числу
        while (a[last] > average):
            last -= 1

        if (first <= last):
            a[first], a[last] = a[last], a[first]
            first += 1
            last -= 1

    qsort(a, startElement, last)
    qsort(a, first, endElement)

a = [5, 8, 1, 5, 3, 5, 2, 0, 2, 5, 2]
print(a)
qsort(a, 0, len(a) - 1)
print(a)