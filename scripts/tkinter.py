from tkinter import *
import random
root = Tk()

#Размеры окна
WIDTH = 320
HEIGHT = 240

#Вычисляем координаты для размещения окна по центру
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2

#Устанавливаем ширину, высоту и позицию
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

#Установка заголовка
root.title("Strange game")

#Запрещаем изменение размеров
root.resizable(False, False)

#кнопки
button01 = Button()
button01["text"] = "Press me"
button01.place(x=35, y = 200)

button02 = Button()
button02["text"] = "Press me"
button02.place(x=135, y = 200)

button03 = Button()
button03["text"] = "Press me"
button03.place(x=235, y = 200)

cmd = random.randint(1, 3)
if (cmd == 1):
    button01["command"] = quit
elif (cmd == 2):
    button02["command"] = quit
else:
    button03["command"] = quit

#Запуск программы
root.mainloop()