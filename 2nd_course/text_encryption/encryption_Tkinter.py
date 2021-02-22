from tkinter import *

# Расшифровка текста
def goDecode():
    # Если справа один из чекбоксов принял "True"
    if (rBtn.get() == 0 or rBtn.get() == 1):    # Если 0 или 1, то запускаем метод goCode()
        goCode()
    else:                                       # Иначе
        tOutput.delete(1.0, END)
        tIn = tInput.get(1.0, END)
        tIn = tIn[0:len(tIn) - 1]
        tOut = ""
        if (rBtn.get() == 2):                   # Если 2, то код символа введённой строки - 1
            for i in range(len(tIn)):
                tOut += chr(ord(tIn[i]) - 1)
        elif (rBtn.get() == 3):                 # Иначе если 3, то код символа введённой строки - p,
            p = 0                               # p + 1, пока не дойдёт до 33
            for i in range(len(tIn)):
                tOut += chr(ord(tIn[i]) - p)
                p = (p + 1) % 33
        # Выводим строку tOutput
        tOutput.insert(1.0, tOut)

# Шифровка текста
def goCode():
    # Очищаем строку tOutput
    tOutput.delete(1.0, END)
    tIn = tInput.get(1.0, END)
    # Убираем перенос строки
    tIn = tIn[0:len(tIn) - 1]
    tOut = ""

    # Если справа один из чекбоксов принял "True"
    if (rBtn.get() == 0):                       # Если 0, то запускаем инверсию текста
        for i in range(len(tIn) - 1, -1, -1):
            tOut += tIn[i]
    elif (rBtn.get() == 1):                     # Иначе если 1, запускаем замену с соседней
        for i in range(0, len(tIn) -1, 2):
            tOut += tIn[i + 1] + tIn[i]
    elif (rBtn.get() == 2):                     # Иначе если 2, добавляем к коду символа 1 (+1)
        for i in range(len(tIn)):
            tOut += chr(ord(tIn[i]) + 1)
    elif (rBtn.get() == 3):                     # Иначе если 3, добавляем к коду символа + позицию (до 33)
        p = 0
        for i in range(len(tIn)):
            tOut += chr(ord(tIn[i]) + p)
            p = (p + 1) % 33
    # Выводим строку tOutput
    tOutput.insert(1.0, tOut)

# Очистить текст
def clearText():
    tInput.delete(1.0, END)
    tOutput.delete(1.0, END)

# Результат -> Исходный
def resToDef():
    tInput.delete(1.0, END)
    txt = tOutput.get(1.0, END)
    txt = txt[0:len(txt) - 1]
    tInput.insert(1.0, txt)

# Вставить из буфера обмена текст
def pasteFromClipboard():
    try:
        tInput.insert(END, root.clipboard_get())
    except:
        # Если Нет текста выдаём "Буфер пуст"
        tInput.insert(END, "\nОШИБКА: Буфер пуст")

# Копировать текст в буфер
def copyToClipboard():
    root.clipboard_clear()
    root.clipboard_append(tOutput.get(1.0, END))

# Позиция меню
def setMenuPos(event):
    menuInput.post(event.x_root, event.y_root)

#************************************************************
#               Окно программмы
#************************************************************
# Инциализация окна
root = Tk()
root.resizable(False, False)
root.title("Шифровщик")

# Настройка геометрии окна
WIDTH = 800
HEIGHT = 320
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

# Текстовые метки
textInput = Label(text="Введите исходный текст:")
textInput.place(x=2, y=1)
textOutput = Label(text="Результат:")
textOutput.place(x=2, y=157)

#************************************************************
#                   Текстовые поля

# Текстовое поле tInput
tInput = Text(width=70, height=8, wrap=WORD)
tInput.place(x=5, y=20)

# Ввод текста программой(читы)(чтобы его не писать)
tInput.insert(1.0, """Экземпляры Checkbutton также могут быть визуально оформлены в группу,
но каждый флажок независим от остальных. Каждый может быть в состоянии
"установлен" или "снят", независимо от состояния других флажков. Другими словами, в группе Checkbutton можно сделать множественный выбор, в группе Radiobutton - нет.""")

# Колесо прокрутки к тексту tInput
scrollInput = Scrollbar(command=tInput.yview, width=20)
scrollInput.place(x=570, y=20, height=132)
tInput["yscrollcommand"] = scrollInput.set

# Текстовое поле tOutput
tOutput = Text(width=70, height=8, wrap=WORD)
tOutput.place(x=5, y=180)

# Колесо прокрутки к тексту tOutput
scrollOutput = Scrollbar(command=tOutput.yview, width=20)
scrollOutput.place(x=570, y=180, height=132)
tOutput["yscrollcommand"] = scrollOutput.set

# Меню на правую кнопку
menuInput = Menu(tearoff=False)
menuInput.add_command(label="Копировать результат", command=copyToClipboard)
menuInput.add_command(label="Вставить в исходный текст", command=pasteFromClipboard)
menuInput.add_command(label="Результат -> Исходный", command=resToDef)
menuInput.add_command(label="Очистить текст", command=clearText)
tInput.bind("<Button-3>", setMenuPos)

# Кнопка Шифровать
btnCode = Button(text="Шифровать", width=25, command=goCode)
btnCode.place(x=600, y=20)

#Кнопка Дешифровать
btnDecode = Button(text="Дешифровать", width=25, command=goDecode)
btnDecode.place(x=600, y=50)

# Радиокнопки
textAlgo = Label(text="Алгоритм:")
textAlgo.place(x=600, y=100)
rBtn = IntVar()
rBtn.set(0)

# Надпись на радиокнопках
algo01 = Radiobutton(text="Инвертировать", variable=rBtn, value=0)
algo02 = Radiobutton(text="Замена с соседней", variable=rBtn, value=1)
algo03 = Radiobutton(text="+1", variable=rBtn, value=2)
algo04 = Radiobutton(text="+позиция (до 33)", variable=rBtn, value=3)

# Расположение радиокнопок
algo01.place(x=600, y=120)
algo02.place(x=600, y=140)
algo03.place(x=600, y=160)
algo04.place(x=600, y=180)

# Запуск окна
root.mainloop()