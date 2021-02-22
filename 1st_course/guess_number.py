import random #Для генерации случайного числа

lowDigit = 10 #Минимальное число
highDigit = 50 #Максимальное число
digit = 0 #число, загаданное компьютером

countInput = 0 #количество попыток угадать
win = False #Угадал число текущее?
playGame = True #Продолжается ли игра?
x = 0 #Число которе вводит пользователь
startScore = 100 #Начальное количество очков
score = 0 #Текущее количество очков
maxScore = 0 #Максимальное за сессию игры

#==============================================

                                #-----Главный цикл
while (playGame):
    digit = random.randint(lowDigit, highDigit)
    #print(f"Загаданное число: {digit}")
    print("-" * 30)
    countInput = 0
    score = startScore
    print("Компьютер загадал число, поробуйте его отгадать!")
    while(not win and score > 0):
        print("-" * 30)
        print(f"Заработано очков: {score}")
        print(f"Рекорд: {maxScore}")

                                   #-----------Внутренний цикл
        x = " "         
        while (not x.isdigit()):
            x = input(f"Введите число от {lowDigit} до {highDigit}: ")
            if (not x.isdigit()):
                print("." * 27 + "Введите, пожалуйста число.")

        x = int(x) #Преобразование из строки в целое число        
        if (x == digit):                  #Если ввели число загаданное компом
            print("Победа! Поздравляем!")            
            win = True
        else:
            length = abs(x - digit)
            if (length < 3):
                print("Очень горячо!")
            elif (length < 5):
                print("Горячо!")
            elif (length < 10):
                print("Тепло")
            elif (length < 15):
                print("Прохладно")
            elif (length < 20):
                print("Холодно")
            else:
                print("Ледяной ветер")
                                          #Стоимость подсказки
            if (countInput == 7):
                score -= 10
                if (digit % 2 == 0):
                    print("Число чётное")
                else:
                    print("Число нечётное")
            elif (countInput == 6):
                score -= 8
                if (digit % 3 == 0):
                    print("Число делится на 3")
                else:
                    print("Число не делится на 3")
            elif (countInput == 5):
                score -= 4
                if (digit % 4 == 0):
                    print("Число делится на 4")
                else:
                    print("Число не делится на 4")
            elif (countInput > 2 and countInput < 5):
                score -= 2
                if (x > digit):
                    print("Загданное число Меньше вашего")
                else:
                    print("Загданное число Больше вашего")
            score -= 5 #За каждый ход - 5 очков
        countInput += 1 #Обязательно увеличиваем количество сделанных ходов

    print("*" * 40)
    if (x == digit):
        print("Победа! Поздравляем!")            
    else:                   # В любом другом случае выход из цикла произойдет только
        print("Ой, у вас закончились очки. Вы проиграли :(") #Когда нет очков

    # Сыграть?
    if (input("Enter - сыграть ещё, 0 - выход ") == "0"):
        playGame = False
    else:
        win = False

    #Вычисляем максимальное количество очков
    if (score > maxScore):
        maxScore = score

#После завершения игры
print("*" * 40)
print("""Спасибо, что сыграли в мою игру!
Возвращайтесь скорей! Буду ждать с нетерпением!
P.S. Вы хорошо держались :)""")

#Конец
