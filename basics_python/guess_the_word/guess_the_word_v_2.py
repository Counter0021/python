from tkinter import *
from tkinter import messagebox
from random import randint

# ***********************************************
#               Методы
# ***********************************************

# ------------------------------------------------------------------------------------------------------------------
# Загружаем словарь из файла
def dictionaryFromFile():
    global dictionary
    dictionary = getWordsFromFile()
    return dictionary
# ------------------------------------------------------------------------------------------------------------------

# Метод при нажатии на клавиатуру
def pressKey(event):
    # CTRL чит
    if (event.keycode == 17):
        wordLabel["text"] = wordComp

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

# Загружает слова в список
def getWordsFromFile():
    # Переменная-список для возвращаемого результата
    ret = []

    # Составим блок проверки ошибок
    try:
        # Получаем дескриптор. Кодировка utf-8
        f = open("words.dat", "r", encoding="utf-8")

        # Читаем по строчно
        for l in f.readlines():
            # Обязательно убираем последний символ переноса строки
            l = l.replace("\n", "")

            # Добавляем слово в список
            ret.append(l)

        # Закрываем файл
        f.close()
    except:
        # Если ошибка
        print("Проблема с файлом. Программа прекращает работу.")
        quit(0)

    # Возвращаем список
    return ret

# Сравниваем строки и считаем,
# сколько символов различаются
def compareWord(s1, s2):
    # Возвращаемый результат
    res = 0

    # Сравниваем s1 и s2 посимвольно
    for i in range(len(s1)):
        if (s1[i] != s2[i]):
            # Если символы разные, то увеличиваем res
            res += 1
    return res

# Возвращаем слово с открытыми символами
def getWordStar(ch):
    # Переменная для результата
    ret = ""

    for i in range(len(wordComp)):
        # Сравниваем символы
        if (wordComp[i] == ch):
            ret += ch
        else:
            ret += wordStar[i]
    return ret

# ------------------------------------------------------------------------------------------------------------------
# Удаляем лишние слова(которые уже загадывались)
def clearSpisok(dictionary01):
    global dictionary, dictionaryovtor

    # Если слово загадано, добавляем его в новый список "повторок"
    for i in range(len(dictionary01)):
        if (dictionary01[i] == wordComp):
            dictionaryovtor.append(dictionary01[i])
            break
    # И потом список "чистый" сравниваем со списком повторных, если слово поторное,
    # то удаляем его в списке dictionary01 и выводим в консоль повторки
    for o in range(len(dictionaryovtor)):
        if (dictionaryovtor[o] == wordComp):
            for j in range(len(dictionary01)):
                try:
                    if (dictionary01[j] == dictionaryovtor[o]):
                        del dictionary01[j]
                except:
                        print("Повторки:", dictionaryovtor)
    # Вывод списков в консоль
    print("Вывод чистого списка:", dictionary01)
    print("Ещё 1 вывод поторок:", dictionaryovtor)
    return dictionary01
# =================================================================================================================
#                                   Исправлен баг с вылетом программы
# =================================================================================================================
# Остановка игры
def stopGame():
    global dictionary01, dictionaryovtor, play
    if (play == 5 and dictionary01 == []):
        print("СТОП")
        dictionary01 = dictionaryFromFile()
        dictionaryovtor.clear()
        play = 0
    return dictionary01, dictionaryovtor, play

# =================================================================================================================

# Начало нового раунда
def startNewRound():
    global wordStar, wordComp, userTry, play, dictionaryovtor, dictionary0, count

    # Это необходимо, питон ругается
    clearSpisok(dictionary01)
    # Завершение игры, предотвращает ошибку(мне лень это делать, пока что и я очень устал писать этот вариант)
    stopGame()
    # Загадываем слово
    wordComp = dictionary01[randint(0, len(dictionary01) - 1)]
    # Запускаем очистку списка
    clearSpisok(dictionary01)

    # Формируем строку из "*"
    wordStar = "*" * len(wordComp)

    # Устанавливаем текст в метку
    wordLabel["text"] = wordStar

    # Устанавливаем метку по центру для вывода слова
    wordLabel.place(x=WIDTH // 2 - wordLabel.winfo_reqwidth() // 2, y=50)

    # Сбрасываем кнопки
    for i in range(32):
        btn[i]["text"] = chr(st + i)
        btn[i]["state"] = "normal"

    # Сбрасываем попытки
    userTry = 10

    # Обновляем информацию в окне
    updateInfo()

# ------------------------------------------------------------------------------------------------------------------

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
        score -= 10

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
        # Добавляем 50% очков
        score += score // 2

        # Обновляем информацию
        updateInfo()

        # Если человек заработал больше, чем свой рекорд, то сообщаем и записываем в файл
        if (score > topScore):
            messagebox.showinfo("Поздравляю!", f"Вы - топчик! Угадано слово: {wordComp}! Нажмите ок для продолжения игры.")
            # Метод записи очков
            saveTopScore()
        else:
            messagebox.showinfo("Отлично", f"Слово угадано: {wordComp}! Продолжаем играть дальше!")

        # Запускаем новый раудн
        startNewRound()

    elif (userTry <= 0):
        messagebox.showinfo("Бу!", "ГГ вы проиграли")
        quit(0)
# ------------------------------------------------------------------------------------------------------------------

# Создание окна
root = Tk()                     # В переменной root хранится ссылка на окно в памяти
root.resizable(False, False)    # Запрещаем изменять размер
root.title("Угадай слово")      # Устанавливаем заголовок

# Настрока геометрии окна
WIDTH = 810    # Ширина
HEIGHT = 320   # Высота

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

# Устанавливаем метки в окне
scoreLabel.place(x=10, y=165)
topScoreLabel.place(x=10, y=190)
userTryLabel.place(x=10, y=215)

# Переменные для хранения значений
score = 0                 # Текущие очки
topScore = getTopScore()  # Рекорд игры
userTry = 10              # Количество попыток

# Для определения символа на кнопке по коду
st = ord("А")
# Список для хранения кодов
# Список кнопок
btn = []

# ------------------------------------------------------------------------------------------------------------------
# Список для загрузки словаря
dictionary01 = dictionaryFromFile()

# Список с повторками
dictionaryovtor = []

# Счётчик, когда игра закончится
play = 0
# ------------------------------------------------------------------------------------------------------------------

# Работем с кнопками
# Вывод кнопок на экран
for i in range(32):
    btn.append(Button(text=chr(st + i), width=2, font="consolas 15"))   # Создаём и добавляем в список
    btn[i].place(x=215 + (i % 11) * 35, y=150 + i // 11 * 50)           # Устанавливаем на экран
    btn[i]["command"] = lambda x = i : pressLetter(x)                   # Определяем переход на метод с
                                                                        # передачей аргументом номера кнопки

# Определяем глобально: "загаданное слово"
wordComp = ""
# Определяем глобально: "слово со звёздочками"
wordStar = ""

# Установка обработки клавиш
root.bind("<Key>", pressKey)

# Стартуем
startNewRound()

# Запуск окна
root.mainloop()