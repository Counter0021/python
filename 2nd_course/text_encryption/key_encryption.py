import random

# Функция шифровки и расшифровки
def crypt(s, key):
    # Длина ключа
    lenKey = len(key)
    # Стартовая позиция
    start = 0
    # Номер элемента в списке swaps
    p1 = 0

    # Добавляем "левые" символы, Если длина не кратна длине "ключа"
    if (len(s) % lenKey != 0):
        for i in range(lenKey - len(s) % lenKey):
            s += chr(random.randint(ord("!"), ord("=")))

    # Длина шифруемой строки
    lenS = len(s)
    # Накопитель для зашифрованной строки
    sEncrypt = ""

    while (start + lenKey < lenS + 1):
        # Добавляем символ по позиции из swaps
        sEncrypt += s[start + key[p1] - 1]
        # Увеличиваем счётчик элемента в swaps
        p1 += 1
        # Как только достигает длины "ключа", сбрасываем на ноль и перемещаем позицию start
        if (p1 == lenKey):
            p1 = 0
            start += lenKey

    # Возвращаем зашифрованную строку
    return sEncrypt


# Ключ шифрования
encryptKey = [3, 6, 4, 2, 1, 5]

# Ключ дешифровки
decryptKey = [5, 4, 1, 3, 6, 2]

# Выдача шифрованной информации
stringCrypt = crypt("На мели мы налимов лениво ловили, это зашифровано", encryptKey)
print(" Зашифровано:", stringCrypt)

# Выдача расшифрованной информации
stringCrypt = crypt(stringCrypt, decryptKey)
print("Расшифровано:", stringCrypt)