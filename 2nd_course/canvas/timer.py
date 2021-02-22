from tkinter import *

def plusSecond():
    global second, timerLink
    second += 1
    label["text"] = f"Прошло секунд: {second}"

    # Вызываем через 1 секунду
    timerLink = root.after(1000, plusSecond)

def startTimer():
    global timerLink
    timerLink = root.after(1000, plusSecond)

def stopTimer():
    global timerLink
    if (timerLink != None):
        # .after_cancel прекращает вызов
        root.after_cancel(timerLink)
        timerLink = None

root = Tk()
root.geometry(f"{320}x{240}")

startButton = Button(root, text="Старт")
startButton.place(x=10, y=50)
startButton["command"] = startTimer

stopButton = Button(root, text="Стоп")
stopButton.place(x=70, y=50)
stopButton["command"] = stopTimer

label = Label(root)
label.place(x=10, y=10)

# Секунды
second = 0
timerLink = None

plusSecond()
root.mainloop()