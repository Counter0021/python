from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from random import randint

#*************************************************************
#       Методы и функции
#*************************************************************

#Установка состояния лошадей и погоды
def setupHorse():
    global state01, state02, state03, state04
    global weather, timeDay
    global winCoeff01, winCoeff02, winCoeff03, winCoeff04
    global play01, play02, play03, play04
    global reverse01, reverse02, reverse03, reverse04
    global fastSpeed01, fastSpeed02, fastSpeed03, fastSpeed04

    weather = randint(1, 5)
    timeDay = randint(1, 4)

    state01 = randint(1, 5)
    state02 = randint(1, 5)
    state03 = randint(1, 5)
    state04 = randint(1, 5)

    winCoeff01 = int(100 + randint(1, 30 + state01 * 60)) / 100
    winCoeff02 = int(100 + randint(1, 30 + state02 * 60)) / 100
    winCoeff03 = int(100 + randint(1, 30 + state03 * 60)) / 100
    winCoeff04 = int(100 + randint(1, 30 + state04 * 60)) / 100

    #Маркеры ситуаций
    reverse01 = False
    reverse02 = False
    reverse03 = False
    reverse04 = False

    play01 = True
    play02 = True
    play03 = True
    play04 = True

    fastSpeed01 = False
    fastSpeed02 = False
    fastSpeed03 = False
    fastSpeed04 = False

#Сбрасываем игру
def sbrosGame():
    global x01, x02, x03, x04, money
    #Сбрасываем виджеты
    startButton["state"] = "normal"
    stavka01["state"] = "readonly"
    stavka02["state"] = "readonly"
    stavka03["state"] = "readonly"
    stavka04["state"] = "readonly"
    stavka01.current(0)
    stavka02.current(0)
    stavka03.current(0)
    stavka04.current(0)

    #Сбрасываем координаты лошадей
    x01 = 20
    x02 = 20
    x03 = 20
    x04 = 20
    horsePlaceInWindow()

    #Обновляем интерфейс
    refreshCombo(eventObject="") #Обновляем выпадающие списки и чекбоксы
    viewWeather() #Выводит в чат погоду
    healthHorse() #Выводит в чат инфу о лошадях
    insertText(f"Ваши средства: {int(money)} {valuta}.") #Выводит в чат инфу о доступной сумме

    #Закрываем программу, если сумма средств на счету меньше 1
    if (money < 1):
        messagebox.showinfo("Стоп!", "На ипподром без денег заходить нельзя!")
        quit(0)

#Победа лошади
def winRound(horse):
    global x01, x02, x03, x04, money

    res = "К финишу пришла лошадь "
    if (horse == 1):
        res += nameHorse01
        win = summ01.get() * winCoeff01
    elif (horse == 2):
        res += nameHorse02
        win = summ02.get() * winCoeff02
    elif (horse == 3):
        res += nameHorse03
        win = summ03.get() * winCoeff03
    elif (horse == 4):
        res += nameHorse04
        win = summ04.get() * winCoeff04

    if (horse > 0):
        res += f"! Вы выиграли {int(win)} {valuta}. "
        if (win > 0):
            res += "Поздравляем! Средства уже зачислены на Ваш счёт!"
            insertText(f"Этот забег принёс Вам {int(win)} {valuta}.")
        else:
            res += "К сожелению, Ваша лошадь была неправильной. Попробуйте ещё раз!"
            insertText("Делайте ставку! Увеличивайте прибыль!")
        messagebox.showinfo("РЕЗУЛЬТАТ", res)
    else:
        messagebox.showinfo("Всё плохо", "До финиша не дошёл никто. Забег признан несостоявшимся. Все ставки возвращены.")
        insertText("Забег признан несостоявшимся.")
        win = summ01.get() + summ02.get() + summ03.get() + summ04.get()

    money += win
    saveMoney(int(money))

    #Сброс переменных
    setupHorse()
    #Сброс игры
    sbrosGame()

#Проблемы лошадей
def problemHorse():
    global reverse01, reverse02, reverse03, reverse04
    global play01, play02, play03, play04
    global state01, state02, state03, state04
    global fastSpeed01, fastSpeed02, fastSpeed03, fastSpeed04

    #Выбираем лошадь для события
    horse = randint(1, 4)

    #Чем выше число, тем ниже вероятность события
    maxRand = 10000

    if (horse == 1 and play01 == True and x01 > 0):
        if (randint(0, maxRand) < state01 * 5):
            #Маркер движения в обратный
            reverse01 = not reverse01
            #Сообщаем пользователю (выводи окно)
            messagebox.showinfo("Аааааа", f"Лошадь {nameHorse01} развернулась и бежит в другую сторону!")
        elif (randint(0, maxRand) < state01 * 5):
            #Лошадь остановилась
            play01 = False
            #Сообщаем
            messagebox.showinfo("Никогда такого не было и вот опять", f"{nameHorse01} заржала и скинула жокея!")
        elif (randint(0, maxRand) < state01 * 5 and not fastSpeed01):
            messagebox.showinfo("Великолепно!", f"{nameHorse01} перестала притворятся и ускорилась!")
            #Задаём множитель ускорения. Теперь точно побежит быстрее!
            fastSpeed01 = True

    elif (horse == 2 and play02 == True and x02 > 0):
        if (randint(0, maxRand) < state02 * 5):
            reverse02 = not reverse02
            messagebox.showinfo("Аааааа", f"Лошадь {nameHorse02} развернулась и бежит в другую сторону!")
        elif (randint(0, maxRand) < state02 * 5):
            play02 = False
            messagebox.showinfo("Никогда такого не было и вот опять", f"{nameHorse02} заржала и скинула жокея!")
        elif (randint(0, maxRand) < state02 * 5 and not fastSpeed02):
            messagebox.showinfo("Великолепно!", f"{nameHorse02} перестала притворятся и ускорилась!")
            fastSpeed02 = True

    elif (horse == 3 and play03 == True and x03 > 0):
        if (randint(0, maxRand) < state03 * 5):
            reverse03 = not reverse03
            messagebox.showinfo("Аааааа", f"Лошадь {nameHorse03} развернулась и бежит в другую сторону!")
        elif (randint(0, maxRand) < state03 * 5):
            play03 = False
            messagebox.showinfo("Никогда такого не было и вот опять", f"{nameHorse03} заржала и скинула жокея!")
        elif (randint(0, maxRand) < state03 * 5 and not fastSpeed03):
            messagebox.showinfo("Великолепно!", f"{nameHorse03} перестала притворятся и ускорилась!")
            fastSpeed03 = True

    elif (horse == 4 and play04 == True and x04 > 0):
        if (randint(0, maxRand) < state04 * 5):
            reverse04 = not reverse04
            messagebox.showinfo("Аааааа", f"Лошадь {nameHorse04} развернулась и бежит в другую сторону!")
        elif (randint(0, maxRand) < state04 * 5):
            play04 = False
            messagebox.showinfo("Никогда такого не было и вот опять", f"{nameHorse04} заржала и скинула жокея!")
        elif (randint(0, maxRand) < state04 * 5 and not fastSpeed04):
            messagebox.showinfo("Великолепно!", f"{nameHorse04} перестала притворятся и ускорилась!")
            fastSpeed04 = True

#Состояние лошадей в текстовой переменной
def getHealth(name, state, win):
    s = f"Лошадь {name} "
    if (state == 5):
        s += "мучается несварением желудка."
    elif (state == 4):
        s += "плохо спала. Подёргивается веко."
    elif (state == 3):
        s += "сурова и беспощадна."
    elif (state == 2):
        s += "в отличном настроении, покушала хорошо."
    elif (state == 1):
        s += "просто ракета!"

    s += f" ({win}:1)"
    return s

#Отображение состояние лошадей
def healthHorse():
    insertText(getHealth(nameHorse01, state01, winCoeff01))
    insertText(getHealth(nameHorse02, state02, winCoeff02))
    insertText(getHealth(nameHorse03, state03, winCoeff03))
    insertText(getHealth(nameHorse04, state04, winCoeff04))

#Вывод погоды
def viewWeather():
    s = "Сейчас на ипподроме "
    if (timeDay == 1):
        s += "ночь, "
    elif (timeDay == 2):
        s += "утро, "
    elif (timeDay == 3):
        s += "день, "
    elif (timeDay == 4):
        s += "вечер, "

    if (weather == 1):
        s += "льёт сильный дождь."
    elif (weather == 2):
        s += "моросит дождик."
    elif (weather == 3):
        s += "облачно, на горизонте тучи."
    elif (weather == 4):
        s += "безоблачно, ветер."
    elif (weather == 5):
        s += "безоблачно, прекрасная погода!"
    insertText(s)

#Перемещение лошадей
def moveHorse():
    global x01, x02, x03, x04

    #Проблемы лошадей
    if (randint(0, 100) < 20):
        problemHorse()

    #Рассчитываем скорость для каждой лошади
    speed01 = (randint(1, timeDay + weather) + randint(1, int((7 - state01)) * 3)) / randint(10, 175)
    speed02 = (randint(1, timeDay + weather) + randint(1, int((7 - state02)) * 3)) / randint(10, 175)
    speed03 = (randint(1, timeDay + weather) + randint(1, int((7 - state03)) * 3)) / randint(10, 175)
    speed04 = (randint(1, timeDay + weather) + randint(1, int((7 - state04)) * 3)) / randint(10, 175)

    # Множитель скорости
    multiple = 3
    speed01 *= int(randint(1, 2 + state01) * (1 + fastSpeed01 * multiple))
    speed02 *= int(randint(1, 2 + state02) * (1 + fastSpeed02 * multiple))
    speed03 *= int(randint(1, 2 + state03) * (1 + fastSpeed03 * multiple))
    speed04 *= int(randint(1, 2 + state04) * (1 + fastSpeed04 * multiple))

    #Вправо или влево бежит лошадь?
    if (play01):
        if (not reverse01):
            x01 += speed01
        else:
            x01 -= speed01

    if (play02):
        if (not reverse02):
            x02 += speed02
        else:
            x02 -= speed02

    if (play03):
        if (not reverse03):
            x03 += speed03
        else:
            x03 -= speed03

    if (play04):
        if (not reverse04):
            x04 += speed04
        else:
            x04 -= speed04

    horsePlaceInWindow()

    #Текущая ситуация
    allPlay = play01 or play02 or play03 or play04
    allX = x01 < 0 and x02 < 0 and x03 < 0 and x04 < 0
    allReverse = reverse01 and reverse02 and reverse03 and reverse04

    #Если всё плохо и никто не дошёл до финиша
    if (not allPlay or allX or allReverse):
        winRound(0)
        return 0

    # Если не на финише
    if(x01 < 952 and
       x02 < 952 and
       x03 < 952 and
       x04 < 952):
        root.after(5, moveHorse)
    else:
        if (x01 >= 952):
            winRound(1)
        elif (x02 >= 952):
            winRound(2)
        elif (x03 >= 952):
            winRound(3)
        elif (x04 >= 952):
            winRound(4)

#При нажатии на кнопку СТАРТ
def runHorse():
    global money
    startButton["state"] = "disabled"   #Блокируем изменение ставок и нажатие на кнопку СТАРТ
    stavka01["state"] = "disabled"
    stavka02["state"] = "disabled"
    stavka03["state"] = "disabled"
    stavka04["state"] = "disabled"
    money -= summ01.get() + summ02.get() + summ03.get() + summ04.get()
    moveHorse()

#Вызывается каждый раз при выборе любого Combobox
def refreshCombo(eventObject):
    summ = summ01.get() + summ02.get() + summ03.get() + summ04.get()
    labelAllMoney["text"] = f"У вас на счету: {int(money - summ)} {valuta}." #вывод суммы после ставки

    #Определяем значения ставки в списке (1/10), после каждой поставленной суммы
    stavka01["values"] = getValues(int(money - summ02.get() - summ03.get() - summ04.get()))
    stavka02["values"] = getValues(int(money - summ01.get() - summ03.get() - summ04.get()))
    stavka03["values"] = getValues(int(money - summ02.get() - summ01.get() - summ04.get()))
    stavka04["values"] = getValues(int(money - summ02.get() - summ03.get() - summ01.get()))

    #Включаем или выключаем кнопку СТАРТ
    if(summ > 0):
        startButton["state"] = "normal"
    else:
        startButton["state"] = "disabled"

    #Если ставка поставлена программа ставит галочку в чекбокс
    if(summ01.get() > 0):
        horse01Game.set(True)
    else:
        horse01Game.set(False)

    if (summ02.get() > 0):
        horse02Game.set(True)
    else:
        horse02Game.set(False)

    if (summ03.get() > 0):
        horse03Game.set(True)
    else:
        horse03Game.set(False)

    if (summ04.get() > 0):
        horse04Game.set(True)
    else:
        horse04Game.set(False)

#Список значений для Combobox
def getValues(summa):   #Вывод списка ставок
    value = []
    if(summa > 9):                  #Если money > 9 выводим ставку 1/10
        for i in range(0, 11):
            value.append(i * (int(summa) // 10))
    else:                           #Иначе ставка становится либо 0, либо money
        value.append(0)
        if(summa > 0):
            value.append(summa)
    return value

#Чтение из файла оставшейся суммы
def loadMoney():
    try:
        f = open("money.dat", "r")
        m = int(f.readline())
        f.close()
    except FileNotFoundError:
        insertText(f"Файла не существует, задано значение {defaultMoney} {valuta}")
        m = defaultMoney
    return m

#Запись суммы в файл
def saveMoney(moneyToSave):
    try:
        f = open("money.dat", "w")
        f.write(str(moneyToSave))
        f.close()
    except:
        insertText("Ошибка создания файла, наш Ипподром закрывается!")
        quit(0)

#Добавления строки в текстовый блок
def insertText(s):
    textDiary.insert(INSERT, s + "\n")
    textDiary.see(END)

#координаты лошадей на экране
def horsePlaceInWindow():
    horse01.place(x=int(x01), y=20)
    horse02.place(x=int(x02), y=100)
    horse03.place(x=int(x03), y=180)
    horse04.place(x=int(x04), y=260)

root = Tk()

#*************************************************************
#       Переменные
#*************************************************************

#Размеры окна программы
WIDTH = 1024
HEIGHT = 600

#Позиции лошадей
x01 = 20
x02 = 20
x03 = 20
x04 = 20

#финансовые показатели
defaultMoney = 10000
money = 0
valuta = "руб"

#Клички лошадей
nameHorse01 = "Ананас"
nameHorse02 = "Сталкер"
nameHorse03 = "Прожорливый"
nameHorse04 = "Копытце"

#Погода
#1 - ливень, ураган
#5 - безоблачно
weather = randint(1, 5)

#Время суток
#1 - ночь
#2 - утро
#3 - день
#4 - вечер
timeDay = randint(1, 4)

#Состояние лошадей
#1 - Великолепное
#5 - Ужасно плохое
state01 = randint(1, 5)
state02 = randint(1, 5)
state03 = randint(1, 5)
state04 = randint(1, 5)

#Коэффициент выгрыша
winCoeff01 = int(100 + randint(1, 30 + state01 * 60)) / 100
winCoeff02 = int(100 + randint(1, 30 + state02 * 60)) / 100
winCoeff03 = int(100 + randint(1, 30 + state03 * 60)) / 100
winCoeff04 = int(100 + randint(1, 30 + state04 * 60)) / 100

#Маркеры ситуаций
reverse01 = False
reverse02 = False
reverse03 = False
reverse04 = False

play01 = True
play02 = True
play03 = True
play04 = True

fastSpeed01 = False
fastSpeed02 = False
fastSpeed03 = False
fastSpeed04 = False

#*************************************************************
#       Формирование эллементов в окне
#*************************************************************

#Создаём главное окно
#Вычисляем координаты для размещения окна по центру
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2

#Установка заголовка окна
root.title("ИППОДРОМ")

#Запрет изменения размеров окна
root.resizable(False, False)

#Устанавливаем ширину, высоту и позицию окна
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

#Изображение фона(дороги)
road_image = PhotoImage(file="road.png")            #Загружаем изображение
road = Label(root, image=road_image)                #Устанавливаем фото в Label
road.place(x=0, y=17)                               #Выводим фото в окно

#Изображения лошадей на экране
horse01_image = PhotoImage(file="horse01.png")      #Загружаем изображение
horse01 = Label(root, image=horse01_image)          #Устанавливаем фото в Label

horse02_image = PhotoImage(file="horse02.png")
horse02 = Label(root, image=horse02_image)

horse03_image = PhotoImage(file="horse03.png")
horse03 = Label(root, image=horse03_image)

horse04_image = PhotoImage(file="horse04.png")
horse04 = Label(root, image=horse04_image)

#Координаты лошадок на экране
horsePlaceInWindow()

#Создаём кнопку СТАРТ и выводим её на экран
startButton = Button(text="СТАРТ", font="arial 20", width=61, background="#37AA37")
startButton.place(x=20, y=370)
startButton["state"] = "disabled"

#Создаём чат с информацией виджетом TEXT
textDiary = Text(width=70, height=8, wrap=WORD)
textDiary.place(x=430, y=450)

#Создаём и прикрепляем к тексту полосу прокрутки
scroll = Scrollbar(command=textDiary.yview, width=20)
scroll.place(x=990, y=450, height=132)
textDiary["yscrollcommand"] = scroll.set

#загрузка средств игрока из файла
money = loadMoney()

#Если у игрока нет денег, выгоняем
if(money <= 0):
    messagebox.showinfo("Стоп!", "На ипподром без средств заходить нельзя!")
    quit(0)

#Формируем текстовую строку и выводим в неё оставшуюся сумму средств
labelAllMoney = Label(text=f"Осталось средств: {money} {valuta}.", font="Arial 12")
labelAllMoney.place(x=20, y=565)

#выводим текстовые метки в левом нижнем углу окна
labelHorse01 = Label(text="Ставка на лошадь №1")
labelHorse01.place(x=20, y=450)

labelHorse02 = Label(text="Ставка на лошадь №2")
labelHorse02.place(x=20, y=480)

labelHorse03 = Label(text="Ставка на лошадь №3")
labelHorse03.place(x=20, y=510)

labelHorse04 = Label(text="Ставка на лошадь №4")
labelHorse04.place(x=20, y=540)

#Чекбоксы для лошадок
horse01Game = BooleanVar()
horse01Game.set(0)
horseCheck01 = Checkbutton(text=nameHorse01, variable=horse01Game, onvalue=1, offvalue=0)
horseCheck01.place(x=150, y=448)

horse02Game = BooleanVar()
horse02Game.set(0)
horseCheck02 = Checkbutton(text=nameHorse02, variable=horse02Game, onvalue=1, offvalue=0)
horseCheck02.place(x=150, y=478)

horse03Game = BooleanVar()
horse03Game.set(0)
horseCheck03 = Checkbutton(text=nameHorse03, variable=horse03Game, onvalue=1, offvalue=0)
horseCheck03.place(x=150, y=508)

horse04Game = BooleanVar()
horse04Game.set(0)
horseCheck04 = Checkbutton(text=nameHorse04, variable=horse04Game, onvalue=1, offvalue=0)
horseCheck04.place(x=150, y=538)

#Запрещаем пользователю изменять значение чекбоксов
horseCheck01["state"] = "disabled"
horseCheck02["state"] = "disabled"
horseCheck03["state"] = "disabled"
horseCheck04["state"] = "disabled"

#Выпадающий список
stavka01 = ttk.Combobox(root)
stavka02 = ttk.Combobox(root)
stavka03 = ttk.Combobox(root)
stavka04 = ttk.Combobox(root)

#Задаём атрибут "Только чтение"
stavka01["state"] = "readonly"
stavka01.place(x=280, y=450)

stavka02["state"] = "readonly"
stavka02.place(x=280, y=480)

stavka03["state"] = "readonly"
stavka03.place(x=280, y=510)

stavka04["state"] = "readonly"
stavka04.place(x=280, y=540)

#Определяем переменные для хранения значений из Combobox
summ01 = IntVar()
summ02 = IntVar()
summ03 = IntVar()
summ04 = IntVar()

#Привязываем переменные к Combobox
#В них будет храниться выбранное в виджите значение
stavka01["textvariable"] = summ01
stavka02["textvariable"] = summ02
stavka03["textvariable"] = summ03
stavka04["textvariable"] = summ04

stavka01.bind("<<ComboboxSelected>>", refreshCombo)
stavka02.bind("<<ComboboxSelected>>", refreshCombo)
stavka03.bind("<<ComboboxSelected>>", refreshCombo)
stavka04.bind("<<ComboboxSelected>>", refreshCombo)

#Обновляем значения Combobox
refreshCombo("")

#Устанавливаем самое первое значение списка равное 0
stavka01.current(0)
stavka02.current(0)
stavka03.current(0)
stavka04.current(0)

startButton["command"] = runHorse

viewWeather()
healthHorse()

#Вывод окна на экран
root.mainloop()