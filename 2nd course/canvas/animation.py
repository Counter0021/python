from tkinter import *

def pressSpace(event):
    global countAnimation

    # Не обрабатываем пробел
    cnv.unbind("<space>")

    countAnimation += 1
    if (countAnimation < 20):
        cnv.move(evil, 2, 0)
        root.after(50, lambda e=event : pressSpace(e))
    else:
        countAnimation = 0
        cnv.bind("<space>", pressSpace)

root = Tk()
root.geometry(f"{640}x{480}")

cnv = Canvas(root, width=640, height=480)
cnv.config(highlightthickness=0)
cnv.place(x=0, y=0)
cnv.focus_set()

# Загружаем изображения
evilCircle = PhotoImage(file="circle.png")
evil = cnv.create_image(120, 240, image=evilCircle)

# Назначаем на пробел метод pressSpace
cnv.bind("<space>", pressSpace)

# Количество рекурсий
countAnimation = 0

root.mainloop()