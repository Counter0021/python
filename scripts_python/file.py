try:
    f = open("???.txt", "r", encoding="utf-8")
    a = f.readline()
    f.close()
except IOError:
    print("Ошибка открытия файла")
    a = 0
