from tkinter import *
from tkinter import messagebox
from random import randint
import time

#time.sleep(0)
# ***********************************************
#               Методы
# ***********************************************
def barabann(times):
    global baraban, btn, bar
    bar = 0
    # Закрываем кнопки на время рандома
    for i in range(3, len(btn)):
        btn[i]["state"] = "disabled"
    exitButton["state"] = "disabled"

    # Рандом барабана
    for i in range(len(barabanList)):
        baraban = randint(0, len(barabanList) - 1)
        # Время рандома барабана
        time.sleep(times)
        bar = barabanList[baraban]
        barabanLable["text"] = f"Выпало число: {bar}"
        # Обновляем информацию виджета в окне
        root.update()

    return btn, bar, time.sleep(0)

# Очистить текст
def clearText():
    textDiary.delete(1.0, END)

# Добавления строки в текстовый блок
def insertText(s):
    textDiary.configure(state='normal')
    clearText()
    textDiary.insert(INSERT, s + "\n")
    textDiary.see(END)
    textDiary.configure(state='disabled')

# Метод при нажатии на клаву
def pressKey(event):
    # Чит на CTRL
    if (event.keycode == 17):
        wordLabel["text"] = wordComp
        root.update()
        time.sleep(0.5)
        wordLabel["text"] = wordStar
        root.update()

    # Получим код символа нажатого
    ch = event.char.upper()
    if (len(ch) == 0):
        return 0

    # Определяем номер нажатого символа в рус. алфавите
    codeBtn = ord(ch) - st
    if (codeBtn >= 0 and codeBtn <= 32):
        pressLetter(codeBtn)

# Обновляем информацию об очках и т.п.
def updateInfo():
    scoreLabel["text"] = f"Ваши очки: {score}"
    topScoreLabel["text"] = f"Лучший результат: {topScore}"
    userTryLabel["text"] = f"Осталось попыток: {userTry}"

# Сохраняем очки в файл
def saveTopScore():
    # Обязательно global, чтобы изменить topScore
    global topScore

    # Изменяем
    topScore = score

    # Открываем файл и записываем
    try:
        f = open("topchik.dat", "w", encoding="utf-8")
        f.write(str(topScore))
        f.close()
    # Если ошибка создания и записи
    except:
        messagebox.showinfo("Ошибка",
                            "Возникла проблема с файлом сохранения очков")

# Возвращает максимальное значение очков из файла
def getTopScore():
    try:
        f = open("topchik.dat", "r", encoding="utf-8")
        m = int(f.readline())
        f.close()
    except:
        m = 0
    return m

# ============================================ Двумерный список ==============================================
# Загружает слова в список
# Считывает из файла, формирует и возвращает двумерный список данных
def getFileString(filename):
    # Создаём список, который вернём
    ret = []

    try:
        f = open(filename, "r", encoding="utf-8")

        # Обрабатываем каждую строку информации из файла
        for line in f.readlines():
            line = line.replace("\n", "")
            line = line.split("#")
            ret.append(line)

        f.close()
    except:
        # Если что-то пошло не так
        print("Ошибка открытия! Проверьте правильность имени и пути.")

    # Вернём сформированный список
    return ret
# ============================================================================================================

# Сравниваем строки и считаем,
# сколько символов различаются
def compareWord(s1, s2):
    # Возвращаемый результат
    res = 0

    # Сравниваем s1 и s2 посимвольно
    for i in range(len(s1)):
        if (s1[i][0] != s2[i][0]):
            # Если символы разные, то увеличиваем res
            res += 1
    return res

# Возвращаем слово с открытыми символами
def getWordStar(ch):
    # Переменная для результата
    ret = ""

    for i in range(len(wordComp)):
        # Сравниваем символы
        if (wordComp[i][0] == ch):
            ret += ch
        else:
            ret += wordStar[i][0]
    return ret

# Удаляем лишние слова(которые уже загадывались)
def clearSpisok(dictionary01):
    global dictionary, dictionaryovtor

    # Если слово загадано, добавляем его в новый список "повторок"
    for i in range(len(dictionary01)):
        if (dictionary01[i][0] == wordComp):
            dictionaryovtor.append(dictionary01[i][0])
            break
    # И потом список "чистый" сравниваем со списком повторных, если слово поторное,
    # то удаляем его в списке dictionary01
    for o in range(len(dictionaryovtor)):
        if (dictionaryovtor[o] == wordComp):
            for j in range(len(dictionary01)):
                try:
                    if (dictionary01[j][0] == dictionaryovtor[o]):
                        del dictionary01[j]
                except:
                        #print("Повторки:", dictionaryovtor)
                        pass
                        #...

    # Вывод списков в консоль
    #print("Вывод чистого списка:", dictionary01)
    #print("Ещё 1 вывод поторок:", dictionaryovtor)
    return dictionary01

# Остановка игры
def stopGame():
    global dictionary01, dictionaryovtor, play, dictionary00, bar
    if (play == 4 and dictionary00 == []):
        dictionary01 = getFileString("words.dat")
        dictionaryovtor.clear()
        play = 0
        dictionary00 = dictionary01.copy()
        bar = 0
    return dictionary01, dictionaryovtor, play, dictionary00, bar


# Начало нового раунда
def startNewRound():
    global wordStar, wordComp, userTry, play, dictionaryovtor, dictionary00, bar

    # Это необходимо, питон ругается
    clearSpisok(dictionary00)
    # Завершение игры, предотвращает ошибку(мне лень это делать, пока что и я очень устал писать этот вариант)
    stopGame()
    # Загадываем слово
    wordComp = dictionary00[randint(0, len(dictionary00) - 1)][0]
    if (play != 0):
        for i in range(len(dictionary00)):
            if(dictionary00[i][0] == wordComp):
                insertText(dictionary00[i][1])
                # Время рандома барабана
                barabann(randint(1, 5) / 10)
    else:
        for i in range(len(dictionary01)):
            if(dictionary01[i][0] == wordComp):
                insertText(dictionary01[i][1])
                # Если запуск 1 раз, то время рандома барабана = 0
                barabann(0)

    # Запускаем очистку списка
    clearSpisok(dictionary00)

    # Формируем строку из "*"
    wordStar = "*" * len(wordComp)

    # Устанавливаем текст в метку
    wordLabel["text"] = wordStar

    # Устанавливаем метку по центру для вывода слова
    wordLabel.place(x=WIDTH // 2 - wordLabel.winfo_reqwidth() // 2, y=200)

    # Сбрасываем кнопки
    for i in range(32):
        btn[i]["text"] = chr(st + i)
        btn[i]["state"] = "normal"
    exitButton["state"] = "normal"

    # Сбрасываем попытки
    userTry = 10

    # Обновляем информацию в окне
    updateInfo()

# При нажатии на кнопку мышкой
def pressLetter(n):
    global wordStar, score, userTry, wordComp, play
    # Проверяем, если эта буква уже была выбрана, то прерываем метод
    if (btn[n]["text"] == "."):
        return 0

    btn[n]["text"] = "."
    btn[n]["state"] = "disabled"

    # Временная переменная
    oldWordStar = wordStar

    # Получаем строку с открытыми символами
    wordStar = getWordStar(chr(st + n))

    # Находим различие между старой и новой строкой
    count = compareWord(wordStar, oldWordStar)

    wordLabel["text"] = wordStar

    # Считаем очки
    if (count > 0):
        score += count * 5
    else:
        score -= 20

        # Проверка, чтобы не было score < 0
        if (score < 0):
            score = 0

        # Уменьшаем количество попыток
        userTry -= 1

    # Обновляем информацию в окне
    updateInfo()

    # Сравниваем загаданное слово с wordStar
    if (wordComp == wordStar):
        # Увеличиваем
        play += 1
        # Добавляем 25% очков
        score += score // 4

        if (bar == barabanList[3] and score <= 100):
            score += ((bar * len(wordComp)) // 2 * -1) - bar
        elif (bar == barabanList[3] and score > 100):
            score += (bar * len(wordComp)) // 2
        else:
            score += (bar * len(wordComp)) // 2

        # Обновляем информацию
        updateInfo()

        # Если человек заработал больше, чем свой рекорд, то сообщаем и записываем в файл
        if (score > topScore):
            messagebox.showinfo("Поздравляю!",
                                f"Вы - топчик! Угадано слово: {wordComp}! Нажмите ок для продолжения игры.")
            # Метод записи очков
            saveTopScore()
        else:
            messagebox.showinfo("Отлично", f"Слово угадано: {wordComp}! Продолжаем играть дальше!")

        # Запускаем новый раудн
        startNewRound()

    # Если очков < 0, то выгоняем
    elif (score < 0):
        messagebox.showinfo("Бу!", "ГГ вы проиграли")
        quit(0)

    # Если попыток 0, то генерируем новый раунд
    elif (userTry <= 0):
        play += 1
        if (bar != barabanList[3]):
            score -= bar * len(wordStar) * 2
        else:
            score += bar * len(wordStar) * 2
        updateInfo()
        messagebox.showinfo("Некст", "Запускаем следующую игру!")
        startNewRound()

# Создание окна
root = Tk()                     # В переменной root хранится ссылка на окно в памяти
root.resizable(False, False)    # Запрещаем изменять размер
root.title("Поле чудес")        # Устанавливаем заголовок

# Настрока геометрии окна
WIDTH = 1920        # Ширина
HEIGHT = 1080       # Высота

# Экран пользователя
SCR_WIDTH = root.winfo_screenwidth()    # Ширина экрана в пикселях
SCR_HEIGHT = root.winfo_screenheight()  # Высота экрана в пикселях

# Расположение окна на экране
POS_X = SCR_WIDTH // 2 - WIDTH // 2     # Координата по X
POS_Y = SCR_HEIGHT // 2 - HEIGHT // 2   # Координата по Y

# Устанавливаем нужные параметры экрана
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

# Метка для вывода слова, которое угадывает человек в текущем раунде
wordLabel = Label(font="consolas 35")

# Метки для отображения текущих очков и рекорда
scoreLabel = Label(font=", 12")
topScoreLabel = Label(font=", 12")

# Метка оставшихся попыток
userTryLabel = Label(font=", 12")

# Метка для вывода "барабана"
barabanLable = Label(font=", 12")

# Устанавливаем метки в окне
scoreLabel.place(x=10, y=165)
topScoreLabel.place(x=10, y=190)
userTryLabel.place(x=10, y=215)
barabanLable.place(x=460, y=500)

# Переменные для хранения значений
score = 0                                                   # Текущие очки
topScore = getTopScore()                                    # Рекорд игры
userTry = 10                                                # Количество попыток
barabanList = [100, 200, 300, -100, 250, 350, 500]          # Список для барабана
baraban = 0                                                 # Барабан
bar = 0                                                     # Значение на барабане

# Для определения символа на кнопке по коду
st = ord("А")

# Список для хранения кодов
# Список кнопок
btn = []

# ------------------------------------------------------------------------------------------------------------------
# Список для загрузки словаря
dictionary01 = getFileString("words.dat")

# Список с повторками
dictionaryovtor = []

# Список копия
dictionary00 = dictionary01.copy()

# Счётчик, когда игра закончится
play = 0
# ------------------------------------------------------------------------------------------------------------------

# Работем с кнопками
# Вывод кнопок на экран
for i in range(32):
    btn.append(Button(text=chr(st + i), width=2, font="consolas 15"))   # Создаём и добавляем в список
    btn[i].place(x=750 + (i % 11) * 35, y=270 + i // 11 * 50)           # Устанавливаем на экран
    btn[i]["command"] = lambda x = i : pressLetter(x)                   # Определяем переход на метод с
                                                                        # передачей аргументом номера кнопки

# Определяем глобально: "загаданное слово"
wordComp = ""
# Определяем глобально: "слово со звёздочками"
wordStar = ""

# Словарь
dictionary = getFileString("words.dat")

# Установка обработки клавиш
root.bind("<Key>", pressKey)

# Создаём чат с информацией виджетом TEXT
textDiary = Text(width=122, height=8, wrap=WORD)
textDiary.place(x=460, y=20)
textDiary.configure(state='disabled')

# Создаём и прикрепляем к тексту полосу прокрутки
scroll = Scrollbar(command=textDiary.yview, width=20)
scroll.place(x=1440, y=20, height=132)
textDiary["yscrollcommand"] = scroll.set

# Кнопка выхода
exitButton = Button(text="Выход", width=20, height=5, background="red", font="consolas 15")
exitButton.place(x=1650, y=850)
exitButton["command"] = exit

# Стартуем
startNewRound()

# Запуск окна
root.mainloop()