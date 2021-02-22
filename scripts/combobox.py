#Выпадающий список Combobox
from tkinter import *
from tkinter import ttk

#Метод, который будет вызываться при выборе одного из пунктов меню
def showInTerminal(*args):
    lbl["text"] = cmbxSelect.get()
#Список значения для Combobox
def getValues(summa):
    value = []
    if(summa > 9):
        for i in range(0, 11):
            value.append(i * (int(summa) // 10))
    else:
        value.append(0)
        if(summa > 0):
            value.append(summa)
    return value

#Определяем окно
root = Tk()

#Размеры окна
root.geometry(f"{250}x{150}")

#Создаём Combobox
cmbx = ttk.Combobox(root)

#Запрещаем редактировать
cmbx["state"] = "readonly"

#Выводим на экран
cmbx.place(x=60, y=50)

#Определяем переменную, в которой будет храниться выбранное значение
#StringVar() - Тип "Строка"
cmbxSelect = StringVar()
cmbx["textvariable"] = cmbxSelect

#Значения в комбобокс
cmbx["values"] = getValues(10000)
#Устанавливаем активный выбор
#0 - самый первый из списка значений,
#1 - второй
#и т.д.
cmbx.current(0)

cmbx.bind("<<ComboboxSelected>>", showInTerminal)

lbl = Label(root, font="Arial 15")
lbl["text"] = "Здесь выбор"
lbl.place(x=10, y=10)

#Вывод окна на экран
root.mainloop()