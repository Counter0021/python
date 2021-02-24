# Считывает из файла, формирует и возвращает двумерный список данных
def getFileString(filename):
    # Создаём список, который вернём
    ret = []

    # Потенциальная небезовасная операция
    try:
        # Получаем "паспорт" файла в переменную f
        f = open(filename, "r", encoding="utf-8")

        # Обрабатываем каждую строку информации из файла
        for line in f.readlines():
            line = line.replace("\n", "")
            line = line.split("#")
            ret.append(line)

        # Обязательно закрываем паспорт-дескриптор
        f.close()

    except:
        # Если что-то пошло не так
        print("Ошибка открытия! Проверьте правильность имени и пути.")

    # Вернём сформированный список
    return ret

# Среднее значение по строке line
def getAverage(line):
    ret = 0
    summa = 0
    count = 0

    for i in range(1, len(line)):
        if (line[i].isdigit()):         # Есть ли в элементе списка число?
            summa += int(line[i])       # Суммируем элементы
            count += 1                  # Для подсчёта среднего нужно количество элементов

    # Вычисляем среднее значение
    ret = summa / count
    # Округляем значение
    ret = int(ret * 10) / 10

    return ret

# Формируем и возвращаем текст для записи в файл
def getStringToFile(arr):
    ret = ""
    for i in range(len(arr)):
        ret += arr[i][0] + "#" + str(getAverage(arr[i])) + "\n"
    return ret

# Запись переданной информации в файл
def saveToFile(strToFile, filename):
    try:
        f = open(filename, "w", encoding="utf-8")
        f.write(strToFile)
        f.close()
    except:
        print("Ошибка создания файла.")

journal = getFileString("journal.dat")

for i in range(len(journal)):
    print(f"{journal[i][0]}, средняя оценка {getAverage(journal[i])}")

saveToFile(getStringToFile(journal), "average.dat")