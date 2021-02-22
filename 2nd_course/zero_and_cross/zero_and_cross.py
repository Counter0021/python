from tkinter import *
from random import randint
from tkinter import messagebox
from time import sleep

# ====================== Функции и методы ======================
# Сохраняем количество побед в файл
def saveStat():
    # Открываем файл и записываем
    try:
        f = open("steps.dat", "w", encoding="utf-8")
        for i in range(len(steps)):
            f.write(str(steps[i]) + "\n")
        f.close()
    # В случае ошибки
    except:
        messagebox.showinfo("Ошибка",
                            "Возникла проблема с файлом при сохранении очков")

# Возвращаем рекорды побед
def getStat():
    try:
        m = []
        f = open("steps.dat", "r", encoding="utf-8")
        for line in f.readlines():
            m.append(int(line))
        f.close()
    except:
        # В случае ошибки создаём пустой список
        m = []

    # Проверяем: длина списка должна быть = 2!
    if (len(m) != 2):
        m = []
        for i in range(2):
            m.append(0)

    return m

# Обновляем надписи
def refreshText():
    winHumanLabel["text"] = f"Человек выиграл:   {steps[0]} раундов"
    winBotLabel["text"] = f"Бот выиграл:            {steps[1]} раундов"

# Проверка поля для нолика
def draw():
    count = 0
    if (playGame == True and win == 0):
        for i in range(n):
            for j in range(m):
                if (dataImage[i][j] != 0):
                    count += 1
        if (count == 9):
            messagebox.showinfo("Ничья", "Игра окончена")
            resetPictures()

# Сбросс игры
def resetPictures():
    global dataImage, playGame, play, win, gamer

    gamer = False
    win = 0
    play = 0
    playGame = False
    startButton["state"] = NORMAL
    resetButton["state"] = DISABLED
    radio01["state"] = NORMAL
    radio02["state"] = NORMAL

    # Заполняем dataImage[][] первоначальными
    # значениями
    for i in range(n):
        for j in range(m):
            dataImage[i][j] = 0

    # Обновляем
    updatePictures()
    refreshText()

# Проверка выигрыша
def winRound(playGames):
    global win, playGame
    if (playGames):
        for i in range(n):
            for j in range(m):
                # Проверка совпадений по горизонтали
                if (dataImage[i][0] == mode and dataImage[i][1] == mode and dataImage[i][2] == mode):
                    playGame = False
                    win = 1
                elif (dataImage[i][0] == modeBot and dataImage[i][1] == modeBot and dataImage[i][2] == modeBot):
                    playGame = False
                    win = 2

                # Проверка совпадений по вертикали
                if (dataImage[0][j] == mode and dataImage[1][j] == mode and dataImage[2][j] == mode):
                    playGame = False
                    win = 1
                elif (dataImage[0][j] == modeBot and dataImage[1][j] == modeBot and dataImage[2][j] == modeBot):
                    playGame = False
                    win = 2

                # Проверка по диагонали
                if ((dataImage[1][1] == mode and dataImage[0][0] == mode and dataImage[2][2] == mode) \
                        # Диагональ справа на лево
                        or (dataImage[1][1] == mode and dataImage[0][2] == mode and dataImage[2][0] == mode)):
                    playGame = False
                    win = 1
                elif ((dataImage[1][1] == modeBot and dataImage[0][0] == modeBot and dataImage[2][2] == modeBot) \
                        or (dataImage[1][1] == modeBot and dataImage[0][2] == modeBot and dataImage[2][0] == modeBot)):
                    playGame = False
                    win = 2
        return win, playGame
    else:
        return 0

# Обновление всех изображений
def updatePictures():
    # С помощью цикла проходим все labelImage[][], устанавливая в них необходимые изображения
    for i in range(n):
        for j in range(m):
            labelImage[i][j]["image"] = \
                imageBackground[dataImage[i][j]]
    root.update()

# Режим бота
def checkImgBot():
    global modeBot

    # Узнаём режим бота
    if (image.get()):
        modeBot = 2
    else:
        modeBot = 1

# Выбор режима: крестик или нолик
def checkImage():
    global mode

    # Узнаём режим пользователя
    if (image.get()):
        mode = 1
    else:
        mode = 2

# Ставим крестик или нолик
def go(x, y):
    global dataImage, labelImage, gamer, play, steps
    # Если на картинке пустое поле
    if (dataImage[x][y] == 0):
        dataImage[x][y] = mode
        labelImage[x][y]["image"] = imageBackground[dataImage[x][y]]
    elif (dataImage[x][y] == 1 or dataImage[x][y] == 2):
        gamer = False
        messagebox.showinfo("Нажмите на другую клетку!", "Вы нажали уже на занятую клетку!")
        return 0
    root.update()

    # Игрок походил
    gamer = True
    # Победил ли кто-нибудь?
    winRound(playGame)

    # Бот ходит
    bot()
    # Увеличиваем, показывая боту, что это не 1 ход пользователя, если выбран нолик в качестве режима
    play += 1
    # Победил ли кто-нибудь?
    winRound(playGame)
    # Если игрок выиграл
    if (playGame == False and win == 1):
        messagebox.showinfo("КРОССАВЧИК", "Ты победил бота!")
        resetPictures()
        steps[0] += 1
        saveStat()
    # Если выиграл бот
    elif (playGame == False and win == 2):
        messagebox.showinfo("Печалька", "Ты проиграл боту!")
        resetPictures()
        steps[1] += 1
        saveStat()
    refreshText()
    #print(dataImage)

# Выбор режима бота и ход бота
def bot():
    global dataImage, gamer

    checkImgBot()
    # Если ходы ещё есть
    try:
        if (mode == 2 and play == 0):
            dataImage[randint(0, len(dataImage) - 1)][randint(0, len(dataImage) - 1)] = modeBot
            updatePictures()
        else:
            # Ход бота, игрок походил
            if (gamer == True):
                # Рандом хода бота
                i = randint(0, len(dataImage) - 1)
                j = randint(0, len(dataImage) - 1)
                # Он может походить только если клетка пуста
                if (dataImage[i][j] == 0):
                    dataImage[i][j] = modeBot
                    sleep(0.1)
                    updatePictures()
                    gamer = False
                else:
                    bot()

    # Если игра зашла в тупик
    except:
        winRound(playGame)
    #print(dataImage)
    winRound(playGame)
    draw()

def startNewRound():
    global playGame

    # Игра началась
    playGame = True

    # Сбрасываем кнопки
    startButton["state"] = DISABLED
    radio01["state"] = DISABLED
    radio02["state"] = DISABLED
    resetButton["state"] = NORMAL
    # Запуск бота
    bot()
    # Проверка победы
    winRound(playGame)

    refreshText()

# ====================== Начало программы ======================
# Создание окна
root = Tk()
root.resizable(False, False)
root.title("Крестики-нолики")

# Цвет окна
back = "gray"

# Геомтрия окна
WIDTH = 800
HEIGHT = 900
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

root["bg"] = back

# ====================== Надписи и кнопки ======================
# Кнопка СТАРТ
startButton = Button(text="СТАРТ", width=56, bg="green", fg="white", activebackground="green")
startButton.place(x=230, y=750)
startButton["command"] = startNewRound

# Кнопка СБРОС
resetButton = Button(text="СБРОС", width=56, bg="red", fg="white", activebackground="red")
resetButton.place(x=230, y=780)
resetButton["command"] = resetPictures

# Радиопереключатели
# Создаём переменную
image = BooleanVar()
# Устанавливаем значение
image.set(True)

radio01 = Radiobutton(root, text="Крестик", variable=image, value=True, activebackground=back, bg=back)
radio02 = Radiobutton(root, text="Нолик", variable=image, value=False, activebackground=back, bg=back)
radio01["command"] = checkImage
radio02["command"] = checkImage
radio01.place(x=150, y=800)
radio02.place(x=150, y=850)

# Устанавливаем метки побед бота и человека
winBotLabel = Label(root, bg=back)
winBotLabel.place(x=300, y=810)
winHumanLabel = Label(root, bg=back)
winHumanLabel.place(x=300, y=830)

# ====================== Изображения ======================

# Размер поля
n = 3
m = 3

# Размер полного изображения
pictureWidth = 800
pictureHeight = 800

# Ширина и высота 1 спрайта
widthPic = pictureWidth / n
heightPic = pictureHeight / m

imageBackground = [PhotoImage(file="field.png"),
                   PhotoImage(file="cross.png"),
                   PhotoImage(file="zero.png")]

# Метки Label
labelImage = []

# Математическая модели игрового поля
dataImage = []

for i in range(n):
    # Начинаем заполнять списки
    labelImage.append([])
    dataImage.append([])

    for j in range(m):
        # Формула i * n + j сгенерирует ряд чисел 0, 1, 2, 3...
        # Это и есть номера собранной версии изображения
        dataImage[i].append(0)

        # Создаём и настраиваем Label, в который будем выводить PhotoImage из imageBackground
        labelImage[i].append(Label(root, bg=back))
        labelImage[i][j]["bd"] = 1      # Граница 1 пиксель
        labelImage[i][j].place(x=10 + j * widthPic, y=10 + i * heightPic)

        # Что произойдёт при нажатии на Label
        labelImage[i][j].bind("<Button-1>", lambda e, x=i, y=j: go(x, y))

        # Устанавливаем изображение
        labelImage[i][j]["image"] = \
            imageBackground[dataImage[i][j]]

# Игра началась?
playGame = False

# Режимы по умолчанию
# Игрок
mode = 1
# Бот
modeBot = 2

# Игрок походил?
gamer = False

# Игра только началась, нужно при выборе игры за "Нолик", чтобы бот походил 1
play = 0

# Список побед
steps = getStat()

# Победитель
# 1 - Челове
# 2 - БОТ
win = 0

# Обновляем изображения
resetPictures()

# Запуск
root.mainloop()