#Превый способ
def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

x33 = False
while (x33 != True):
    x3 = input("x1 =")
    x33 = is_digit(x3)

x44 = False
while (x44 != True):
    x4 = input("x2 =")
    x44 = is_digit(x4)
x3 = float(x3)
x4 = float(x4)

#Второй способ
def isDigit(s):
    res = True
    startCode = ord("0")
    stopCode = ord("9")
    minus = ord("-")
    p = 0
    while (p < len(s) and res):
        if ((ord(s[p]) < startCode or ord(s[p]) > stopCode) and not(ord(s[p]) == minus)):
            res = False
        p += 1
    return res

stroka = "123123"
print(f"Состоит ли строка {stroka} из цифр (True) или в ней есть символы (False)?")
print(f"Функция вернула: {isDigit(stroka)}")

stroka = "-1"
print(f"Состоит ли строка {stroka} из цифр (True) или в ней есть символы (False)?")
print(f"Функция вернула: {isDigit(stroka)}")