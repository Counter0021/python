# Строка с текстом для расшифровки
sOld = input("Введите строку для расшифровки: ")

# Строка с расшифрованным текстом
sNew = ""

# Переменная, хранящая прибавляемое значение
code = 0

# Перебираем символы в sOld
for i in sOld:
    # Добавляем к новой строке, получая и увеличивая код символа, преобразуя в символ
    sNew += chr(ord(i) - (code % 10) - 1)
    # Увеличиваем прибавляемое к коду символа
    code += 1

print(sNew)