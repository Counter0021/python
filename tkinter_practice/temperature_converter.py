# Перевод температуры

from tkinter import *

root = Tk()


# Перевод из цельсия в фаренгейт
def convertor():
    celsius_res = int(entry_celsius.get())
    fahrenheit = (celsius_res * 9 / 5) + 32
    labelTempConvertor['text'] = f'{fahrenheit}'

# *************************************************************
#       Переменные
# *************************************************************

WIDTH = 500
HEIGHT = 200

# *************************************************************
#       Формирование эллементов в окне
# *************************************************************

# Создаём главное окно
# Вычисляем координаты для размещения окна по центру
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2

# Установка заголовка окна
root.title("Temperature converter")

# Запрет изменения размеров окна
root.resizable(False, False)

# Устанавливаем ширину, высоту и позицию окна
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

# Текс
label_celsius = Label(text='Celsius: ')
label_fahrenheit = Label(text='Fahrenheit: ')
label_celsius.place(x=20, y=10)
label_fahrenheit.place(x=20, y=50)

labelTempConvertor = Label(text='Temperature in fahrenheits...')
labelTempConvertor.place(x=WIDTH // 2 - 80, y=50)

# Поле ввода
entry_celsius = Entry(root, width=100)
entry_celsius.place(x=WIDTH // 2 - 70, y=20, width=150)

# Кнопки
convert = Button(text='Convert')
convert.place(x=WIDTH // 2 - 50, y=130, width=100)
convert['command'] = convertor

root.mainloop()
