from tkinter import *

# Кнопка куда идёт квадрат
def moveButton(button):
    global butt, buttNow

    # Ставим номер кнопки
    if (button == UPKEY):
        butt = 0
    elif (button == DOWNKEY):
        butt = 1
    elif (button == LEFTKEY):
        butt = 2
    elif (button == RIGHTKEY):
        butt = 3

    # Кнопка сейчас
    buttNow = butt
    return buttNow

# Движение квадрата
def move():
    global vectorX_player, vectorY_player, After, buttNow

    # Передвигаем квадрат
    if (buttNow == UPKEY):
        cnv.move(player, 0, -vectorY_player)
    elif (buttNow == DOWNKEY):
        cnv.move(player, 0, vectorY_player)
    elif (buttNow == LEFTKEY):
        cnv.move(player, -vectorX_player, 0)
    elif (buttNow == RIGHTKEY):
        cnv.move(player, vectorX_player, 0)

    # Получаем координаты квадрата в отдельные переменые
    x = cnv.coords(player)[0]
    y = cnv.coords(player)[1]

    # Проверка выхода за границы
    if (x > WIDTH - 32 or x < 32):
        vectorX_player = -vectorX_player
    if (y > HEIGHT - 32 or y < 32):
        vectorY_player = -vectorY_player

    # Если кнопка сейчас == кнопке, то стоп рекурсии
    if (buttNow != butt):
        After = root.after_cancel(move)
    else:
        After = root.after(30, move)


# Движение красного круга
def evilMove():
    global evilAfter, vectors

    # Передвигаем вражеский круг
    cnv.move(evil, vectors[0], vectors[1])
    cnv.move(evil2, vectors[2], vectors[3])

    # Получаем координаты в отдельные переменные
    # cnv.coords возвращает список,
    # в котором на позиции 0 стоит координата x, на первой y
    # координаты x на месте списка = xy[0], xy[2]
    # координаты y = xy[1], xy[3]
    xy = [cnv.coords(evil)[0],
          cnv.coords(evil)[1],
          cnv.coords(evil2)[0],
          cnv.coords(evil2)[1]]

    # Проверяем: ударился ли первый красный круг о границы окна
    if (xy[0] > WIDTH - 32 or xy[0] < 32):
        vectors[0] = -vectors[0]
    if (xy[1] > HEIGHT - 32 or xy[1] < 32):
        vectors[1] = -vectors[1]

    # Проверяем: ударился ли второй красный круг о границы окна
    if (xy[2] > WIDTH - 32 or xy[2] < 32):
        vectors[2] = -vectors[2]
    if (xy[3] > HEIGHT - 32 or xy[3] < 32):
        vectors[3] = -vectors[3]

    # Получаем координаты игрока
    xP = cnv.coords(player)[0]
    yP = cnv.coords(player)[1]

    # Если расстояние между координатами меньше диаметра круга, то засчитываем
    # соприкосновение и стопаем круг
    distance = (abs(xy[0] - xP) ** 2 + abs(xy[1] - yP) ** 2) ** 0.5
    distance2 = (abs(xy[2] - xP) ** 2 + abs(xy[3] - yP) ** 2) ** 0.5

    # Если соприкосновение первого круга, то Смещение vector[0](x) и vector[1](y) = 0
    if (distance < 64):
        vectors[0] = 0
        vectors[1] = 0
    # Если соприкосновение второго круга, то Смещение vector[2](x) и vector[3](y) = 0
    elif (distance2 < 64):
        vectors[2] = 0
        vectors[3] = 0

    # Если координаты x двух кругов равны НУЛЮ, то останавливаем рекурсию
    if (vectors[0] == 0 and vectors[2] == 0):
        root.after_cancel(evilMove)
        #messagebox.showinfo("Шары остановились", "Все шары остановились. Для выхода нажмите: ENTER")
        #quit(0)
    else:
        # Если нет
        evilAfter = root.after(30, evilMove)

# Размеры окна
WIDTH = 640
HEIGHT = 480

root = Tk()
root.title("Шары и квадрат")
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

# Создаём виджет CANVAS
cnv = Canvas(root, width=WIDTH, height=HEIGHT)
cnv.config(highlightthickness=0)
cnv.place(x=0, y=0)
cnv.focus_set()

# Загружаем изображения
back = PhotoImage(file="background.png")
evilCircle = PhotoImage(file="circle.png")
playerSquare = PhotoImage(file="square.png")
evil2Circle = PhotoImage(file="circle.png")

# Устанавливаем фон
cnv.create_image(WIDTH // 2, HEIGHT // 2, image=back)

# Смещение вражеского круга
# координаты x = vectors[0], vectors[2]
# по y = vectors[1], vectors[3]
vectors = [2, 2, 2, 2]

# Скорость движения
vectorX_player = 4
vectorY_player = 4

# Создаём и получаем ссылку на объекты
evil = cnv.create_image(32, 32, image=evilCircle)
evil2 = cnv.create_image(608, 448, image=evil2Circle)
player = cnv.create_image(WIDTH // 2, HEIGHT // 2, image=playerSquare)

# Закодируем кнопки константами
UPKEY = 0
DOWNKEY = 1
LEFTKEY = 2
RIGHTKEY = 3

# Запускаем движение квадрата
After = None
# Запускаем движение вражеского круга
evilAfter = root.after(30, evilMove)
# Кнопка
butt = None
# Кнопка сейчас
buttNow = None
# Биндим клавиши управления курсором
cnv.bind("<Up>", lambda e, x = UPKEY: moveButton(x))
cnv.bind("<Down>", lambda e, x = DOWNKEY: moveButton(x))
cnv.bind("<Left>", lambda e, x = LEFTKEY: moveButton(x))
cnv.bind("<Right>", lambda e, x = RIGHTKEY: moveButton(x))
# Запуск движения квадрата
move()

# Запуск окна
root.mainloop()