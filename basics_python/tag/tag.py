from tkinter import *

# Radiobutton
from tkinter import ttk

from tkinter import messagebox

from random import randint

# Бипер (пищалка), генератор звука
from winsound import Beep

from time import sleep

# ====================== Функции и методы ======================
# Победная мелодия
def music():
    Beep(100, 100)
    Beep(200, 200)
    Beep(300, 250)

# Обновляем надписи
def refreshText():
    textSteps["text"] = f"Сделано ходов: {steps[diffCombobox.current()]}"
    textRecord["text"] = f"Рекорд ходов: {record[diffCombobox.current()]}"

# Сохраняем в файл рекорды пользователя
def saveRecords():
    global record
    # Открываем файл и записываем
    try:
        f = open("steps.dat", "w", encoding="utf-8")
        for i in range(len(steps)):
            # Проверка: чтобы побить рекорд, количество ходов для каждого уровня
            # должно быть > 0 и < предыдущего рекорда
            if (steps[i] > 0 and steps[i] < record[i]):
                record[i] = steps[i]
            f.write(str(record[i]) + "\n")
        f.close()
    # В случае ошибки
    except:
        messagebox.showinfo("Ошибка",
                            "Возникла проблема с файлом при сохранении очков")

# Возвращаем рекорды ходов
def getRecordSteps():
    try:
        m = []
        f = open("steps.dat", "r", encoding="utf-8")
        for line in f.readlines():
            m.append(int(line))
        f.close()
    except:
        # В случае ошибки создаём пустой список
        m = []

    # Проверяем: длина списка должна быть = 6!
    if (len(m) != 6):
        m = []
        for i in range(6):
            m.append(1000 + 1000 * i)

    return m

# Кнопка "Посмотреть, как должно быть" отпущена
def seeEnd(event):
    global dataImage
    Beep(1082, 25)
    for i in range(n):
        for j in range(m):
            # Восстанавливаем значения из copyData в dataImage
            dataImage[i][j] = copyData[i][j]

    # Обновляем окно
    updatePictures()

# Кнопка "Посмотреть, как должно быть" нажата
def seeStart(event):
    global copyData, dataImage
    Beep(1632, 25)
    for i in range(n):
        for j in range(m):
            # Передаём значения напрямую, фактически копируя их
            copyData[i][j] = dataImage[i][j]

            # Формируем собранное поле, устанавливая значения 0-15 включительно
            dataImage[i][j] = i * n + j

    # Обновляем окно
    updatePictures()

# Выбор изображения
def isCheckImage():
    global imageBackground
    # Если в image содержится True
    if (image.get()):
        # То ставим imageBackground01
        imageBackground = imageBackground01
        Beep(1000, 25)
    else:
        # Иначе ставим imageBackground02
        imageBackground = imageBackground02
        Beep(1300, 25)

    updatePictures()

# Нажимаем на спрайт
def go(x, y):
    global steps, playGame

    if (x + 1 < n and dataImage[x + 1][y] == blackImg):
        exchangeImage(x, y, x + 1, y)
    elif (x - 1 >= 0 and dataImage[x - 1][y] == blackImg):
        exchangeImage(x, y, x - 1, y)
    elif (y + 1 < m and dataImage[x][y + 1] == blackImg):
        exchangeImage(x, y, x, y + 1)
    elif (y - 1 >= 0 and dataImage[x][y - 1] == blackImg):
        exchangeImage(x, y, x, y - 1)
    else:
        Beep(500, 100)
        return 0

    Beep(1400, 5)
    # Если игра идёт и метод продолжает выполняться (не сработала строка return 0),
    # то добавляем +1 ход
    if (playGame):
        steps[diffCombobox.current()] += 1
        refreshText()

        # Заранее предполагаем, что пользователь выиграл. Задача алгоритма -
        # доказать, что это не так
        win = True

        # В циклах обходим весь список dataImage
        for i in range(n):
            for j in range(m):
                # Контролируем, если правая нижняя клетка,
                # то сравниваем с blackImg
                if (i == n - 1 and j == m - 1):
                    win = win and dataImage[i][j] == blackImg

                # Иначе сравниваем с рядом чисел от 0 до 14 включительно
                else:
                    win = win and dataImage[i][j] == i * n + j

        if (win):
            # Устанавливаем вместо свободного поля спрайт правого нижнего угла
            # для целостности изображения
            dataImage[n - 1][m - 1] = blackImg - 1
            # Обновляем Label
            updatePictures()

            # Вывод окна-сообщения
            messagebox.showinfo("Браво!", "Вы одолели эту игру!")

            # Проигрываем победную мелодию
            music()

            # Сохраняем рекорды
            saveRecords()
            # Игра окончена
            playGame = False
            # Обновляем текст
            refreshText()
            resetPictures()


# Обновление всех изображений
def updatePictures():
    # С помощью цикла проходим все labelImage[][], устанавливая в них необходимые изображения
    for i in range(n):
        for j in range(m):
            labelImage[i][j]["image"] = \
                imageBackground[dataImage[i][j]]

    root.update()

# Сброс игрового поля
def resetPictures():
    global dataImage, steps, playGame

    steps[diffCombobox.current()] = 0
    playGame = False

    # Настраиваем состояние виджетов
    startButton["state"] = NORMAL
    resetButton["state"] = DISABLED
    diffCombobox["state"] = "readonly"
    radio01["state"] = NORMAL
    radio02["state"] = NORMAL

    # Заполняем dataImage[][] первоначальными
    # значениями (список должен содержать последовательность от 0 до 15 включительно)
    for i in range(n):
        for j in range(m):
            dataImage[i][j] = i * n + j

    # Задаём пустое поле
    dataImage[n - 1][m - 1] = blackImg

    # Победные сигналы
    Beep(800, 50)
    Beep(810, 35)

    # Перерисовываем экран
    updatePictures()
    refreshText()

# Обмен изображений
def exchangeImage(x1, y1, x2, y2):
    global dataImage, labelImage

    # Изменяем математическую модель
    dataImage[x1][y1], dataImage[x2][y2] = \
            dataImage[x2][y2], dataImage[x1][y1]

    # Получаем изображение по номеру из dataImage и устанавливаем его в labelImage
    labelImage[x1][y1]["image"] = imageBackground[dataImage[x1][y1]]
    labelImage[x2][y2]["image"] = imageBackground[dataImage[x2][y2]]

    root.update()
    sleep(0.01)

# Перемешиваем
def shufflePictures(x, y):
    if (diffCombobox.current() < 5):
        # Количество перемешиваний в зависимости от уровня сложности
        count = (2 + diffCombobox.current()) ** 4

        # Запрет направления
        noDirection = 0

        # ===============================================================================================
        # Решение проблемы с количеством итераций: перемещения спрайтов горонтированные, если был бы цикл for,
        # то при не выполнении условий, он защитывал бы всё равно +1 итерация, теперь только при выполнении условия
        # +1 итерация.
        # ===============================================================================================

        # Счётчик чистых перемещений спрайтов, нужен для избежаня проблемы выше ^
        countNoFail = 0

        # Повторение перемешиваний
        while(countNoFail < count):
            # Задаём заведомо истинную комбинацию для while
            direction = noDirection

            # Получаем число, ТОЧНО не повторяющее предыдущее
            while (direction == noDirection):
                direction = randint(0, 3)

            # Вниз
            if (direction == 0 and x + 1 < n):
                # Обмениваем текущую и спрайт ниже
                exchangeImage(x, y, x + 1, y)

                # Увеличиваем x, т.к. пустое место переместилось в новую позицию x + 1
                x += 1

                # Запрещаем направление. Следующее direction не должно равняться числу 1,
                # которое символизирует обмен с верхней плиткой
                noDirection = 1

                # Увеличиваем счётчик на 1 (чистое перемещение спрайтов)
                countNoFail += 1

            # Вверх
            elif (direction == 1 and x - 1 >= 0):
                exchangeImage(x, y, x - 1, y)
                x -= 1
                noDirection = 0
                countNoFail += 1

            # Вправо
            elif (direction == 2 and y + 1 < m):
                exchangeImage(x, y, x, y + 1)
                y += 1
                noDirection = 3
                countNoFail += 1

            # Влево
            elif (direction == 3 and y - 1 >= 0):
                exchangeImage(x, y, x, y - 1)
                y -= 1
                noDirection = 2
                countNoFail += 1
    else:
        exchangeImage(n - 1, m - 3, n - 1, m - 2)

    Beep(1750, 50)
    resetButton["state"] = NORMAL

# Стартуем
def startNewRound():
    global steps, playGame

    # Игра началась
    playGame = True

    # Обнуляем шаги для текущего уровня
    steps[diffCombobox.current()] = 0

    # Сбрасываем кнопки и радиопереключатели
    diffCombobox["state"] = DISABLED
    startButton["state"] = DISABLED
    radio01["state"] = DISABLED
    radio02["state"] = DISABLED

    # Проигрываем звуковой сигнал
    Beep(750, 50)

    # Находим координаты пустого поля простым перебором каждого элемента двумерного списка dataImage[][]
    x = 0
    y = 0
    for i in range(n):
        for j in range(m):
            # При совпадении числа в dataImage[][]
            # с номером "пустого поля", передаём в x и y счётчики циклов, ведь их значения и есть искомые координаты
            if (dataImage[i][j] == blackImg):
                x = i
                y = j
                break
    # Запускаем метод и перемешиваем
    shufflePictures(x, y)
    refreshText()

# ====================== Начало программы ======================
# Создание окна
root = Tk()
root.resizable(False, False)
root.title("Головоломка для самых умных")

# Иконка
root.iconbitmap("icon/icon.ico")

# Цвета
back = "#373737"
fore = "#AFAFAF"

# Геомтрия окна
WIDTH = 422
HEIGHT = 730
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

# Установка фона
root["bg"] = back

# ====================== Надписи и кнопки ======================

# Кнопка ПОСМОТРЕТЬ СОБРАННОЕ
seeButton = Button(root, text="Посмотреть, как должно быть", width=56)
seeButton.place(x=10, y=620)
seeButton.bind("<Button-1>", seeStart)
seeButton.bind("<ButtonRelease>", seeEnd)

# Кнопка СТАРТ
startButton = Button(text="СТАРТ", width=56)
startButton.place(x=10, y=650)
startButton["command"] = startNewRound

# Кнопка СБРОС
resetButton = Button(root, text="СБРОС", width=56)
resetButton.place(x=10, y=680)
resetButton["command"] = resetPictures

# Метка для вывода текста с количеством сделанных ходов и рекордом текущего уровня
textSteps = Label(root, bg=back, fg=fore)
textSteps.place(x=10, y=550)
textRecord = Label(root, bg=back, fg=fore)
textRecord.place(x=10, y=570)

# Метка сложности без переменной (не будет изменяться)
Label(root, bg=back, fg=fore, text="Сложность:").place(x=267, y=550)

# Названия степеней сложности перемешивания
itemDiff = ["Только начал", "Немного почитал", "Знаю print()", "Понял сортировку", "Изучил лабиринт", "Задонатил!"]

# Выпадающий список
diffCombobox = ttk.Combobox(root, width=20, values=itemDiff, state="readonly")
diffCombobox.place(x=270, y=570)

# Метод refreshText()
diffCombobox.bind("<<ComboboxSelected>>", lambda e: refreshText())

# Выбираем 0 пункт: сложность "Только начал"
diffCombobox.current(0)

# Радиопереключатели
# Создаём переменную
image = BooleanVar()
# Устанавливаем значение
image.set(True)

# Создаём радио-кнопку и привязываем к ней переменную image
radio01 = Radiobutton(root, text="Космос", variable=image, value=True, activebackground=back, bg=back, fg=fore)
radio02 = Radiobutton(root, text="Природа", variable=image, value=False, activebackground=back, bg=back, fg=fore)
radio01["command"] = isCheckImage
radio02["command"] = isCheckImage
radio01.place(x=150, y=548)
radio02.place(x=150, y=568)

# ====================== Изображения ======================

# Размер поля
n = 4
m = 4

# Размер полного изображения
pictureWidth = 400
pictureHeight = 532

# Ширина и высота 1 спрайта
widthPic = pictureWidth / n
heightPic = pictureHeight / m

fileName = ["img01.png",
            "img02.png",
            "img03.png",
            "img04.png",
            "img05.png",
            "img06.png",
            "img07.png",
            "img08.png",
            "img09.png",
            "img10.png",
            "img11.png",
            "img12.png",
            "img13.png",
            "img14.png",
            "img15.png",
            "img16.png",
            "black.png"]

# Списки для хранения изображений
imageBackground = []    # АКТИВНОЕ ИЗОБРАЖЕНИЕ
imageBackground01 = []  # Космос
imageBackground02 = []  # Природа

# Добавляем в сиски элементы и загружаем в них объекты PhotoImage
for name in fileName:
    imageBackground01.append(PhotoImage(file="image01/" + name))
    imageBackground02.append(PhotoImage(file="image02/" + name))

# Номер пустого поля
blackImg = 16

# Устанавливаем набор спрайтов "КОСМОС"
imageBackground = imageBackground01

# Метки Label
labelImage = []

# Математическая модели игрового поля
dataImage = []

# Для создания копии модели игрового поля при просмотре по кнопке "Посмотреть, как должно быть"
copyData = []

for i in range(n):
    # Начинаем заполнять списки
    labelImage.append([])
    dataImage.append([])
    copyData.append([])

    for j in range(m):
        # Формула i * n + j сгенерирует ряд чисел 0, 1, 2, 3...
        # Это и есть номера собранной версии изображения
        dataImage[i].append(i * n + j)
        copyData[i].append(i * n + j)

        # Создаём и настраиваем Label, в который будем выводить PhotoImage из imageBackground
        labelImage[i].append(Label(root, bg=back))
        labelImage[i][j]["bd"] = 1      # Граница 1 пиксель
        labelImage[i][j].place(x=10 + j * widthPic, y=10 + i * heightPic)

        # Что произойдёт при нажатии на Label
        labelImage[i][j].bind("<Button-1>", lambda e, x=i, y=j: go(x, y))

        # Устанавливаем изображение
        labelImage[i][j]["image"] = \
            imageBackground[dataImage[i][j]]

# ======================== Ходы ========================
steps = [0, 0, 0, 0, 0, 0]

# Началась ли игра?
playGame = False

# Наименьшее количество шагов для сбора головоломки
record = getRecordSteps()

# Обновляем текст
refreshText()

# Обновляем изображения
resetPictures()

# Запуск
root.mainloop()