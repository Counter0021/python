def isDigit(s):
    res = True
    startCode = ord("0")
    stopCode = ord("9")
    tochka = ord(".")
    p = 0
    while (p < len(s) and res):
        if (ord(s[p]) < startCode or ord(s[p]) > stopCode):
            if (ord(s[p]) == tochka):
                print("Число вещественное")
            res = False
        p += 1
    return res

stroka = "123123"
print(f"Состоит ли строка {stroka} из цифр (True) или в ней есть символы (False)?")
print(f"Функция вернула: {isDigit(stroka)}")

stroka = "1000.23"      #Есть точка
print(f"Состоит ли строка {stroka} из цифр (True) или в ней есть символы (False)?")
print(f"Функция вернула: {isDigit(stroka)}")

stroka = "Я строка"
print(f"Состоит ли строка {stroka} из цифр (True) или в ней есть символы (False)?")
print(f"Функция вернула: {isDigit(stroka)}")