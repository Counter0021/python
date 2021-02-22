def stringSort(s):
    ret = ""

    # Список для кодов
    code = []

    # Формируем список кодов
    for i in s:
        code.append(ord(i))

    # Сортировка вставками
    for i in range(1, len(code)):
        n = code[i]
        j = i - 1
        while (j >= 0 and code[j] > n):
            code[j + 1] = code[j]
            j -= 1
        code[j + 1] = n

    # Формируем строку по кодам
    for i in code:
        ret += chr(i)

    # Возвращаем результат
    return ret

m = "ЯЮЭЬЫЪЩШЧЦХФУТСРПОНМЛКЙИЗЖЕДГВБА"
m = stringSort(m)
print(m)