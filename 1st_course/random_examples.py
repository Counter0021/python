import random #Для генерации случайного числа

lowDiapazon = 10 #Нижняя граница чисел
highDiapazon = 100 #Верхняя граница чисел
sign = 0 #Знак операции
playGame = True #Главный цикл
count = 0 #количество решенных примеров
right = 0 #Количество правильных ответов
score = 0 #очки

print("""Компьютер составляет пример. Введите ответ.
Для завершения работы введите STOP""")
print("*" * 40)

while (playGame):
    print(f"Ваши очки: {score}")
    print(f"Обработано задач: {count}")
    print(f"Правильных ответов: {right}")
    print("-" * 20)

    #генерация знака
    
    sign = random.randint(0, 3)
    # 0 - плюс
    # 1 - минус
    # 2 - умножить
    # 3 - делить

    # Сложение
    if (sign == 0):
        z = random.randint(lowDiapazon, highDiapazon)
        x = random.randint(lowDiapazon, z)
        y = z - x
        if(random.randint(0, 1) == 0):
            print(f"{x} + {y} = ?")
        else:
            print(f"{y} + {x} = ?")

    # Вычитание
    elif (sign == 1):
        x = random.randint(lowDiapazon, highDiapazon)
        y = random.randint(0, x - lowDiapazon)
        z = x - y
        print(f"{x} - {y} = ?")

    # Умножени
    elif (sign == 2):
        x = random.randint(1, (highDiapazon - lowDiapazon) //
                           random.randint(1, highDiapazon // 10) +1)
        y = random.randint(lowDiapazon, highDiapazon) // x
        z = x * y
        print(f"{x} * {y} = ?")

    #Деление
    elif (sign == 3):
        x = random.randint(1, (highDiapazon - lowDiapazon) //
                           random.randint(1, highDiapazon // 10) +1)
        y = random.randint(lowDiapazon, highDiapazon) // x
        if (y == 0):
            y = 1
        x = x * y
        z = x // y
        print(f"{x} / {y} = ?")

    user = " "
    while (not user.isdigit()
           and user.upper() != "STOP"
           and user.upper() != "S"
           and user.upper() != "Ы"
           and user.upper() != "ЫЕЩЗ"):
        user = input("Ваш ответ: ")

        if (user.upper() == "HELP"
                or user == "?"
                or user == ","
                or user.upper == "РУДЗ"):
            if (z > 9):
                print(f"Последняя цифра ответа: {z % 10}")
            else:
                print("Ответ состоит из 1 цифры, подсказка невозможна.")
            score -= 10

                #команда STOP
                
        elif (user.upper() == "STOP"
              or user.upper() == "S"
              or user.upper() == "Ы"
              or user.upper() == "ЫЕЩЗ"):
            playGame = False
        else:
            count += 1
            if (int(user) == z):
                print("Правильно!")
                right += 1
                score += 10
            else:
                print(f"Ответ неправильный... Правльно: {z}")
                print(f"Вы сможете ввести команду HELP или ? чтобы увидеть последнюю цифру ответа (-10 очков)")
                score -= 20
print("*" * 40)
print("Статистика игры: ")
print(f"Всего примеров: {count}")
print(f"Правильных ответов: {right}")
print(f"Неправильных ответов: {count - right}")



                

