from tkinter import *
from time import sleep
from winsound import Beep
# ============================== Функции и методы ==============================
# Чит 1
def goCheat():
    global moving
    print("Метод goCheat()")
    moving = True
    # Установка ящиков на места
    for i in range(len(boxes)):
        boxes[i][0] = finish[i][0]
        boxes[i][1] = finish[i][1]
        cnv.coords(boxes[i][2],
                   SQUARE_SIZE // 2 + boxes[i][1] * SQUARE_SIZE,
                   SQUARE_SIZE // 2 + boxes[i][0] * SQUARE_SIZE)
    # Обновление изображения
    cnv.update()
    # Пауза
    sleep(2)
    # Проверка победы
    checkBoxInFinish()

# При нажатии на кнопку продолжить
def nextLevelSet(btnNext: Button):
    global level
    level += 1
    # Установка фокуса внимания, чтобы работали кнопки на клавиатуре
    cnv.focus_set()

    # Удаляем кнопку "ПРОДОЛЖИТЬ"
    btnNext.destroy()

    # Возвращаем назад кнопки
    btnCheat.place(x=10, y=590)
    btnReset.place(x=10, y=550)

    # Очищаем Canvas
    cnv.delete(ALL)
    reset()

# В случае победы переключаем уровень
def nextLevel():
    print("Метод nextLevel()")
    # Удаляем всё
    cnv.delete(ALL)
    # Стоп таймеру
    stopTimer()

    # Убираем из зоны видимости кнопки
    btnCheat.place(x=-100, y=-100)
    btnReset.place(x=-100, y=-100)

    # Создаём новую для продолжения, потом удалим
    btnNext = Button(text="Продолжить",
                     font="Verdana, 19",
                     width=45)
    btnNext.place(x=300, y=550)
    btnNext.focus_set()
    btnNext["command"] = lambda b=btnNext: nextLevelSet(b)

    cnv.create_text(WIDTH * SQUARE_SIZE // 2,
                    200,
                    fill="#AAFFCC",
                    text=f"Победа! Вы собрали головоломку за {getMinSec(second)}!",
                    font="Verdana, 25")

# Ящики на месте?
def checkBoxInFinish():
    global finish, win
    print("Метод checkBoxInFinish()")

    # Сбросс параметра в списке мест сбора, отвечающий на вопрос: "Ящик на месте?"
    for fin in finish:
        fin[3] = False

    # Предпологаем, что игрок выиграл, но пытаемся доказать обратное
    win = True
    fin = 0
    while (fin < len(finish) and win):
        box = 0
        while (box < len(boxes) and win):
            if (finish[fin][0:2] ==
                    boxes[box][0:2]):
                finish[fin][3] = True
                box = len(boxes)
            box += 1
        win = win and finish[fin][3]
        fin += 1

    # Если всё же победа
    if (win):
        Beep(750, 10)
        Beep(1750, 10)
        nextLevel()

# Перемещение ящика вместе с погрузчиком
def movePlayerBoxTo(x, y, count, numberBox):
    global moving
    count -= 1
    cnv.move(player[2], x, y)
    cnv.move(boxes[numberBox][2], x, y)

    if (count > 0):
        moving = True
        root.after(20,
                   lambda x=x,
                          y=y,
                          c=count,
                          n=numberBox:
                   movePlayerBoxTo(x, y, c, n))
    else:
        print("Метод movePlayerBoxTo выполнился")
        moving = False
        checkBoxInFinish()

# Перемещение погрузчика
def movePlayerTo(x, y, count):
    global moving
    count -= 1
    # Перемещаем игрока без ящика
    cnv.move(player[2], x, y)

    # Продолжаем, пока не переместим на нужное расстояние
    if (count > 0):
        moving = True
        # Задаём анимацию. С интервалом в 20 миллисекунд
        root.after(20,
                   lambda x=x,
                          y=y,
                          c=count:
                   movePlayerTo(x, y, c))
    else:
        print("Метод movePlayerTo() выполнился")
        # Перемещение закончилось, разрешаем программе реагировать на нажатие клавиатуры
        moving = False

# Получаем номер ящика, расположенного по координатам x, y
def getBox(x, y):
    print("Метод getBox()")
    for i in range(len(boxes)):
        if (boxes[i][0] == x and boxes[i][1] == y):
            return i
    return None

# Получаем номер объекта, расположенного в позиции x, y. Это ящик(2), стена(1), трава(0)
def getNumber(x, y):
    print("Метод getNumber()")
    for box in boxes:
        if (box[0] == x and box[1] == y):
            return 2
    if (dataLevel[x][y] <= 1):
        return dataLevel[x][y]

# Рассчитываем перемещение погрузчика при нажатии на кнопку курсора
def move(v):
    print("Метод move()")

    # Если выполняется анимация, то прерываем метод
    if (moving):
        return 0
    # Удаляем изображения игрока
    cnv.delete(player[2])
    # Создаём его, но повёрнутое в другую сторону v
    player[2] = cnv.create_image(SQUARE_SIZE // 2 + player[1] * SQUARE_SIZE,
                                 SQUARE_SIZE // 2 + player[0] * SQUARE_SIZE,
                                 image=img[3][v])

    # Для удобства
    x = player[0]
    y = player[1]
    Beep(625, 10)

    # Вверх
    if (v == UPKEY):
        # Номер объекта сверху
        check = getNumber(x - 1, y)

        # Если пустое место или место сбора ящиков, то двигаемся
        if (check == 0):
            movePlayerTo(0, -8, 8)
            # Изменяем координаты игрока
            player[0] -= 1
        # Если впереди ящик
        elif (check == 2):
            # Получаем номер клетки, в которую нужно передвинуть ящик,
            # и если клетка пустая перемещаем ящик и игрока
            nextCheck = getNumber(x - 2, y)
            if (nextCheck == 0):
                numberBox = getBox(x - 1, y)
                # Отправляем координаты смещения и номер ящика
                movePlayerBoxTo(0, -8, 8, numberBox)
                # Изменяем координаты игрока
                player[0] -= 1
                # И ящика
                boxes[numberBox][0] -= 1

    # Вниз
    elif (v == DOWNKEY):
        check = getNumber(x + 1, y)
        if (check == 0):
            movePlayerTo(0, 8, 8)
            player[0] += 1
        elif (check == 2):
            nextCheck = getNumber(x + 2, y)
            if (nextCheck == 0):
                numberBox = getBox(x + 1, y)
                movePlayerBoxTo(0, 8, 8, numberBox)
                player[0] += 1
                boxes[numberBox][0] += 1

    # Влево
    elif (v == LEFTKEY):
        check = getNumber(x, y - 1)
        if (check == 0):
            movePlayerTo(-8, 0, 8)
            player[1] -= 1
        elif (check == 2):
            nextCheck = getNumber(x, y - 2)
            if (nextCheck == 0):
                numberBox = getBox(x, y - 1)
                movePlayerBoxTo(-8, 0, 8, numberBox)
                player[1] -= 1
                boxes[numberBox][1] -= 1

    # Вправо
    elif (v == RIGHTKEY):
        check = getNumber(x, y + 1)
        if (check == 0):
            movePlayerTo(8, 0, 8)
            player[1] += 1
        elif (check == 2):
            nextCheck = getNumber(x, y + 2)
            if (nextCheck == 0):
                numberBox = getBox(x, y + 1)
                movePlayerBoxTo(8, 0, 8, numberBox)
                player[1] += 1
                boxes[numberBox][1] += 1


# Возвращаем строку в виде ММ:СС
def getMinSec(s):
    # Находим минуты
    intMin = s // 60
    # Находим секунды
    intSec = s % 60
    textSecond = str(intSec)

    # Сбрасываем минуты, если прошло > 59, чтобы не выводить часы
    if (intMin > 59):
        intMin %= 60

    # Добавляем 0, если секунд < 10
    if (intSec < 10):
        textSecond = "0" + textSecond

    if (intMin == 0):
        return f"{textSecond} сек."
    else:
        textMin = str(intMin)
        if (intMin < 10):
            textMin = "0" + textMin
        return f"{textMin} мин. {textSecond} сек."

# Обновляем полоску с текстом вверху
def updateText():
    global textTime, second, timeRun
    # Увеличиваем количество секунд
    second += 1
    # Удаляем предыдущую надпись
    cnv.delete(textTime)

    # Формируем строку для вывода
    txt = f"Уровень: {level}    Прошло времени: {getMinSec(second)}"

    # Переменная для таймера, нужна, чтобы программа имела ссылку на таймер тогда,
    # когда нам нужно остановить таймер
    textTime = cnv.create_text(10,                          # Координата x относительно Canvas
                               10,                          # Координата y относительно Canvas
                               fill="#FFCAAB",              # Цвет текста
                               anchor="nw",                 # Выравнивание "nw" - по левому краю
                               text=txt,                    # Текстовая надпись
                               font="Verdana, 15")          # Шрифт и размер
    # Вызов метода каждую секунду(1000 миллисекунд)
    timeRun = root.after(1000, updateText)

# Создание объектов Canvas:
# формируем изображение позиции
def createLevel():
    print("Метод createLevel()")
    global player, boxes, finish

    player = []
    boxes = []
    finish = []

    # Нижний слой, кирпичные стены и поля сбора
    for i in range(len(dataLevel)):
        for j in range(len(dataLevel[i])):
            # Стены
            if (dataLevel[i][j] == 1):
                cnv.create_image(SQUARE_SIZE // 2 + j * SQUARE_SIZE,
                                 SQUARE_SIZE // 2 + i * SQUARE_SIZE,
                                 image=img[0])
            # Поля сбора
            elif (dataLevel[i][j] == 3):
                dataLevel[i][j] = 0
                finish.append([i, j,
                               cnv.create_image(SQUARE_SIZE // 2 + j * SQUARE_SIZE,
                                                SQUARE_SIZE // 2 + i * SQUARE_SIZE,
                                                image=img[2]),
                               False])
    # Данные списка finish[ a, b, c, d]:
    # a - координата по x относительно математической модели 20x10
    # b - координата по y -""-
    # c - объект Canvas (Изображение зелёной точки)
    # d - признак True - есть на это клетке ящик, False - нет

    # Верхний слой, ящики и игрок
    for i in range(len(dataLevel)):
        for j in range(len(dataLevel[i])):
            # Ящики
            if (dataLevel[i][j] == 2):
                dataLevel[i][j] = 0
                boxes.append([i, j,
                              cnv.create_image(SQUARE_SIZE // 2 + j * SQUARE_SIZE,
                                               SQUARE_SIZE // 2 + i * SQUARE_SIZE,
                                               image=img[1])])
            # Данные списка boxes[a, b, c]:
            # a - координата по x относительно математической модели 20x10
            # b - координата по y -""-
            # c - объект Canvas (изображение ящика)

            # Погрузчик
            elif (dataLevel[i][j] == 4):
                dataLevel[i][j] = 0
                player = [i, j, cnv.create_image(SQUARE_SIZE // 2 + j * SQUARE_SIZE,
                                                 SQUARE_SIZE // 2 + i * SQUARE_SIZE,
                                                 image=img[3][1])]
            # Данные списка player[a, b, c]:
            # a - координата по x относительно математической модели 20x10
            # b - координата по y -""-
            # c - объект Canvas (изображение погрузчика)

# Загрузка данных уровня
def getLevel(lvl):
    global dataLevel
    print("Метод getLevel()")
    dataLevel = []
    tmp = []

    # Формируем индекс к имени файла
    idx = str(lvl)
    if (lvl < 10):
        idx = f"0{lvl}"
    try:
        f = open(f"levels/level{idx}.dat", "r", encoding="utf-8")
        for i in f.readlines():
            tmp.append(i.replace("\n", ""))
        f.close()
        # Перегоняем в двумерный список с числами
        for i in range(len(tmp)):
            dataLevel.append([])
            for j in tmp[i]:
                dataLevel[i].append(int(j))
    except:
        print("Не найден файл с данными.")
        quit(0)

# Стоп таймер
def stopTimer():
    global timeRun
    if (timeRun != None):
        root.after_cancel(timeRun)

        # Убираем маркер работы таймера
        timeRun = None

# Замостить изображением grass.png всю область окна
# Вызов самым первым, чтобы трава легла снизу
def clear_setGrass():
    print("Метод clear_setGrass()")
    cnv.delete(ALL)
    for i in range(WIDTH):
        for j in range(HEIGHT):
            cnv.create_image(SQUARE_SIZE // 2 + i * SQUARE_SIZE,
                             SQUARE_SIZE // 2 + j * SQUARE_SIZE,
                             image=backGround)

# Сброс и пересоздание уровня
def reset():
    global moving, second, timeRun
    print("Метод reset()")

    moving = False
    second = -1
    # Стоп таймеру
    stopTimer()
    # Загрузка данных
    getLevel(level)
    # Очистка экрана, устанавливая фон
    clear_setGrass()
    # Создаём уровень
    createLevel()
    # Запуск таймера
    updateText()

# ============================== Начало программы ==============================
root = Tk()
root.resizable(False, False)
root.title("Кособан")
root.iconbitmap("icon/icon.ico")

# Кол. плиток
WIDTH = 20
HEIGHT = 10
# Размер 1 плитки
SQUARE_SIZE = 64

POS_X = root.winfo_screenwidth() // 2 - (WIDTH * SQUARE_SIZE) // 2
POS_Y = root.winfo_screenheight() // 2 - (HEIGHT * SQUARE_SIZE) // 2
root.geometry(f"{WIDTH * SQUARE_SIZE + 0}x{HEIGHT * SQUARE_SIZE + 0}+{POS_X}+{POS_Y}")

# Константы кнопок
UPKEY = 0
DOWNKEY = 1
LEFTKEY = 2
RIGHTKEY = 3

# Canvas
cnv = Canvas(root, width=WIDTH * SQUARE_SIZE, height=HEIGHT * SQUARE_SIZE, bg="#373737")
cnv.config(highlightthickness=0)
cnv.place(x=0, y=0)
cnv.focus_set()

# Устанавливаем вызов move на стрелки(кнопки курсора)
cnv.bind("<Up>", lambda e, x=UPKEY: move(x))
cnv.bind("<Down>", lambda e, x=DOWNKEY: move(x))
cnv.bind("<Left>", lambda e, x=LEFTKEY: move(x))
cnv.bind("<Right>", lambda e, x=RIGHTKEY: move(x))

# Работает ли анимация?
# Если True, то анимация перемещения погрузчика и ящиков работает
moving = True

# Текстура травы, фона
backGround = PhotoImage(file="image/grass.png")

# Список для хранения изображений
img = []
img.append(PhotoImage(file="image/wall.png"))
img.append(PhotoImage(file="image/box.png"))
img.append(PhotoImage(file="image/finish.png"))
img.append([])
img[3].append(PhotoImage(file="image/kosoban_up.png"))      # Погрузчик вверх
img[3].append(PhotoImage(file="image/kosoban_down.png"))    # Погрузчик вниз
img[3].append(PhotoImage(file="image/kosoban_left.png"))    # Погрузчик влево
img[3].append(PhotoImage(file="image/kosoban_right.png"))   # Погрузчик вправо

# Игрок
player = []
# Ящики
boxes = []
# Точки сбора
finish = []

# Игрок победил?
win = False

# Кнопки управления
# Кнопка сброса
btnReset = Button(text="Сбросить поле".upper(),
                  font=("Consolas", "15"),
                  width=20)
btnReset.place(x=10, y=550)
btnReset["command"] = reset

# Кнопка ЧИТ
btnCheat = Button(text="Установить ящики".upper(),
                  font=("Consolas", "15"),
                  width=20)
btnCheat.place(x=10, y=590)
btnCheat["command"] = goCheat

# Текстовая строка, показывающая время
textTime = None
# Время прошедшее
second = None

# Номер текущего уровня
level = 1

# Математическая модель из файла
dataLevel = []

# Объект для хранения вызова с помощью .after
timeRun = None

# Создаём уровень
reset()

root.mainloop()