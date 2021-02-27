import random

toCode = "0123456789ABCDEGHIJKLMNOPQRSTUVWXYZВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
sIn = input("ВВедите строку для шифрования: ").upper()
sOut = ""

for i in range(len(sIn)):
    count = random.randint(0, 10)
    for j in range(count):
        sOut += toCode[random.randint(0, len(toCode) - 1)]
    if (sIn[i] == " "):                 #Если пробел ставим символ "F"
        sOut += "F"                     #Иначе ставим "А" или "Б"
    elif (random.randint(0, 1) == 1):
        sOut += "А"
    else:
        sOut += "Б"
    sOut += sIn[i]

#Добавляем букву вместо пробела
l = sOut.split()
sOut1 = toCode[random.randint(0, len(toCode) - 1)].join(l)
print(f"Зашифрованная строка: {sOut1}")