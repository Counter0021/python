from tkinter import *
from tkinter import messagebox
from random import randint

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
    if (len(m) != 2):
        m = []
        for i in range(2):
            m.append(0)

    return m

# Сохраняем в файл рекорды пользователя
def saveRecords():
    global record
    # Открываем файл и записываем
    try:
        f = open("steps.dat", "w", encoding="utf-8")
        for i in range(len(record)):
            if (countRed > record[0]):
                record[0] = countRed
            if (countGreen > record[1]):
                record[1] = countGreen
            f.write(str(record[i]) + "\n")
        f.close()
    # Если ошибка
    except:
        messagebox.showinfo("Ошибка",
                            "Возникла проблема с файлом при сохранении очков")

# Обновляем текст
def refreshText():
    countLabelRed["text"] = f"Игрок красной платформы забил: {countRed}"
    countLabelGreen["text"] = f"Игрок зелёной платформы забил: {countGreen}"
    recordRed["text"] = f"Рекорд красного игрока: {record[0]}"
    recordGreen["text"] = f"Рекорд зелёного игрока: {record[1]}"

# Расстояние от платформы до мяча
def distanceBall(x, y, platformX, platformY):
    global distance
    distance = [(abs(x - platformX) ** 2 + abs(y - platformY) ** 2) ** 0.5,
                (abs(x - platformX) ** 2 + abs(y - (platformY + 73)) ** 2) ** 0.5,
                (abs(x - platformX) ** 2 + abs(y - (platformY - 73)) ** 2) ** 0.5]

    return distance

# Кнопка куда идёт платформа зелёная
def moveButtonEvil(button):
    global buttEvil, buttNowEvil, vectorY_evil

    vectorY_evil = 5
    buttEvil = button

    buttNowEvil = buttEvil

    return buttNowEvil

# Кнопка куда идёт платформа красная
def moveButton(button):
    global butt, buttNow, vectorY_player

    vectorY_player = 5
    butt = button

    # Кнопка сейчас
    buttNow = butt
    return buttNow

# Движение платформы игрока
def move():
    global vectorY_player, afterPlayer, vectorY_evil, afterEvil, gamer

    # Передвигаем платформу
    if (buttNow == UPKEY):
        canvas.move(player, 0, -vectorY_player)
    elif (buttNow == DOWNKEY):
        canvas.move(player, 0, vectorY_player)

    if (buttNowEvil == WKEY):
        canvas.move(evil, 0, -vectorY_evil)
    elif (buttNowEvil == SKEY):
        canvas.move(evil, 0, vectorY_evil)

    # Получаем координаты платформы игрока в отдельные переменные
    y = canvas.coords(player)[1]
    yE = canvas.coords(evil)[1]

    # Проверка выхода за границы
    if (y > HEIGHT - 100 or y < 100):
        vectorY_player = -vectorY_player
    if (yE > HEIGHT - 100 or yE < 100):
        vectorY_evil = -vectorY_evil

    # Если кнопка сейчас == кнопке, то стоп рекурсии
    if (buttNow != butt and buttNowEvil != buttEvil):
        afterPlayer = root.after_cancel(move)
    else:
        afterPlayer = root.after(30, move)

# Рандом движения мяча
def ballDirection(x, y):
    global vectorX, vectorY, play
    direction = randint(0, 3)
    if (direction == 0):
        vectorX = -x
    elif (direction == 1):
        vectorY = -y
    elif (direction == 2):
        vectorX = -x
        vectorY = -vectorY
    elif (direction == 3):
        vectorX = x
        vectorY = y
    play += 1

# Движение мяча
def ballMove():
    global vectorX, vectorY, ballAfter, countGreen, countRed

    # Передвигаем мяч
    if (play == 0):
        ballDirection(vectorX, vectorY)
    canvas.move(ball, vectorX, vectorY)

    # Получаем координаты в отдельные переменные
    # cnv.coords возвращает список,
    # в котором на позиции 0 стоит координата x, на первой y
    x = canvas.coords(ball)[0]
    y = canvas.coords(ball)[1]

    # Проверяем: ударился ли второй красный круг о границы окна
    if (y > HEIGHT - 32 or y < 32):
        vectorY = -vectorY

    # Получаем координаты игрока красной и зелёной платформы
    xP = canvas.coords(player)[0]
    yP = canvas.coords(player)[1]

    xE = canvas.coords(evil)[0]
    yE = canvas.coords(evil)[1]

    # Узнаём дистанцию до мяча, чтобы платформа его оттолкнула
    if (x < 960):
        distanceBall(x, y, xE, yE)
    if (x > 960):
        distanceBall(x, y, xP, yP)
    for i in range(len(distance)):
        if (distance[i] < 61):
            vectorX = -vectorX
            vectorY = -vectorY

    # Если координаты x подошли к рамке окна, то останавливаем рекурсию
    if (x > WIDTH - 32 or x < 32):
        root.after_cancel(ballMove)
        # Если ушёл вправо
        if (x > WIDTH - 32):
            messagebox.showinfo("Победа!", "В этом раунде победил зелёный!")
            countGreen += 1
        # Если ушёл влево
        else:
            messagebox.showinfo("Победа!", "В этом раунде победил красный!")
            countRed += 1
        saveRecords()
        # Обновляем виджеты
        refreshText()
        # Сбрасываем раунд
        reset()
    else:
        # Если нет
        ballAfter = root.after(30, ballMove)

# Сбрасываем всё
def reset():
    global ball, butt, buttNow, buttEvil, buttNowEvil, afterPlayer, vectorY_evil, vectorY_player, vectorX, vectorY, play
    # Сбрасываем координаты мячика
    canvas.coords(ball, WIDTH // 2, HEIGHT // 2)
    # Ставим бинд на пробел "старт нового раунда"
    canvas.bind("<space>", startNewRoundBind)
    # Сбрасываем кнопки нажатые
    buttNow = None
    buttNowEvil = None
    # Нужны разные значения, чтобы сбросить движение платформ
    butt = 0
    buttEvil = 0
    # Запуск движения
    move()
    # Сбрасываем координаты платформ
    canvas.coords(player, 1882, 696)
    canvas.coords(evil, 38, 150)
    # Обновляем текст
    refreshText()
    # Сбрасываем скорость движения платформ
    vectorY_player = 5
    vectorY_evil = 5
    # Сбрасываем корость движения мяча
    vectorX = 7
    vectorY = 7
    # Нужна для рандома направления
    play = 0

# Основное тело старта нового раунда
def startNewRound():
    global ballAfter, butt, buttNow, buttEvil, buttNowEvil, ball
    refreshText()
    ballAfter = root.after(30, ballMove)

    # Вызываем метод сброса
    reset()
    # Убираем бинд с пробела
    canvas.unbind("<space>")
    # Ещё раз сбрасываем кнопки нажатые, чтобы платформы опять двигались
    butt = None
    buttEvil = None
    # Запуск движения платформ
    move()

# Старт нового раунда на пробел
def startNewRoundBind(event):
    startNewRound()
# ====================== Начало программы ======================
root = Tk()

# Размеры окна
WIDTH = 1920
HEIGHT = 900
root.resizable(False, False)
root.title("Теннис")
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")
root.iconbitmap("tennis.ico")

# Создаём canvas
canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.config(highlightthickness=0)
canvas.place(x=0, y=0)
canvas.focus_set()

# Загружаем изображения
back = PhotoImage(file="background.png")
playerRectangle = PhotoImage(file="red_rectangle.png")
evilRectangle = PhotoImage(file="green_rectangle.png")
ballCircle = PhotoImage(file="circle.png")

# Установка фона
canvas.create_image(WIDTH // 2, HEIGHT // 2, image=back)

# Скорость движения мяча
vectorX = 7
vectorY = 7

# Скорость движения платформ
vectorY_player = 5
vectorY_evil = 5

# Создаём и получаем ссылку на объекты
player = canvas.create_image(1882, 696, image=playerRectangle)   # Тест значения хитбоксов     696       529     221
evil = canvas.create_image(38, 150, image=evilRectangle)
ball = canvas.create_image(WIDTH // 2, HEIGHT // 2, image=ballCircle)

# Закодируем движения кнопками
UPKEY = 0
DOWNKEY = 1
WKEY = 2
SKEY = 3

# кнопки сейчас
butt = None
buttNow = None
buttEvil = None
buttNowEvil = None
# Запускаем движения игроков
afterPlayer = None
# Запуск движения мяча
ballAfter = None
# Счётчик количество забитых голов
countGreen = 0
countRed = 0
# Нужна для рандома направления
play = 0

# Задний фон виджетов с текстом
backgroundLabel = "#b4b4b4"

# Метки для вывода ГОЛОВ
countLabelRed = Label(root, text="Игрок красной платформы забил:", bg=backgroundLabel)
countLabelRed.place(x=1300, y=0)
countLabelGreen = Label(root, text="Игрок зелёной платформы забил:", bg=backgroundLabel)
countLabelGreen.place(x=350, y=0)
recordRed = Label(root, text="Рекорд красного игрока:", bg=backgroundLabel)
recordRed.place(x=1350, y=880)
recordGreen = Label(root, text="Рекорд зелёного игрока:", bg=backgroundLabel)
recordGreen.place(x=400, y=880)

# Биндим клавиши управления курсором(стрелки) для управления красной платформы
canvas.bind("<Up>", lambda e, x = UPKEY: moveButton(x))
canvas.bind("<Down>", lambda e, x = DOWNKEY: moveButton(x))
# Биндим клавиши W и S для управления зелёной платформы
canvas.bind("<w>", lambda e, y = WKEY: moveButtonEvil(y))
canvas.bind("<s>", lambda e, y = SKEY: moveButtonEvil(y))
# Биндим Старт нового раунда на пробел
canvas.bind("<space>", startNewRoundBind)

# Наибольшее количество голов
record = getRecordSteps()

refreshText()
root.mainloop()