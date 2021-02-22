from tkinter import *
import random
from tkinter import messagebox

# Окно
root = Tk()

#*************************************************************
#       Методы и функции
#*************************************************************

# Открытие нового окна в кнопке 6
def podscazca_window():
    global textDiary2

    # Размеры окна программы
    WIDTH = 1024
    HEIGHT = 600

    window = Toplevel(root)

    # Создаём главное окно
    # Вычисляем координаты для размещения окна по центру
    POS_X = window.winfo_screenwidth() // 2 - WIDTH // 2
    POS_Y = window.winfo_screenheight() // 2 - HEIGHT // 2

    # Установка заголовка окна
    window.title("Подсказки")

    # Запрет изменения размеров окна
    window.resizable(False, False)

    # Устанавливаем ширину, высоту и позицию окна
    window.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

    # Создаём чат с информацией виджетом TEXT
    textDiary2 = Text(window, width=122, height=13, wrap=WORD)
    textDiary2.place(x=10, y=20)
    textDiary2.configure(state='disabled')

    # Создаём и прикрепляем к тексту полосу прокрутки
    scroll2 = Scrollbar(window, command=textDiary2.yview, width=20)
    scroll2.place(x=990, y=20, height=214)
    textDiary2["yscrollcommand"] = scroll2.set

    # Кнопки в новом окне
    podscazcaButton01 = Button(window, text="ax^2 + bx = 0", font="arial 20", width=20)
    podscazcaButton01.place(x=10, y=250)
    podscazcaButton01["command"] = podscazka1

    podscazcaButton02 = Button(window, text="ax^2 + c = 0", font="arial 20", width=20)
    podscazcaButton02.place(x=345, y=250)
    podscazcaButton02["command"] = podscazka2

    podscazcaButton03 = Button(window, text="ax^2 = 0", font="arial 20", width=20)
    podscazcaButton03.place(x=680, y=250)
    podscazcaButton03["command"] = podscazka3

    podscazcaButton04 = Button(window, text="x^2 + bx + c = 0", font="arial 20", width=20)
    podscazcaButton04.place(x=10, y=310)
    podscazcaButton04["command"] = podscazka4

    podscazcaButton05 = Button(window, text="ax^2 + bx + c = 0", font="arial 20", width=20)
    podscazcaButton05.place(x=345, y=310)
    podscazcaButton05["command"] = podscazka5


# Добавления строки в текстовый блок
def insertText(s, textDiary):
    textDiary.configure(state='normal')
    textDiary.insert(INSERT, s + "\n")
    textDiary.see(END)
    textDiary.configure(state='disabled')

# Разрешаем нажимать на кнопки
def runProgrammButton():
    button1["state"] = "normal"
    button2["state"] = "normal"
    button3["state"] = "normal"
    button4["state"] = "normal"
    button5["state"] = "normal"
    button6["state"] = "normal"
    button7["state"] = "normal"
    button8["state"] = "normal"
    buttonRight["state"] = "disabled"

# Запрещаем нажимать на кнопки
def runProgramm():
    button1["state"] = "disabled"
    button2["state"] = "disabled"
    button3["state"] = "disabled"
    button4["state"] = "disabled"
    button5["state"] = "disabled"
    button6["state"] = "disabled"
    button7["state"] = "disabled"
    button8["state"] = "disabled"

# основное тело функции проверки на число
def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

# рандом корней
def randoms():
    global x1, x2, a
    x1 = 0
    x2 = 0
    while not (x1 != 0):
        x1 = random.randint(-10, 10)
    while not (x2 != 0):
        x2 = random.randint(-10, 10)
    a = 0
    while not (a != 0):
        a = random.randint(-10, 10)

    # Включение кнопки "принять ответ", чтобы пользователь не читерил очки
    buttonRight["state"] = "normal"

# рандом корней цикл на проверку чтобы x1 != -x2
def randomsX1minX2():
    randoms()
    while (x1 == -x2):
        randoms()
    while (a == 1):
        randoms()

# Вычисление коэф для 4 и 5
def bac():
    global b,c, a
    b = (x1 + x2) * -1 * a
    c = x1 * x2 * a

# Проверка ввода число
def proverka():
    global right, score, discri, count

    x1_x2 = edit.get()
    x2_x1 = edit1.get()
    x_x2 = is_digit(x1_x2)
    x2_x = is_digit(x2_x1)

    x_x2 = float(x_x2)
    x2_x = float(x2_x)

    if (x_x2 and x2_x):
        x33 = False
        while (x33 != True):
            x3 = edit.get()
            x33 = is_digit(x3)

        x44 = False
        while (x44 != True):
            x4 = edit1.get()
            x44 = is_digit(x4)
        x3 = float(x3)
        x4 = float(x4)

        # Проверка результатов
        if ((x3 == x1 and x4 == x2) or (x3 == x2 and x4 == x1)):
            insertText("Победа! Поздравляем!", textDiary)
            record[1] += 1
            record[0] += 10
        else:
            insertText(f"Вы проиграли правильный ответ: {x1} и {x2} ", textDiary)
            record[0] -= 20
        record[2] += 1
        runProgrammButton()
    else:
        messagebox.showinfo("Стоп!", "Введите пожалуйста число!")
    saveRecords()

    # Очистка виджета ввода данных (Entry)
    edit.delete(0, END)
    edit1.delete(0, END)

# Чтение из файла статистики
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
    if (len(m) != 3):
        m = []
        for i in range(3):
            m.append(0)
    return m

# Запись статистики в файл
def saveRecords():
    global record
    # Открываем файл и записываем
    try:
        f = open("steps.dat", "w", encoding="utf-8")
        for i in range(len(record)):
            f.write(str(record[i]) + "\n")
        f.close()
    # Если ошибка
    except:
        messagebox.showinfo("Ошибка",
                            "Возникла проблема с файлом при сохранении очков")


#*************************************************************
#                   Функции уранений
#*************************************************************

# 1 - ax^2 + bx = 0
def form1():
    global right, score, x1
    runProgramm()
    randomsX1minX2()

    x1 = 0

    b = x2 * a * -1
    if (b < 0):
        insertText(f"{a} x^2  {b} x = 0", textDiary)
    else:
        insertText(f"{a} x^2 + {b} x = 0", textDiary)

# 2 - ax^2 + c = 0
def form2():
    global right, score, x2
    runProgramm()
    randomsX1minX2()

    x = x1
    x2 = -x1
    xv2 = x ** 2
    c = (xv2 * -1 * a)

    if (c != 0):
        if (c > 0):
            insertText(f"{a}x^2 + {c} = 0", textDiary)
        else:
            insertText(f"{a}x^2 {c} = 0", textDiary)

# 3 - ax^2 = 0
def form3():
    global right, score, x1, x2
    runProgramm()
    randoms()

    x1 = 0
    x2 = 0
    insertText(f"{a} x^2 = 0", textDiary)


# 4 - x^2 + bx + c = 0
def form4():
    global right, score, a
    runProgramm()
    randomsX1minX2()

    a = 1
    bac()

    if (b <= 0 and c <= 0):
        insertText(f"x^2 {b} x {c} = 0", textDiary)
    elif (b <= 0 and c >= 0):
        insertText(f"x^2 {b} x + {c} = 0", textDiary)
    elif (b >= 0 and c >= 0):
        insertText(f"x^2 + {b} x + {c} = 0", textDiary)
    else:
        insertText(f"x^2 + {b} x {c} = 0", textDiary)


# 5 - ax^2 + bx + c = 0
def form5():
    global right, score
    runProgramm()
    randomsX1minX2()
    bac()

    if (b <= 0 and c <= 0):
        insertText(f"{a}x^2 {b}x {c} = 0", textDiary)
    elif (b <= 0 and c >= 0):
        insertText(f"{a}x^2 {b}x + {c} = 0", textDiary)
    elif (b >= 0 and c >= 0):
        insertText(f"{a}x^2 + {b}x + {c} = 0", textDiary)
    else:
        insertText(f"{a}x^2 + {b}x {c} = 0", textDiary)

# Показать статистику
def form7():
    insertText(f"""Ваше количество очков: {record[0]}
Количество правильных решений: {record[1]}
Количество примеров: {record[2]}""", textDiary)

# Правила
def form8():
    insertText(f"""Правила:
1 - Выбрать режим.
2 - Вводить цифры, если введёте другие символы, вам всё равно придётся ввести цифры.
3 - После ввода цифр нажмите на кнопку "Принять ответ".
4 - Ваша статистика записывается в файл.""", textDiary)

# *************************************************************
#       Подсказки
# *************************************************************

def podscazka1():
    insertText("""
Это подсказка.
1 - ax^2 + bx = 0
x(ax+b) = 0
x = 0 v ax+b = 0
        x = -b/a
Пример:
    2 x^2  -16 x = 0
    x(2x - 16) = 0
    x = 0 v 2x - 16 = 0
            2x = 16
            x = 8
Ответ: x1 = 0, x2 = 8""", textDiary2)

def podscazka2():
    insertText("""
Это подсказка.
2 - ax^2 + c = 0
x^2 = -c / a
x = √-c/a
Пример:
    -10x^2 + 90 = 0
    x^2 = 90/10
    x^2 = 9
    x = √9
    x = ±3
Ответ: x1 = 3, x2 = -3""", textDiary2)

def podscazka3():
    insertText("""
Это подсказка.
3 - ax^2 = 0
Пример:
    10x^2 = 0
    x = 0
Ответ: x = 0""", textDiary2)

def podscazka4():
    insertText("""
Это подсказка.
4 - x^2 + bx + c = 0
{x1 + x2 = -b
{x1 * x2 = c
Пример:
    x^2 + 3 x -4 = 0        
    {x1 + x2 = -3   {x1 = -4
    {x1 * x2 = -4   {x2 = 1
Ответ: x1 = -4, x2 = 1""", textDiary2)

def podscazka5():
    insertText("""
Это подсказка.
5 - ax^2 + bx + c = 0
D = b^2 - 4ac
x = (-b ± √D) / (2a)
x1 = (-b - √D) / (2a)
x2 = (-b + √D) / (2a)
Пример:
    6x^2 -54x + 48 = 0
    D = 2916 - 1152 = 1764
    √D = 42
    x1 = (54 - 42) / 12 = 1
    x2 = (54 + 42) / 12 = 8
Ответ: x1 = 1, x2 = 8""", textDiary2)

#*************************************************************
#       Переменные
#*************************************************************

# Размеры окна программы
WIDTH = 1024
HEIGHT = 600

#*************************************************************
#       Формирование эллементов в окне
#*************************************************************

# Создаём главное окно
# Вычисляем координаты для размещения окна по центру
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2

# Установка заголовка окна
root.title("Тренажёр квадратных уравнений")

# Запрет изменения размеров окна
root.resizable(False, False)

# Устанавливаем ширину, высоту и позицию окна
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

# Создаём чат с информацией виджетом TEXT
textDiary = Text(width=122, height=8, wrap=WORD)
textDiary.place(x=10, y=20)
textDiary.configure(state='disabled')

# Создаём и прикрепляем к тексту полосу прокрутки
scroll = Scrollbar(command=textDiary.yview, width=20)
scroll.place(x=990, y=20, height=132)
textDiary["yscrollcommand"] = scroll.set

# Кнопка принять результат
buttonRight = Button(text="Принять ответ", font="arial 20", width=15, background="red")
buttonRight.place(x=10, y=500)
buttonRight["command"] = proverka
buttonRight["state"] = "disabled"

# Создаём кнопку 1 режима
button1 = Button(text="ax^2 + bx = 0", font="arial 20", width=20, background="white")
button1.place(x=10, y=190)
button1["command"] = form1

# Создаём кнопку 2 режима
button2 = Button(text="ax^2 + c = 0", font="arial 20", width=20, background="white")
button2.place(x=345, y=190)
button2["command"] = form2

# Создаём кнопку 3 режима
button3 = Button(text="ax^2 = 0", font="arial 20", width=20, background="white")
button3.place(x=680, y=190)
button3["command"] = form3

# Создаём кнопку 4 режима
button4 = Button(text="x^2 + bx + c = 0", font="arial 20", width=20, background="white")
button4.place(x=10, y=250)
button4["command"] = form4

# Создаём кнопку 5 режима
button5 = Button(text="ax^2 + bx + c = 0", font="arial 20", width=20, background="white")
button5.place(x=680, y=250)
button5["command"] = form5

# Создаём кнопку 6 режима - Подсказки
button6 = Button(text="Подсказки", font="arial 20", width=20, background="white")
button6.place(x=10, y=310)
button6["command"] = podscazca_window

# Создаём кнопку 7 режима - Статистика игры
button7 = Button(text="Статистика игры", font="arial 20", width=20, background="white")
button7.place(x=680, y=310)
button7["command"] = form7

# Создаём кнопку 8 режима - Правила
button8 = Button(text="Правила игры", font="arial 20", width=20, background="white")
button8.place(x=345, y=310)
button8["command"] = form8

# Загрузка статистики из файла
record = getRecordSteps()

#*************************************
#           поле ввода
#*************************************

# x1 Ввод
label_x1 = Label(text="x1=", font="arial 15")
label_x1.place(x=20, y=154)

# Установка окна ввода x1
edit = Entry(root, width=50)
edit.place(x=57, y=160)

# x2 Ввод
label_x2 = Label(text="x2=", font="arial 15")
label_x2.place(x=375, y=154)

# Установка окна ввода x1
edit1 = Entry(root, width=50)
edit1.place(x=410, y=160)

# Запуск программы
root.mainloop()