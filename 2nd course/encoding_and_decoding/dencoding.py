sIn = input("ВВедите строку для шифрования: ")
sOut = ""

p1 = 0
while (p1 < len(sIn)):
    if (sIn[p1] == "F"):                    #Если есть символ "F", то sOut += " "(пробел)
        sOut += " "                         #Если есть "А" или "Б", то sOut += симво после
    if (sIn[p1] == "А" or sIn[p1] == "Б"):
        sOut += sIn[p1 + 1]
        p1 += 2
    else:
        p1 += 1

print(sOut)